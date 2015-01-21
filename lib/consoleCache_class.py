#!/usr/bin/python2.7
#coding:utf-8

import yaml

import globalVar

from consoleColor_class   import *
from sqlite3    import *
from os         import listdir,system
from random     import choice
from consoleLoad_class   import load
from consoleUser_class 	import WebUser
from dummy import BASEDIR

p_InfoCollect   = 'Info_Collect'
p_Common        = 'Common'
p_SensitiveInfo = 'Sensitive_Info'
p_System        = 'System'
p_WeakPassword  = 'Weak_Password'
p_WebApplications   = 'Web_Applications' 
p_Others        = 'Others'

pldict = {'info':'Info_Collect',
		'com':'Common',
		'sens':'Sensitive_Info',
		'sys':'System',
		'pwd':'Weak_Password',
		'web':'Web_Applications',
		'oth':'Others',
		}

class Cache(object):
	'''consoleCache=>Class::Cache'''
	def __init__(self,dbfile=BASEDIR+'/cache/hammer.sql',conffile=BASEDIR+'/cache/hammer.yaml'):
		super(Cache, self).__init__()
		self.db   = dbfile
		self.conffile = conffile
		self.user = WebUser()
		if self.user.name:
			self.username = self.user.name + '@' + self.user.server
		else:
			self.errmsg('has not logged in, please log in first!')
			self.username = 'anonymous@local'

		self.initGlobal()

	def initGlobal(self):
		'''init global variables'''
		if self.user.taskid:
			pass
		else:
			self.user.refreshTaskID()
		globalVar.scan_task_dict['scanID'] = self.user.taskid
		globalVar.scan_task_dict['server'] = self.user.server
		globalVar.scan_task_dict['token'] = self.user.token

	def initTask(self):
		''' '''
		self.user.refreshTaskID()


	def start(self):
		'''start Cache'''
		color.cprint("[*] Start hammer console ..",GREEN)
		self.runsql("create table if not exists plugin(id integer primary key,type text,path text)")
		self.runsql("delete from plugin")
		self.inscache(self.getplus(p_InfoCollect),p_InfoCollect)
		self.inscache(self.getplus(p_Common),p_Common)
		self.inscache(self.getplus(p_SensitiveInfo),p_SensitiveInfo)
		self.inscache(self.getplus(p_System),p_System)
		self.inscache(self.getplus(p_WeakPassword),p_WeakPassword)
		self.inscache(self.getplus(p_WebApplications),p_WebApplications)
		self.banner()

	def getplus(self,path):
		'''get plugins list'''
		ret = []
		for plugin in listdir(BASEDIR+'/plugins/'+path):
			if plugin[-3:] == '.py' and plugin != 'dummy.py' and plugin !='__init__.py':
				ret.append(plugin)
		return ret

	def inscache(self,c,p):
		'''insert data to cache'''
		for tmp in c:
			tmp=tmp[:-3]
			self.runsql('insert into plugin(type,path) values("%s","%s/%s")'%(p,p,tmp))
					
	def runsql(self,sql):
		'''execute a sql'''
		conn=connect(self.db)
		conn.execute(sql)
		conn.commit()
		conn.close()

	def setconf(self,name,value):
		'''set config'''
		try:
			if name == 'server':
				self.user.setUserInfo(server=value)
			elif name == 'token':
				self.user.setUserInfo(token=value)
			else:
				self.usage('set')
		except Exception,e:
			color.cprint("[!] Err:%s"%e,RED)

	def connect(self):
		''' '''
		self.user.rsyncUserInfo()
		self.username = self.user.name + '@' + self.user.server
		self.initGlobal()

	def sql_all(self,sql):
		'''sqlite3=>cur.fetchall()'''
		conn=connect(self.db)
		cur=conn.cursor()
		cur.execute(sql)
		tmp=cur.fetchall()
		cur.close()
		conn.close()
		return tmp
	
	def search(self,sear):
		'''search plugins'''
		sql='select * from plugin where path like "%'+sear+'%"'
		result=self.sql_all(sql)
		msg="SEARCH '%s'"%sear
		color.cprint(msg,YELLOW)
		color.cprint("="*len(msg),GREY)
		self.listmst(result)
			
	def listmst(self,result):
		'''format print results'''
		color.cprint("%5s %-60s %-7s"%("ID","PATH","TYPE"),YELLOW)
		color.cprint("%5s %-60s %-7s"%("-"*5,"-"*60,"-"*7),GREY)
		for res in result:
			rid=res[0]
			rty=res[1]
			rpa=res[2]
			if len(rpa)>70:
				rpa=rpa[:68]+".."
			color.cprint("%5s %-60s %-7s"%(rid,rpa,rty),CYAN)
		color.cprint("="*74,GREY)
		color.cprint("COUNT [%s] RESULTS (*^_^*)"%len(result),GREEN)
			
	def showplus(self,p):
		'''show plugins'''
		if pldict.has_key(p):
			p = pldict[p]
		elif p == 'all':
			pass
		else:
			self.usage('show')

		pp=("show %s plugins"%p).upper()
		color.cprint(pp,YELLOW)
		color.cprint("="*len(pp),GREY)
		if p == 'all':
			sql='select * from plugin'
		else:
			sql="select * from plugin where type='%s'"%p
		self.listmst(self.sql_all(sql))

	def showuser(self):
		''''''
		pp=("show user information").upper()
		color.cprint(pp,YELLOW)
		color.cprint("="*len(pp),GREY)
		color.cprint(("\tserver:\t\t%s" % self.user.server),CYAN)
		color.cprint(("\ttoken:\t\t%s" % self.user.token),CYAN)
		color.cprint(("\tuser id:\t%s" % self.user.id),CYAN)
		color.cprint(("\tuser name:\t%s" % self.user.name),CYAN)
		color.cprint(("\tscan id:\t%s" % self.user.taskid),CYAN)
		color.cprint("="*74,GREY)

	def load(self,plugin):
		'''load plugins'''
		def getplu(pid):
			'''pid 2 pluName'''
			conn=connect(self.db)
			cur=conn.cursor()
			cur.execute('select * from plugin where id=%s'%pid)
			tmp=cur.fetchone()
			cur.close()
			conn.close()
			pat=tmp[2]
			pty=tmp[1]
			return pat

		def noload():
			'''no this plugin | plugin is payload'''
			color.cprint("[!] NO THIS PLUGIN !",RED)
		try:
			pid=int(plugin)
			if len(self.sql_all('select * from plugin where id=%s'%pid))==0:
				noload()
			else:
				plu=getplu(pid)
				if len(plu)>0:
					pt=plu.split("/")[0]
					# print pt,plu
					load.start(pt,plu)

		except:
			if len(self.sql_all('select * from plugin where path="%s"'%plugin))==0:
				noload()
			else:
				pt=plugin.split("/")[0]
				load.start(pt,plugin)
							
	def getplunums(self,p):
		'''get plugins nums'''
		if p == 'all':
			return len(self.sql_all('select * from plugin'))
		else:
			return len(self.sql_all('select * from plugin where type="%s"'%p))

	def mainhelp(self):
		'''show mainhelp'''
		color.cprint('HAMMER COSOLE COMMAND HELP MENU',YELLOW)
		color.cprint('=============',GREY)
		color.cprint('        COMMAND         DESCRIPTION',YELLOW)
		color.cprint('        -------         -----------',GREY,0)
		color.cprint('''
	help		Displays the help menu
	exit		Exit the Hammer console mode
	cls 		Clear the screen
	set 		Set server and token
	connect 	Connect to server
	show 		List the plugins
	search 		Search plugins
	use 		Use the plugin''',CYAN)
		color.cprint('HAMMER HELP::SHOW',YELLOW)
		color.cprint('==============',GREY)
		color.cprint('        COMMAND         DESCRIPTION',YELLOW)
		color.cprint('        -------         -----------',GREY,0)
		color.cprint('''
	info 		List the Info_Collect plugins
	com 		List the Common plugins
	... 		Others: sens|sys|pwd|web
	all 		List all the plugins
	user 		Show user information
''',CYAN)

	def usage(self,c):
		'''mst=>usage'''
		def ius(c):
			'''def's def =.='''
			color.cprint('[?] USAGE:%s'%c,YELLOW)
		if   c == "search":
			ius('search <plugin>')
		elif c == "show":
			ius('show <info|com|sens|sys|pwd|web|all|user>')
		elif c == "use":
			ius('use <plugin|pluginID>')
		elif c == "set":
			ius('set <server|token> <valus>')

	def ban1(self):
		'''banner 1'''
		color.cprint('''
	   ██░ ██  ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
	  ▓██░ ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
	  ▒██▀▀██░▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
	  ░▓█ ░██ ░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
	  ░▓█▒░██▓ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
	   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
	   ▒ ░▒░ ░  ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
	   ░  ░░ ░  ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
	   ░  ░  ░      ░  ░       ░          ░      ░  ░   ░     
''',YELLOW)
	def ban2(self):
		color.cprint('''
                                                                    
                                   ,i77SSXrr,     ,ii               
                            7aWMMMMMMMMMMMMMMMMMMMMMMM              
                        7@MMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                       :MMMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                        WMMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                        ,MMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                         ,MMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                          @MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                          XMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           BMMMMMMMMMMMMMMMMMMMMMMMMMMr             
                           SMMMMMMMMMMMMMMMMMMMMMMMMMMM             
                           iMMMMMMMMMMMMMMMMMMMMMMMMMMMX         7; 
                            MMMMM@B8Z2SXXr;;;:,.,,. . . ,;XZBMMMMMM:
                            S7,.   ..::ii;;7XXX2ZBB@MMMMMMMMMMMMMMMi
                      .:;72aZ8B@MMMMMMMMMMMMMMMMMMMMMMMMMMBaXi.     
              BMMMMMMMMMMMMMMMMMMMMM8a22SXrr;i,:rZZZi               
              XMMMMMWB0Za2X;,:MMMMMWS          7WM.             
                 
''',BLUE)
	def ban3(self):
		color.cprint('''
                                        ,-,                     
                                   -x#######=                   
                                =########XX##+                  
                             .x#########XxXx#x=                 
                            X###########XxxXX#=-                
                          .##########X####Xxxxx=                
                          =###XXxX+xX#X##########x=-            
                          +#XxxX#######################=.       
                         -###########X++x+--;+x###########-     
                       =#########X;.  .         ;-X#########.   
                     +#########+,    ,      ,   .  ;#########   
                   -#########- .    -      -.   ..  ;+#######,  
                  =########+,      =;.    --     -  ..=#####+   
                 .########-    .; =;    ,+- .   X ;  ,.X##x     
                 +#######+ ;   -.-.    =+.    .#. = , .#x       
                 ,#######----  = ,   ;+,    .x# ,X, - ;x#       
                  .#######+--= =    ==   ;=-,, -X#===.x=##      
                     ;+X#=-x+=;-  X#+,.,+++X=-#;  ,;;x+#-.-     
                        -   ####x#==--+-., X-.X;=#+; =x#        
                       .; -+-##. -  X##=   =  .,X#+  -#,        
                        =     x   +       ,.   ;     x=         
                         ;-,, +    -;...,.       ..;-x          
                            .##=                     x          
                             +  =                   -;          
                                 +                -+.           
                                  =X+,.        ,==,   
''',CYAN)
	def ban4(self):
		color.cprint('''
                             .;+it+;+tt=:                       
                          .iYi;=YY   .IXXXI;                    
                        :IXV,     iX   t+iRBV,                  
                       IVItY  ,#; =#     ,  Y#=                 
                     .XIttIt,  Mi.XV#I ,; ,.  :i                
                     RttYI,  .   :###Y  ,;..., +:               
                    YItI=  .,,:    .           =: :::           
                    Xtt+ ...             :=Y#I .i;,,:+,         
                    RtI      ,=itYRM#########   V     I         
                    XIt  ::#################;  ;R,   =;         
                    iYI    B###BRXVYVVVVBW#X   tVItiV.          
                     VIi    +BBRVVVVVVYVVBI    ItttB:           
                  ::,.YY;     +XWMMRRRRBB;    tttiVi            
                ,+,. ,:iV=       ;iIIIII:,IM##XtiYY             
                t.    ,tXBt.       :IRMt=XR,  tIYI              
                ,+.   +titIYt;=RW#WRt;:;;M=    Vt .;::          
                 .;;=YRItittttXBX:     ,:::   ,;V,,..,+;        
                      ,iYVItttitt             ;,=      +;       
                         ,iYVItiI ,           :         t       
                            .;Ytt; ;        .,.t        =:      
                              :VtI; ...   ..,:IY        i.      
                              ;YttII=;:::;=iIIIIt      :+       
                             = ItittttIIIIIYXVYYVY=:::==        
                            :; tIttttttIYXI=,      ,,,          
                            =:  tYIIIIVI=                       
                            ,+   .,:.i,                         
                             ==     ;,                          
                              ,;;;;:                            
''',PURPLE)
	def banner(self):
		'''mst banner :)'''
		ic=self.getplunums('Info_Collect')
		co=self.getplunums('Common')
		si=self.getplunums('Sensitive_Info')
		sy=self.getplunums('System')
		wp=self.getplunums('Weak_Password')
		wa=self.getplunums('Web_Applications')
		choice([self.ban1,self.ban2,self.ban3,self.ban4])()
		print '          =[',
		color.cprint('HAMMER::My Sec Tools',GREEN)
		print '    + -- +=[',
		color.cprint('PLU::info::%s com::%s sens::%s sys::%s pwd::%s web::%s'%(ic,co,si,sy,wp,wa),YELLOW)
		
	def printhammer(self):
		'''print mst..'''
		color.cprint(self.username,GREY,0)
			
	def execmd(self,cmd):
		'''run system command'''
		color.cprint('[*] EXEC:%s'%cmd,RED)
		system(cmd)
			
	def cls(self):
		'''clear'''
		if name == 'nt':
			system("cls")
		else:
			system("clear")

	def errmsg(self,msg):
		'''show error msg'''
		color.cprint("[!] Err:%s"%msg,RED)
			
	def mainexit(self):
		'''exit app'''
		color.cprint("\n[*] GoodBye :)",RED)
		exit(0)

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	print __doc__
# else:
# 	cache=Cache()
# 	#cache.start()
