#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'Discuz X3 uctools Default Password',
	'AUTHOR':'darkkid,wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'Discuz! X3 急诊箱,可能存在默认密码：188281MWWxjk'
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
	url = services['url'] +'/source/plugin/tools/tools.php'
	try:
		rqu =requests.get(url)
		if rqu.status_code == 200 :
			res = rqu.text 
			m = re.reserch('Discuz',res)
			if m :
				security_hole(url+'Discuz! X3 急诊箱,可能存在默认密码：188281MWWxjk')
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
