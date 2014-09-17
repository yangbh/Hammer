#!/usr/bin/python2.7
#coding:utf-8

import os
import socket
from dummy import *

info = {
	'NAME':'Sub-Domain Scanning',
	'AUTHOR':'yangbh',
	'TIME':'20140709',
	'WEB':''
}

def Audit(services):
	retinfo = {}
	output = ''
	# pprint(locals())
	# pprint(globals())
	if services.has_key('host') and 'issubdomain' not in services.keys():
		output += 'plugin run' + os.linesep
		subdomains = []
		# step1: get host domain
		# pos = services['host'].find('.')+1
		# domain = services['host'][pos:]
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
				print 'domain=\t',domain
				tmp = th.getSubDomains(domain,'baidu',2)
				print 'result=\t',tmp
				try:
					for eachdomain in tmp:
						socket.gethostbyname(eachdomain)
						subdomains.append(eachdomain)
				except:
					pass
				print 'subdomains=\t',subdomains
			except:
				pass
		# step5: get subdomains by google
		# 
		
		# step6: get subdomains by sitedossier
		# 
		
		# step : combine subdomains
		tmp = list(set(subdomains))
		subdomains = tmp

		ret = subdomains
		retinfo = {'level':'info','content':ret}

		if services['host'] not in subdomains:
			subdomains.append(services['host'])
		services['subdomains'] = subdomains

	# else:
	# 	output += 'plugin does not run' + os.linesep

	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'host':'www.hengtiansoft.com'}
	pprint(Audit(services))
	pprint(services)