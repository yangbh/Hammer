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
	# print locals()
	# print globals()
	retinfo = {}
	output = 'plugin run' + os.linesep
	# print 'logger=',logger
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

		#print 'services:\t',services
		#output += 'services:\t' + str(services) + os.linesep
		retinfo = {'level':'info','content':str(services['ports'])}
		# print 'calling secruity_note-----------------'
		if services.has_key('noSubprocess') and services['noSubprocess'] == True:
			pass
		else:
			security_note(str(services['ports']))

			# add sub task
			urls = generateUrl(ip,services['port_detail'])
			for url in urls:
				add_scan_task(url)

		#print services

	# except IndexError,e:
	# 	print 'IndexError:',e
	# 	output += 'IndexError: ' + str(e) + os.linesep
	except KeyError,e:
		print 'KeyError:',e
		# output += 'KeyError: ' + str(e) + os.linesep

	return (retinfo,output)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services={'ip':'87.230.29.167'}
	print Audit(services)
	pprint(services)