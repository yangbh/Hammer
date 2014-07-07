#!/usr/bin/python2.7
#coding:utf-8

from lib.whatWeb_class import WhatWeb

info = [
		['NAME','whatweb cms recongnise'],
		['AUTHOR','yangbh'],
		['TIME','20140707'],
		['WEB','']
		]
		
def Scan(services):
	if services.has_key('host'):
		try:
			host = services['host']
			wb = WhatWeb(host)
			wb.scan()
			wb.getResult()
		#except urllib2.HTTPError,e:
		except TypeError, e:
			pass