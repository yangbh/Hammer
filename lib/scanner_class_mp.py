#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import time
import re
import socket
import threading
import urllib2
import logging
import multiprocessing

import globalVar

from pprint import pprint

from nmap_class import NmapScanner
from pluginLoader_class import PluginLoader
from mysql_class import MySQLHelper
from spider.domain import GetFirstLevelDomain
from webInterface_class import WebInterface
from dummy import *

# multiprocessing.set_start_method('forkserver')
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def procFunc(pluginheader):
	if type(pluginheader) == PluginLoader:
		pl = pluginheader
		pl.loadPlugins()
		pl.runPlugins()
		return pl
	else:
		print 'pl is not a pluginLoader_class.PluginLoader class'
		return None

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
class Scanner(object):
	"""docstring for Scanner"""
	def __init__(self,url=None,server=None,session=None):
		super(Scanner, self).__init__()
		#url
		if url[-1] != '/':
			url += '/'
		self.url = url

		# web server class
		self.web_interface = None
		if server and session:
			self.web_interface = WebInterface(server,session)

		m = re.match('(http[s]?)://([^:^/]+):?([^/]*)/',url)
		if m:
			self.http_type = m.group(1)
			self.host = m.group(2)
			self.ports = m.group(3)
			self.ip = socket.gethostbyname(self.host)
			self.domain = GetFirstLevelDomain(self.host)
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
		# self.lock = threading.Lock()

		# urls
		self.urls = {}
		# pluginloaders
		self.pls = []

	def getSubDomains(self,host=None):
		if host == None:
			host = self.host
		services={}
		services['host'] = host
		services['noSubprocess'] = True
		pl = PluginLoader(None,services)
		pl.runEachPlugin(PLUGINDIR+'/Info_Collect/subdomain.py')
		print pl.services
		subdomains = pl.services['subdomains']
		return subdomains

	def getNeiboorHosts(self,ip=None):
		if ip == None:
			ip = self.ip
		services={}
		services['ip'] = ip
		services['noSubprocess'] = True
		pl = PluginLoader(None,services)
		pl.runEachPlugin(PLUGINDIR+'/Info_Collect/neighborhost.py')
		neighborhosts = []
		if pl.services.has_key('neighborhosts'):
			neighborhosts = pl.services['neighborhosts']
		return neighborhosts

	def getHttpPorts(self,ip=None):
		if ip == None:
			ip = self.ip
		services={}
		services['ip'] = ip
		services['noSubprocess'] = True
		# get all opened ports
		pl = PluginLoader(None,services)
		pl.runEachPlugin(PLUGINDIR+'/Info_Collect/portscan.py')
		ports = {}
		if pl.services.has_key('port_detail'):
			ports = pl.services['port_detail']

		# get http ports
		httpports = []
		for eachport in ports.keys():
			if ports[eachport]['name'] == 'http':
				httpports.append(eachport)
		print 'httpports:\t',httpports
		return httpports

	def generateUrl(self,ip=None,hosts=None,ports=None):
		''''''
		# url redict  hasn't been considered
		urls = []
		tmpurls = []
		if hosts != None:
			for eachhost in hosts:
				url = 'http://' + eachhost
				tmpurls.append(url)
				url = 'https://' + eachhost
				tmpurls.append(url)

		if ip != None and ports != None:
			for eachport in ports:
				url = 'http://' + ip + ':' + str(eachport)
				tmpurls.append(url)
				url = 'https://' + ip + ':' + str(eachport)
				tmpurls.append(url)

		for url in tmpurls:
			try:
				respone = urllib2.urlopen(url)
				redirected = respone.geturl()
				if redirected == url:
					urls.append(url)
				continue
			except urllib2.URLError,e:
				#print 'urllib2.URLError',e,url
				pass
			except urllib2.HTTPError,e:
				#print 'urllib2.HTTPError',e,url
				pass
			except urllib2.socket.timeout,e:
				#print 'urllib2.socket.timeout',e,url
				pass
			except urllib2.socket.error,e:
				#print 'urllib2.socket.error',e,url
				pass

		return urls

	def startScan(self,services=None):
		''' '''
		try:
			print '>>>starting scan'
			self._noticeStartToWeb()
			self._initGlobalVar()
			# get subdomains
			print '>>>collecting subdomain info'
			subdomains = self.getSubDomains(self.host)
			print 'subdomains:\t',subdomains

			# get hosts
			hosts={}
			print '>>>for each subdomain, collecting neiborhood host info'
			for eachdomain in subdomains:
				tmpip = socket.gethostbyname(eachdomain)
				if tmpip not in hosts.keys():
					tmphosts = self.getNeiboorHosts(tmpip)
					hosts[tmpip] = tmphosts
					if eachdomain not in tmphosts:
						hosts[tmpip].append(eachdomain)

				else:
					if eachdomain not in hosts[tmpip]:
						hosts[tmpip].append(eachdomain)

			print 'hosts:\t',hosts

			# get urls
			urls = {}
			for eachip in hosts.keys():
				ip_hosts = hosts[eachip]
				httpports = self.getHttpPorts(eachip)
				urls[eachip] = self.generateUrl(eachip,ip_hosts,httpports)

			# just for test
			# urls = {'106.185.36.44': ['http://www.hengtiansoft.com','http://www.leesec.com']}
			# urls = {'10.183.0.103': []}
			urls = {'106.185.36.44': ['http://www.leesec.com']}
			
			self.urls = urls
			print 'urls\t',urls

			# get services
			print '>>>starting scan each host'		
			pls = []
			# ip type scan
			for eachip in urls.keys():
				services = {}
				if eachip !=  self.ip:
					services['issubdomain'] = True

				services['ip'] = eachip
				pl = PluginLoader(None,services,outputpath=self.host)
				pls.append(pl)
				print 'scan start:\t',pl.services

			# http type scan
			for eachip in urls.keys():
				for eachurl in urls[eachip]:
					services = {}
					# not subdomain
					if self.domain not in eachurl:
						services['isneighborhost'] = True

					services['url'] = eachurl

					pl = PluginLoader(None,services,outputpath=self.host)
					pls.append(pl)
					print 'scan start:\t',pl.services

			results = []

			proPool = multiprocessing.Pool(8)
			for eachpl in pls:
				results.append(proPool.apply_async(procFunc,(eachpl,)))

			proPool.close()

			try:		
				proPool.join()
			except EOFError,e:
				# isexit = raw_input('Sure to exit?yes/no')
				# if isexit.lower() == 'y' or isexit.lower() == 'yes':
				proPool.terminate()


			newpls = []
			for res in results:
				newpls.append(res.get())
			self.pls = newpls

			self.setResult(urls=self.urls,pls=newpls)
			#self.saveResultToFile(pls)
			self._saveResultToWeb()

		except Exception,e:
			print 'Exception',e


	def setResult(self,urls=None,pls=None):
		''' '''
		urls = self.urls if urls==None else urls
		pls = self.pls if pls==None else pls

		for eachpl in pls:
			for urlip in urls.keys():
				if eachpl.services.has_key('ip'):
					plip = eachpl.services['ip']
					if urlip == plip:
						self.result[urlip] = {}
						self.result[urlip]['retinfo'] = eachpl.retinfo
						break

		for eachpl in pls:
			for urlip in urls.keys():
				for urlurl in urls[urlip]:
					if eachpl.services.has_key('url'):
						plurl = eachpl.services['url']
						if urlurl == plurl:
							self.result[urlip][urlurl] = {}
							self.result[urlip][urlurl]['retinfo'] = eachpl.retinfo

		pprint(self.result)

	def _noticeStartToWeb(self):
		''' '''
		print '>>>notice server start scan'
		if self.web_interface == None:
			print'server not exists'
			return False
		#	save Scan table at first
		print 'self.url\t',self.host
		self.web_interface.task_start(self.host,self.url)
			
	def _initGlobalVar(self):
		# process information
		pid = os.getpid()
		globalVar.scan_task_dict_lock.acquire()
		globalVar.scan_task_dict['pid'] = pid
		globalVar.scan_task_dict['target'] = self.url
		globalVar.scan_task_dict['server'] = self.web_interface.server
		globalVar.scan_task_dict['session'] = self.web_interface.phpsession
		globalVar.scan_task_dict['subtargets'] = {}
		globalVar.scan_task_dict['scanID'] = self.web_interface.id
		globalVar.scan_task_dict_lock.release()

	def _saveResultToWeb(self):
		print '>>>saving scan result to server'
		if self.web_interface == None:
			print'server not exists'
			return False
		else:
			self.web_interface.task_end()

	def _saveResultToWebOld(self,pls=None):
		''' '''
		print '>>>saving scan result to server'
		if self.web_interface == None:
			print'server not exists'
			return False
		#	save each url's vuln
		pls = self.pls if pls==None else pls
		for eachpl in pls:
			ipurl=None
			if eachpl.services.has_key('ip'):
				ipurl = eachpl.services['ip']
			elif eachpl.services.has_key('url'):
				ipurl = eachpl.services['url']
			retinfo =eachpl.retinfo
			print 'ipurl\t',ipurl
			pprint(retinfo)
			self.web_interface.task_end(ipurl,retinfo)


	def saveResultToFile(self,pls,outputpath=None):
		''' '''
		print '>>>saving scan result to file'
		if outputpath == None:
			outputpath = BASEDIR + '/output/' + self.host
		if os.path.isdir(outputpath) == False:
			# maybe should use os.makedirs
			os.makedirs(outputpath)

		for eachpl in pls:
			tmp =''
			if eachpl.services.has_key('ip'):
				threadName = eachpl.services['ip']
				eachfile = outputpath + '/' + threadName
				tmp += '*'*25 + '     scan info     '+ '*'*25 + os.linesep
				tmp += '# this is an ip type scan'  + os.linesep
				tmp += 'ip:\t' + threadName + os.linesep
				if eachpl.services.has_key('issubdomain'):
					tmp +='issubdomain:\t' + 'True' + os.linesep
				else:
					tmp +='issubdomain:\t' + 'False' + os.linesep

			elif eachpl.services.has_key('url'):
				threadName = eachpl.services['url']
				tmpurl = threadName.replace('://','_')
				tmpurl = tmpurl.replace(':','_')
				tmpurl = tmpurl.replace('/','')
				eachfile = outputpath + '/' + tmpurl
				tmp += '*'*25 + '     scan info     '+ '*'*25 + os.linesep
				tmp += '# this is a http type scan' + os.linesep
				tmp += 'url:\t' + threadName + os.linesep
				if eachpl.services.has_key('isneighborhost'):
					tmp +='isneighborhost:\t' + 'True' + os.linesep
				else:
					tmp +='isneighborhost:\t' + 'False' + os.linesep

			tmp += '*'*25 + '    scan output    '+ '*'*25 + os.linesep
			tmp += eachpl.output + os.linesep
			tmp += '*'*25 + ' scan services '+ '*'*25 + os.linesep
			tmp += str(eachpl.services) + os.linesep
			tmp += '*'*25 + '    scan result    '+ '*'*25 + os.linesep
			tmp += str(eachpl.retinfo) + os.linesep

			fp = open(eachfile,'w')
			fp.write(tmp)
			fp.close()

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	# server = '0xff.sinaapp.com/web/'
	server = 'www.hammer.org'
	phpsession = '1i7lf33p0ubee4i9lnui0gbk00'

	url = 'http://www.leesec.com'
	if len(sys.argv) ==  2:
		url = sys.argv[1]

	sn =Scanner(url,server,phpsession)
	sn.startScan()
	# print ">>>scan result:"
	#print sn.result
