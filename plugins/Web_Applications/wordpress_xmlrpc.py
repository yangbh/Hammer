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
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Wordpress':
			return True
	return False

def Audit(services):
	url = services['url'] + '/xmlrpc.php'
	try:
		rqu = requests.get(url)
		if rqu.status_code == 200 and rqu.text == 'XML-RPC server accepts POST requests only.':
			security_note(url)
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)