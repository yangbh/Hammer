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
	output = ''
	# pprint(locals())
	# pprint(globals())
	if services.has_key('host') and 'issubdomain' not in services.keys():
		output += 'plugin run' + os.linesep
		subdomains = []
		# step1: get host domain
		pos = services['host'].find('.')+1
		domain = services['host'][pos:]
		print domain

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
			th = TheHarvester(None)
			print domain
			tmp = th.getSubDomains(domain,'baidu',2)
			print domain,tmp
			subdomains += tmp

		# step5: get subdomains by google
		# 
		
		# step6: get subdomains by sitedossier
		# 
		
		# step : combine subdomains
		tmp = list(set(subdomains))
		subdomains = tmp

		print subdomains
		services['subdomains'] = subdomains

	else:
		output += 'plugin does not run' + os.linesep

	return (None,output)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'host':'www.sel.zju.edu.cn'}
	pprint(Audit(services))
	pprint(services)