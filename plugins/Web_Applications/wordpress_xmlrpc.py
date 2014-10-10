#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Wordpress Xmlrpc.php Crack And DDOS Vulnerability',
	'AUTHOR':'yangbh',
	'TIME':'20140908',
	'WEB':'http://sebug.net/vuldb/ssvid-87183',
	'DESCRIPTION':''
}

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'PhpMyAdmin':
			output += 'plugin run' + os.linesep
			url = services['url'] + '/xmlrpc.php'
			try:
				rqu = requests.get(url)
				if rqu.status_code == 200 and rqu.text == 'XML-RPC server accepts POST requests only.':
					retinfo = {'level':'low','content':url}
					output += 'Vula:\t' + url
					security_note(url)
			except:
				pass
	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)