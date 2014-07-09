#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import re
import threading
from nmap_class import NmapScanner
from pluginLoader_class import PluginLoader
from mysql_class import MySQLHelper
from dummy import PLUGINDIR, BASEDIR
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class MutiScanner(threading.Thread):
	def __init__(self, lock, threadName,pluginheader):  
		'''@summary: 初始化对象。 	
	 	@param lock: 琐对象。 
		@param threadName: 线程名称。 
		'''
		super(MutiScanner, self).__init__(name = threadName)  #注意：一定要显式的调用父类的初始 化函数。  
		self.lock = lock
		self.threadName = threadName

		if type(pluginheader) == PluginLoader:
			self.pl = pluginheader
		else:
			print 'pl is not a pluginLoader_class.PluginLoader class'

	def run(self):  
		''''''  
		self.lock.acquire() 
		print self.threadName, 'staring'
		self.lock.release()

		self.pl.loadPlugins()
		self.pl.runPlugins()

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class Scanner(object):
	"""docstring for Scanner"""
	def __init__(self, url):
		super(Scanner, self).__init__()
		#url
		if url[-1] != '/':
			url += '/'
		self.url = url
		m = re.match('(http[s]?)://([^:^/]+):?([^/]*)/',url)
		if m:
			self.http_type = m.group(1)
			self.host = m.group(2)
			self.ports = m.group(3)
			self.domain = self.host[self.host.find('.')+1:]
		else:
			print 'not a valid url',url
			sys.exit(0)
		commonports = '21,22,23,25,110,53,67,80,443,1521,1526,3306,3389,8080,8580'
		if self.ports != '':
			self.ports = commonports + ',' +ports
		else:
			self.ports = commonports

		# every plugin's input argument services
		self.services = {}
		self.services['url'] = self.url
		self.services['host'] = self.host
		self.services['ports'] = [self.ports]
		self.services['http'] = []
		
		# scan result
		self.result = {}

		# thread arguments
		self.lock = threading.Lock()  

	def getServices(self) :
		''' '''
		# services type: dict
		# services = {
		# 	url:'http://www.leesec.com/',
		# 	ip:'106.187.37.47',
		# 	port:[22,80,3306],
		# 	host: 'www.leesec.com',
		# 	cms:'wordpress',
		# 	cmsversion:'3.9.1'
		# }
		# if host is a neiboorhost
		# services ={
		# 	'host':'***.***.***'
		# 	'mainhost':'www.leesec.com',
		# 	...
		# }
		# if domain is a sondomain
		# services ={
		# 	'host':'mail.leesec.com',
		# 	'fardomain':'www.leesec.com',
		# 	...
		# }		# 
		print '>>>getting services'
		np = NmapScanner(self.host,self.ports)
		sc = np.scanPorts()
		try:
			self.services['url'] = self.url
			self.services['host'] = self.host
			self.services['ip'] = sc.keys()[0]
			self.services['ports'] = []
			self.services['detail'] = {}
			if sc[sc.keys()[0]].has_key('tcp'):
				self.services['detail'].update(sc[sc.keys()[0]]['tcp'])
				for eachport in sc[sc.keys()[0]]['tcp']:
					self.services['ports'].append(eachport)
			if sc[sc.keys()[0]].has_key('udp'):
				self.services['detail'].update(sc[sc.keys()[0]]['udp'])
				for eachport in sc[sc.keys()[0]]['udp']:
					self.services['ports'].append(eachport)
			
			# neiborhood weisites
			self.services['http'] = []

			print 'services:\t',self.services
		except KeyError,e:
			pass

	def getSubDomains(self,domain=None):
		if domain == None:
			domain = self.domain
		return [self.host]

		pl = PluginLoader(None,services)
		pl.loadPlugins(PLUGINDIR+'/Info_Collect')
		pl.runPlugins()
		print pl.services

	def getNeiboorHosts(self,host=None):
		if host == None:
			host = self.host
		return [self.host, 'www.hengtiansoft.com']

	def startScan(self,services=None):
		''' '''
		print '>>>starting scan'
		print '>>>collecting subdomain info'
		subdomains = self.getSubDomains(self.domain)
		print 'subdomains:\t',subdomains
		domains=[]
		print '>>>for each subdomain, collecting neiborhood host info'
		for eachdomain in subdomains:
			tmp={}
			tmp['domain'] = eachdomain
			tmp['hosts'] = self.getNeiboorHosts()
			domains.append(tmp)
			print 'for subdomain',eachdomain,'neiborhood hosts are:\t',tmp['hosts']

		print '>>>starting scan each host'
		
		pls = []
		for eachdomain in domains:
			for eachhost in eachdomain['hosts']:
				services = {}
				if eachdomain['domain'] != self.host:
					services['fardomain'] = self.domain
				if eachdomain['domain'] !=eachhost:
					services['mainhost'] = eachdomain
				services['url'] = 'http://' + eachhost + '/'
				services['host'] = eachhost

				pl = PluginLoader(None,services)
				pls.append(pl)
				print pl.services

		print pls
		mthpls=[]
		for eachpl in pls:
			mthpl = MutiScanner(self.lock,eachpl.services['host'],eachpl)
			mthpls.append(mthpl)

		for eachmthpl in mthpls:
			eachmthpl.start()

		for eachmthpl in mthpls:
			eachmthpl.join()

		for eachpl in pls:
		# 	eachpl.loadPlugins()
		# 	eachpl.runPlugins()
		 	self.result[eachpl.services['host']] = eachpl.retinfo

	def saveResult(self, sqlcur):
		''' '''
		print '>>>saving scan result'
		sqlcmd = 'INSERT INTO '

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	basepath = BASEDIR
	sys.path.append(basepath +'/lib')
	sys.path.append(basepath +'/plugins')
	sys.path.append(basepath +'/bin')
	sys.path.append('/root/workspace/Hammer')

	sn =Scanner('http://www.leesec.com')
	sn.startScan()
	print ">>>scan result:"
	print sn.result