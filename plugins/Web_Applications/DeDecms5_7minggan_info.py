#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'DeDeCms 敏感信息泄露',
	'AUTHOR':'seay,wjk',
	'TIME':'20150323',
	'WEB':'',
	'DESCRIPTION':'dedecms 敏感信息泄露'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'DedeCms':
			return True
	return False

def Audit(services):
	url = services['url'] +'/data/mysqli_error_trace.inc'
	try:
		rqu = requests.get(url)
		if rqu.status_code == 200:
			security_hole('dedecms error info:' + url + '/data/mysqli_error_trace.inc')
	except:
		pass

# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
