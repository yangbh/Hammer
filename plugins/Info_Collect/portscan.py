#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
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
			url = 'http://' + ip + ':' + str(eachport)
			tmpurls.append(url)
			url = 'https://' + ip + ':' + str(eachport)
			tmpurls.append(url)
	# print 'tmpurls:\t',tmpurls
	logger('tmpurls:\t'+str(tmpurls))

	for url in tmpurls:
		try:
			# print 'url=',url
			logger('url=%s ' % url)
			respone = urllib2.urlopen(url,timeout=10)
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
	# print 'urls:\t',urls
	logger('urls:\t'+str(urls))

	return urls

def Assign(services):
	if services.has_key('ip'):
		return True
	return False

def Audit(services):
	logger('services=%s' % services)
	# logger('you are success')
	# logger.debug('logger test plugin run')
	ip = services['ip']
	np = NmapScanner(ip)
	sc = np.scanPorts()
	#print sc
	try:
		services['ip'] = sc.keys()[0]
		services['ports'] = []
		services['port_detail'] = {}
		if sc[sc.keys()[0]].has_key('tcp'):
			services['port_detail'].update(sc[sc.keys()[0]]['tcp'])
			for eachport in sc[sc.keys()[0]]['tcp']:
				services['ports'].append(eachport)
		if sc[sc.keys()[0]].has_key('udp'):
			services['port_detail'].update(sc[sc.keys()[0]]['udp'])
			for eachport in sc[sc.keys()[0]]['udp']:
				services['ports'].append(eachport)

		logger('services:%s' %services)
		if services.has_key('nogather') and services['nogather'] == True:
			pass
		else:
			security_note(str(services['ports']))

			# add sub task
			if services.has_key('mode') and services['mode']=='nogather':
				pass
			else:
				urls = generateUrl(ip,services['port_detail'])
				for url in urls:
					add_scan_task(url)

	# except IndexError,e:
	except KeyError,e:
		logger('KeyError:%s' % str(e))
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	ip='172.16.3.5'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services={'ip':ip}
	print Audit(services)
	pprint(services)