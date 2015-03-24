#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Wordpress Reflect XSS',
	'AUTHOR':'owlinrye,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':'CVE-2012-3414'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Wordpress':
			return True
	return False

def Audit(services):
	url = services['url'] + '/wp-includes/js/swfupload/swfupload.swf'
	try:
		rqu = requests.get(url)
		if rqu.status_code == 200 and validate(rqu.text):
			security_note(url)
	except:
		pass

def validate(res):
	val_hash = '3a1c6cc728dddc258091a601f28a9c12'
	res_md5 = md5.new(res)
	if val_hash == res_md5.hexdigest():
		return True
	else: 
		return False
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)