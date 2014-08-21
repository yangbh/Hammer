#!/usr/bin/python2.7
#coding:utf-8

import os
import re
from urlparse import urlparse

from dummy import * 

info = {
	'NAME':'DNS zone transfer Vulnerability',
	'AUTHOR':'yangbh',
	'TIME':'20140729',
	'WEB':'https://github.com/lijiejie/edu-dns-zone-transfer',
	'DESCRIPTION':'DNS AXFR zone transfer'
}

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url'):
		try:
			url = services['url']
			ulp = urlparse(url)
			host = ulp.netloc
			print host
			# not ip
			
			if re.search('((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))',host):
				return(None,output)
			domain = GetFirstLevelDomain(host)
			print domain

			cmd_res = os.popen('nslookup -type=ns ' + domain).read()	# fetch DNS Server List
			dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
			for server in dns_servers:
				if len(server) < 5: server += domain
				cmd_res = os.popen('dig @%s axfr %s' % (server, domain)).read()
				if cmd_res.find('Transfer failed.') < 0 and \
						cmd_res.find('connection timed out') < 0 and \
						cmd_res.find('XFR size') > 0 :

					output +=  'Vulnerable dns server found:' + server + os.linesep
					retinfo = {'level':'medium','content':domain}
		except Exception,e:
			pass
		return(retinfo,output)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url='http://www.htu.edu.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)