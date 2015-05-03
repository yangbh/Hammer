#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
import requests
import socket
from dummy import *

info = {
	'NAME':'Sub-Domain Scanning',
	'AUTHOR':'yangbh',
	'TIME':'20140709',
	'WEB':'',
	'DESCRIPTION':'子域名扫描',
	'VERSION':'1.0',
	'RUNLEVEL':0
}
opts = [
	['host','kangbtall.com','target host'],
	['timeout',600,'pulgin run max time'],
]

def generateUrl(hosts=[]):
	''''''
	# url redict  hasn't been considered
	urls = []
	# step 1: check https type
	tmpurls = []

	for eachhost in hosts:
		httpurl = 'http://' + eachhost
		tmpurls.append(httpurl)
	logger('http type tmpurls:\t'+str(tmpurls))
	
	for httpurl in tmpurls:
		flag = True
		try:
			# print 'url=',url
			logger('httpurl=%s ' % httpurl)
			httprq = requests.get(httpurl,timeout=20,allow_redirects=True)
			flag = False
			if httprq.status_code == 200 and httpurl in httprq.url:
				urls.append(httpurl)
				httpsurl = httpurl.replace('http://','https://')
				logger('httpsurl=%s ' % httpsurl)
				httpsrq = requests.get(httpsurl,timeout=20,allow_redirects=True,verify=False)
				if httpsrq.status_code == 200 and httpsurl in httpsrq.url:
					if httprq.text != httpsrq.text:
						urls.append(httpsurl)
			else:
				flag = True
		except (requests.exceptions.RequestException) as e:
			logger(str(e))

		if flag:
			try:
				httpsurl = httpurl.replace('http://','https://')
				logger('httpsurl=%s ' % httpsurl)
				httpsrq = requests.get(httpsurl,timeout=20,allow_redirects=True,verify=False)
				if httpsrq.status_code == 200 and httpsurl in httpsrq.url:
					urls.append(httpsurl)
			except (requests.exceptions.RequestException) as e:
				logger(str(e))

	logger('urls:\t'+str(urls))

	return urls

def Assign(services):
	if services.has_key('host'):
		return True
	return False

def Audit(services):
	retinfo = {}
	output = 'plugin run' + os.linesep
	subdomains = []

	# step1: get host domain
	domain = GetFirstLevelDomain(services['host'])
	
	# step2: get subdomains by knock
	if False:
		sb=SubDomain(domain)
		if 	sb.CheckForWildcard(sb.host) != False:
			pass

		sb.checkzone(sb.host)
		sb.subscan(sb.host,sb.wordlist)
		for eachdomain in sb.found:
			subdomains.append(eachdomain[1])
	
	# step3: get subdomains by bing
	# 
	
	# step4: get subdomains by baidu
	# 
	if True:
		try:
			th = TheHarvester(None)
			# print 'domain=\t',domain
			logger('domain=\t'+domain)
			tmp = th.getSubDomains(domain,'baidu',2)
			# print 'result=\t',tmp
			logger('result=\t'+str(tmp))
			try:
				for eachdomain in tmp:
					socket.gethostbyname(eachdomain)
					subdomains.append(eachdomain)
			except:
				pass
			# print 'subdomains=\t',subdomains
			
		except:
			pass
	# step5: get subdomains by google
	# 
	
	# step6: get subdomains by sitedossier
	# 
	
	# step : combine subdomains
	
	tmp = list(set(subdomains))
	subdomains = tmp

	logger('subdomains=\t'+str(subdomains))

	ret = subdomains
	retinfo = {'level':'info','content':ret}
	# security_note(str(subdomains))
	for each_domian in subdomains:
		security_note(each_domian)

	if services['host'] not in subdomains:
		subdomains.append(services['host'])
	services['subdomains'] = subdomains

	# add sub scan task
	if services.has_key('nogather') and services['nogather'] == True:
		pass
	else:
		urls = generateUrl(subdomains)
		for url in urls:
			add_target(url)

	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	host = 'kangbtall.com'
	if len(sys.argv) ==  2:
		host = sys.argv[1]
	services = {'host':host,'nogather':False}
	pprint(Audit(services))
	pprint(services)