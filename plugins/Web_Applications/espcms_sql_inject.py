#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Espcms SQL Injection',
	'AUTHOR':'seay,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':'Via: http://www.cnseay.com/archives/2383'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Espcms':
			output += 'plugin run' + os.linesep
			url = services['url'] + '/index.php?ac=search&at=taglist&tagkey=a%2527'
			try:
				rqu = requests.get(url)
				if rqu.status_code == 200 and rqu.text.find('ESPCMS SQL Error:') != -1:
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