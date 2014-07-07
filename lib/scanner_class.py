#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import re
from nmap_class import NmapScanner
from pluginLoader_class import PluginLoader
from mysql_class import MySQLHelper
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
		
		# scan result
		self.result = {}

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

	def startScan(self,services=None):
		''' '''
		print '>>>starting scan'
		if services == None:
			services = self.services
		pl = PluginLoader(None,services)
		pl.loadPlugins()
		pl.runPlugins()
		self.result = pl.retinfo
		print pl.retinfo

	def saveResult(self, sqlcur):
		''' '''
		print '>>>saving scan result'
		sqlcmd = 'INSERT INTO '

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	sys.path.append('/root/workspace/Hammer/plugins')
	sys.path.append('../plugins')
	sn =Scanner('http://www.leesec.com')
	sn.getServices()
	print ">>>scan starting:"
	sn.startScan()
	print ">>>scan result:"
	print sn.result