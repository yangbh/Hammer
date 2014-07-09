#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import sys
from dummy import LIBDIR
sys.path.insert(0, LIBDIR +'/knock/modules')

try:
		import knockcore
except ImportError:
		print '[!] knockcore not found.'
		print sys.path
		sys.exit(0)
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class SubDomain(object):
	"""docstring for SubDomain"""
	# 静态成员
	# INFORMATION
	NAME		= "Knock Subdomain Scan"
	VERSION		= "2.0"
	AUTHOR		= "Author: Gianni 'guelfoweb' Amato"
	GITHUB		= "Github: https://github.com/guelfoweb/knock"
	INFO		= NAME+" v."+VERSION+" - Open Source Project\n"+AUTHOR+"\n"+GITHUB

	# color const
	COLOR_ALIAS = '\033[93m'
	COLOR_RED   = '\033[91m'
	COLOR_BOLD  = '\033[1m'
	COLOR_END   = '\033[0m'

	def __init__(self, host, wordlist=LIBDIR + "/knock/wordlist.txt"):
		super(SubDomain, self).__init__()
		self.host 		= host
		self.wordlist	= wordlist
		self.found 		= []


	def uniq_by_array(self,array):
		uniq_ip   = []
		uniq_name = []
		array_row = len(array)
		for i in range(0,array_row):
			a  = array[i][0]
			b  = array[i][1]
			if a not in uniq_ip:
				uniq_ip.append(a)
			if b not in uniq_name:
				uniq_name.append(b)

		print self.COLOR_BOLD + "Ip Addr Summary" + self.COLOR_END
		print "-"*15
		for i in range(0,len(uniq_ip)):
			print uniq_ip[i]

		host_found = len(uniq_ip)
		name_found = len(uniq_name)
		print "\nFound "+str(name_found)+" subdomain(s) in "+str(host_found)+" host(s)."
		

	def resolvedomain(self,subdomain):
		result    = knockcore.domaininfo(subdomain)

	#		 [ 4 x 3 ]								[ 3 x 3 ]
	#		 [['hostname'],                0
	#		  ['alias', 'alias', 'ip'],    1 0
	#		  ['alias', 'alias', 'ip'],    2 1
	#		  ['alias', 'alias', 'ip']]    3 2
	#		      0        1      2

	#		 [ 3 x 3 ]								[ 2 x 3 ]
	#		 [['login.lga1.b.yahoo.com'], 														  0
	#		  ['login.yahoo.com',               'l2.login.vip.bf1.yahoo.com', '98.139.237.162'],  1 0
	#		  ['login-global.lgg1.b.yahoo.com', 'l2.login.vip.bf1.yahoo.com', '98.139.237.162']]  2 1
	#		                 0                                 1                       2

		# subdomain is alias
		if result and len(result) == 2 and len(result[1]) == 2:
			hostname = result[0][0]
			alias    = result[1][0]
			ip       = result[1][1]
			#print 1
			print self.COLOR_ALIAS + ip+"\t"+alias + self.COLOR_END
			print ip+"\t"+hostname
			self.found.append([ip, alias])
			#self.found.append([ip, hostname])
		# subdomain is alias
		elif result and len(result) == 2 and len(result[1]) == 3:
			hostname = result[0][0]
			alias    = result[1][0]
			name     = result[1][1]
			ip       = result[1][2]
			#print 2
			print self.COLOR_ALIAS + ip+"\t"+alias + self.COLOR_END
			print ip+"\t"+hostname
			self.found.append([ip, alias])
			#self.found.append([ip, hostname])
		# subdomain is alias
		elif result and not len(result) == 2 and not False:
			uniq = []
			for i in range(1,len(result)):
				ip_alias = result[i][2]+"\t"+result[i][0]
				ip_name  = result[i][2]+"\t"+result[i][1]
				
				if ip_alias not in uniq:
					uniq.append(ip_alias)
					#print 3
					print self.COLOR_ALIAS + ip_alias + self.COLOR_END
					self.found.append([result[i][2], result[i][0]])
				if ip_name not in uniq:
					uniq.append(ip_name)
					print ip_name
					self.found.append([result[i][2], result[i][1]])
			for i in range(1,len(result)):
				ip_hostname  = result[i][2]+"\t"+result[0][0]
				if ip_hostname not in uniq:
					uniq.append(ip_hostname)
					print ip_hostname
					#self.found.append([result[i][2], result[0][0]])
		# subdomain is hostname
		elif result:
			hostname = result[0][0]
			ip       = result[1][0]
			#print 4
			print ip+"\t"+hostname
			self.found.append([ip, hostname])

	def loadwordlist(self,wordlist):
		wlist = knockcore.loadfile(wordlist)

		if wlist == False:
			print self.COLOR_RED + "\nFile not found ["+wordlist+"]" + self.COLOR_END
			print "Download a wordlist file from here:"
			print "https://raw.github.com/guelfoweb/knock/master/wordlist.txt"
			sys.exit(0)
		return wlist

	def subscan(self,url,wordlist):
		#url = self.host
		#wordlist = self.wordlist
		wlist = self.loadwordlist(wordlist)

		print self.COLOR_BOLD + "Getting subdomain for", url + self.COLOR_END
		print "\nIp Address\tDomain Name"
		print "----------\t-----------"

		for sub in wlist:
			subdomain = sub+"."+url
			self.resolvedomain(subdomain)

		print
		self.uniq_by_array(self.found)

	def bypasswildcard(self,url, wordlist):
		wlist = self.loadwordlist(wordlist)

		print self.COLOR_BOLD + "\nGetting subdomain for", url + self.COLOR_END
		print "\nIp Address\tDomain Name"
		print "----------\t-----------"

		for sub in wlist:
			subdomain = sub+"."+url
			header = knockcore.getheader(subdomain, "/", "GET")
			# bypass status code -> header[0] = 301
			if header and not header[0] == 301:
				self.resolvedomain(subdomain)

		print
		self.uniq_by_array(found)

	def checkzone(self,domain):
		print  self.COLOR_BOLD + "Getting NS records for", domain + self.COLOR_END
		print "\nIp Address\tServer Name"
		print "----------\t-----------"
		zt_found = knockcore.zonetransfer(domain)
		if (zt_found):
			print self.COLOR_BOLD + "Getting Zone Transfer\n" + self.COLOR_END
			print "Ip Address\tDomain Name"
			print "----------\t-----------"
			for sub in zt_found:
				self.resolvedomain(sub)
			print
		else:
			return False

	def getheaders(self,url, path, method):
		# Status -> header[0] 
		# Reason -> header[1]
		# Header -> header[2]
		header = knockcore.getheader(url, path, method)
		status = str(header[0])
		reason = str(header[1])
		print self.COLOR_BOLD + "Staus\tReason" +  self.COLOR_END
		print "-----\t------"
		print status + "\t" + reason
		print
		print self.COLOR_BOLD + "Response Headers" +  self.COLOR_END
		print "-"*16
		for i in range(1,len(header[2])):
			print str(header[2][i][0]) + ": " + str(header[2][i][1])
		return status, reason

	def CheckForWildcard(self,url):
		# test wildcard and return True or False
		wildcard  = knockcore.testwildcard(url)
		
		if wildcard == False:
			return False
		else:
			print self.COLOR_RED+self.COLOR_BOLD+"Wildcard enabled\n"+self.COLOR_END

	def check_status(self,url, path, method):
		try:
			header   = knockcore.getheader(url, path, method)
			status   = str(header[0])
			reason   = str(header[1])
			response = header[2]
			return status, reason, response
		except:
			sys.exit(0)

	def purgeurl(self,url):
		url = url.replace("http://","")
		url = url.replace("/","")
		return url

	def help(self):
		print self.COLOR_BOLD+self.INFO+self.COLOR_END
		print
		print self.COLOR_BOLD+"Usage:"+self.COLOR_END+" knock.py domain.com"
		print self.COLOR_BOLD+"Usage:"+self.COLOR_END+" knock.py domain.com "+self.COLOR_BOLD+"--worlist "+self.COLOR_END+"wordlist.txt"
		print "\n\t-h, --help\tThis help"
		print "\t-v, --version\tShow version"
		print "\t    --wordlist\tUse personal wordlist"
		print self.COLOR_BOLD+"\nOptions for single domain"+self.COLOR_END
		print "-"*25
		print "\t-i, --info\tShort information"
		print "\t-r, --resolve\tResolve domain name"
		print "\t-w, --wildcard\tCheck if wildcard is enabled"
		print "\t-z, --zone\tCheck if Zonte Transfer is enabled"
	#	print "\t    --get\tRequest HTTP for GET method"
	#	print "\t    --post\tRequest HTTP for POST method"
	#	print "\t    --head\tRequest HTTP for HEAD method"
	#	print "\t    --trace\tRequest HTTP for TRACE method"
	#	print "\t    --options\tRequest HTTP for OPTIONS method"
		print "\n"+" "*9+self.COLOR_BOLD+"Usage:"+self.COLOR_END+" knock.py"+self.COLOR_BOLD+" [-opt, --option]"+self.COLOR_END+" domain.com"
		print "\nNote: The ALIAS name is marked in yellow."
		sys.exit(0)
	
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	import MySQLdb
	import mysql_class

	try:
		sql = mysql_class.MySQLHelper('192.168.1.2','mac_usr','mac_pwd')
		sql.selectDb('hammer')

		sqlcmd="SELECT * FROM host"
		sql.cur.execute(sqlcmd)
		host=sql.cur.fetchone()
		while host:
			#print host[1]
			host=host[1]
			host=sql.cur.fetchone()

		host='sohu.com'
		sb=SubDomain(host)
		#sb.help()
		if 	sb.CheckForWildcard(sb.host) != False:
			sys.exit(1)

		sb.checkzone(sb.host)
		sb.subscan(sb.host,sb.wordlist)
		print sb.found

		for each_found in sb.found:
			try:
				# IP表
				sqlcmd="SELECT * FROM company WHERE Name='搜狐' LIMIT 1"
				print sqlcmd
				sql.cur.execute(sqlcmd)
				comp_id=sql.cur.fetchone()[0]
				
				ip_addr=each_found[0]
				sqlcmd="INSERT INTO IP(Addr,Comp_ID) VALUES('%s',%d)" %(ip_addr,comp_id)
				print sqlcmd
				sql.cur.execute(sqlcmd)

				# host表
				host=each_found[1]
				sqlcmd="SELECT * FROM ip WHERE Addr='%s' AND Comp_ID=%d LIMIT 1" % (ip_addr,comp_id)
				print sqlcmd
				sql.cur.execute(sqlcmd)
				ip_id=sql.cur.fetchone()[0]
				sqlcmd="INSERT INTO host(Value,IP_ID,Comp_ID) VALUES('%s',%d,%d)" %(host,ip_id,comp_id)
				print sqlcmd
				sql.cur.execute(sqlcmd)
				sql.conn.commit()

			except MySQLdb.IntegrityError,e:
				print e
			except MySQLdb.OperationalError,e:
				sql = mysql_class.MySQLHelper('192.168.1.2','mac_usr','mac_pwd')
				sql.selectDb('hammer')
				print e

		sql.conn.commit()
		sql.cur.close()
		sql.conn.close()
	except TypeError,e:
		print e