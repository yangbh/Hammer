#!/usr/bin/python2.7
#coding:utf-8

import string
import requests
from dummy import *

info = {
	'NAME':'IIS Method Scanner',
	'AUTHOR':'yangbh',
	'TIME':'20140731',
	'WEB':'',
	'DESCRIPTION':'When iis enable PUT or MOVE method, attacker can upload a webshell'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url'):
		return True
	return False

def Audit(services):
	# print services
	if services.has_key('HTTPServer') and services['HTTPServer'].lower().find('iis') == -1:
		return
	url = services['url']
	method = None
	# first, if option method is useful
	try:
		respone = requests.options(url)
		if 'allow' in respone.headers.keys():
			method = respone.headers['allow']
		elif 'public' in respone.headers.keys():
			method = respone.headers('public')
	except Exception,e:
		# print 'Exception:\t',e
		logger('Exception:\t'+str(e))

	if method:
		method = method.upper()
		level = 'low'
		if method.find('PUT') != -1 or method.find('MOVE') != -1:
			level = 'medium'
		if 'PUT' in method:
			security_warning(method)
		else:
			security_note(method)

	# else, option method not useful
	try:
		tmethod = []
		respone = requests.put(url)
		if respone.status_code == 200:
			tmethod.append('PUT')
		respone = requests.delete(url)
		if respone.status_code == 200:
			tmethod.append('DELETE')
		method = string.join(tmethod,', ')
		if method != '':
			if 'PUT' in method:
				security_warning(method)
			else:
				security_note(method)

	except Exception,e:
		# print 'Exception:\t',e
		logger('Exception:\t'+str(e))
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	url='http://www.eguan.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url} 
	pprint(Audit(services))
	pprint(services)