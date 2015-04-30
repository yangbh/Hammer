#!/usr/bin/python2.7
#coding:utf-8

# easier, can use easywebdav
# import easywebdav

import requests
from urlparse import urlparse
from dummy import *

info = {
	'NAME':'WebDAV Enabled',
	'AUTHOR':'yangbh',
	'TIME':'20140731',
	'WEB':'WebDAV（Web-based Distributed Authoring and Versioning）is Open',
	'DESCRIPTION':''
}
opts = [
	['url','http://WSWINCHZ0255.eguan.cn','target url'],
]

def Assign(services):
	if services.has_key('url'):
		return True
	return False

def Audit(services):
	if services.has_key('HTTPServer') and services['HTTPServer'].lower().find('iis') == -1:
		return
	url = services['url'] 
	upl = urlparse(url)

	crackflag = False
	session = requests.session()
	try:
		respone = session.request('PROPFIND',url+'/.')
		if respone.status_code == 207:
			security_warning(output)
		
		elif respone.status_code == 401:
			security_warning(output)
			crackflag = True
	except Exception,e:
		pass
# ----------------------------------------------------------------------------------------------------
#	
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	url='http://WSWINCHZ0255.eguan.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url} 
	pprint(Audit(services))
	pprint(services)