#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'Discuz Comsenz uctools',
	'AUTHOR':'真爱,wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'Comsenz 系统维护工具箱（UCenter专用版）破解登陆密码后可控制Discuz!'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Discuz':
			return True
	return False

def Audit(services):
	url = services['url'] +'/uc_server/uctools.php'
	try:
		rqu =requests.get(url)
		if rqu.status_code == 200 :
			res = rqu.text 
			m = re.reserch('Comsenz',res)
			if m :
				security_hole(url+'Comsenz 系统维护工具箱（UCenter专用版）')
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
