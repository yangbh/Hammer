#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'PhpMyAdmin NULL Password',
	'AUTHOR':'321,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':'phpMyadmin password is empty'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'PhpMyAdmin':
			return True
	return False

def Audit(services):
	url = services['url'] + '/main.php'
	try:
		rqu = requests.get(url)
		if rqu.status_code == 200 and rqu.text.find('MySQL client version') != -1 and rqu.text.find('root@localhost') != -1:
			security_warning(url)
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)