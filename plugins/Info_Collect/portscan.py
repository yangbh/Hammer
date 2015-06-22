#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
import requests
from dummy import *

info = {
	'NAME':'Port and Service Discover',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
	'DESCRIPTION':'端口扫描',
	'VERSION':'1.0',
	'RUNLEVEL':0
}
opts = {
	'ip':'176.28.50.165',	#'target ip'
	'timeout':600,			#'pulgin run max time'
	'ports':'21,22,23,25,110,53,67,80,1521,1526,3306,3389,4899,8580,873,443,465,993,995,2082,2083,2222,2601,2604,3128,3312,3311,4440,6082,6379,7001,7778,8000-9090,8080,8888,8083,8089,9200,10000,11211,11211,28017,27017',#'target ports, string type'
	'argument':'-sV ',		#'nmap port scan argument'
	'auto_add':True,
}
# opts =[
# 	['ip','176.28.50.165','target ip'],
# 	['timeout',600,'pulgin run max time'],
# 	['ports','21,22,23,25,110,53,67,80,1521,1526,3306,3389,4899,8580,873,443,465,993,995,2082,2083,2222,2601,2604,3128,3312,3311,4440,6082,6379,7001,7778,8000-9090,8080,8888,8083,8089,9200,10000,11211,11211,28017,27017','target ports, string type'],
# 	['argument','-sV ','nmap port scan argument'],
# ]
def generateUrl(ip=None,ports=None):
	''''''
	httpports = []
	for eachport in ports.keys():
		if ports[eachport]['name'] == 'http':
			httpports.append(eachport)
	# print 'httpports:\t',httpports
	logger('httpports:\t'+str(httpports))

	# url redict  hasn't been considered
	urls = []
	tmpurls = []

	if ip != None and httpports != None:
		for eachport in httpports:
			if eachport == 443:
				url = 'https://' + ip + ':' + str(eachport)
			else:
				url = 'http://' + ip + ':' + str(eachport)
			tmpurls.append(url)
	logger('tmpurls:\t'+str(tmpurls))

	for url in tmpurls:
		try:
			logger('url=%s ' % url)
			rq = requests.get(url,timeout=20,allow_redirects=True)
			if rq.status_code == 200:
				if url in rq.url:
					urls.append(url)
		except (requests.exceptions.RequestException) as e:
			logger(str(e))

	logger('urls:\t'+str(urls))

	return urls

def Assign(services):
	if services.has_key('ip'):
		return True
	return False

def Audit(services):
	logger('services=%s' % services)
	ip = services['ip']
	np = NmapScanner(hosts=ip,ports=opts['ports'],arguments=opts['argument'])
	sc = np.scanPorts()
	# logger('sc=%s' % str(sc))
	try:
		ports = []
		port_detail = {}
		if sc[sc.keys()[0]].has_key('tcp'):
			port_detail.update(sc[sc.keys()[0]]['tcp'])
			for eachport in sc[sc.keys()[0]]['tcp']:
				ports.append(eachport)
		if sc[sc.keys()[0]].has_key('udp'):
			port_detail.update(sc[sc.keys()[0]]['udp'])
			for eachport in sc[sc.keys()[0]]['udp']:
				ports.append(eachport)

		ports.sort()
		services['ports'] = ports
		services['port_detail'] = port_detail
		for eachport in ports:
			logger('eachport= %d' % eachport)
			security_note('%d: %s' % (eachport,str(port_detail[eachport])))

		logger('services:%s' %services)
		# security_note(str(services['ports']))
		if services.has_key('nogather') and services['nogather'] == True:
			pass
		else:
			# add sub task
			if services.has_key('mode') and services['mode']=='nogather':
				pass
			else:
				urls = generateUrl(ip,services['port_detail'])
				pprint(urls)
				for url in urls:
					add_target(url)

	# except IndexError,e:
	except KeyError,e:
		logger('KeyError:%s' % str(e))
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	ip='176.28.50.165'
	if len(sys.argv) ==  2:
		ip = sys.argv[1]
	services={'ip':ip}
	print Audit(services)
	pprint(services)