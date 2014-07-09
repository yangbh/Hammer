#!/usr/bin/python2.7
#coding:utf-8

import socket
from lib.knock_class import SubDomain

info = {
	'NAME':'Sub-Domain Scanning',
	'AUTHOR':'yangbh',
	'TIME':'20140709',
	'WEB':'',
}

def Audit(services):
	if services.has_key('host') and 'fardomain' not in services.keys():
		subdomains = []
		# step1: get host domain
		pos = services['host'].find('.')+1
		domain = services['host'][pos:]

		# step2: get subdomains by knock
		sb=SubDomain(domain)
		if 	sb.CheckForWildcard(sb.host) != False:
			sys.exit(1)

		sb.checkzone(sb.host)
		sb.subscan(sb.host,sb.wordlist)
		for eachdomain in sb.found:
			subdomains.append(eachdomain[1])
		
		# step3: get subdomains by bing
		# 
		
		# step4: get subdomains by baidu
		# 
		
		# step5: get subdomains by google
		# 
		
		# step6: get subdomains by sitedossier
		# 
		
		# step : combine subdomains
		tmp = list(set(subdomains))
		subdomains = tmp

		print subdomains
		services['subdomains'] = subdomains

