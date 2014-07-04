#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import re
from nmap_class import NmapScanner
from pluginLoader_class import PluginLoader
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class Scanner(object):
	"""docstring for Scanner"""
	def __init__(self, url):
		super(Scanner, self).__init__()
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

		self.services = {}
	
	def getServices(self) :
		''' '''
		np = NmapScanner(self.host,self.ports)
		sc = np.scanPorts()
		try:
			self.services['url'] = self.url
			self.services['host'] = self.host
			self.services['ip'] = sc.keys()[0]
			self.services['ports'] ={}
			if sc[sc.keys()[0]].has_key('tcp'):
				self.services['ports'] .update(sc[sc.keys()[0]]['tcp'])
			if sc[sc.keys()[0]].has_key('udp'):
				self.services['ports'] .update(sc[sc.keys()[0]]['udp'])
		
			#print self.services
		except KeyError,e:
			pass

	def runPlugins(self,services=None):
		''' '''
		if services == None:
			services = self.services
		pl = PluginLoader()
		pl.loadPlugins()
		pl.runPlugins(services)
		
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	sys.path.append('/root/workspace/Hammer/plugins')
	sn =Scanner('http://www.leesec.com')
	sn.getServices()
	sn.runPlugins()
