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

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'PhpMyAdmin':
			output += 'plugin run' + os.linesep
			url = services['url'] + '/main.php'
			try:
				rqu = requests.get(url)
				if rqu.status_code == 200 and rqu.text.find('MySQL client version') != -1 and rqu.text.find('root@localhost') != -1:
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