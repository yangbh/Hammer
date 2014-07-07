#!/usr/bin/python2.7
#coding:utf-8

from lib.whatWeb_class import WhatWeb

info = [
		['NAME','whatweb cms recongnise'],
		['AUTHOR','yangbh'],
		['TIME','20140707'],
		['WEB','']
		]
		
def Audit(services):
	if services.has_key('host'):
		try:
			host = services['host']
			wb = WhatWeb(host)
			wb.scan()
			ret = wb.getResult()
			print ret
			retinfo = {'host':services['host'],'type':'whatweb info','level':'info','url':'','content':ret}
			
			if ret.has_key('plugins'):
				if ret['plugins'].has_key('WordPress'):
					print True
					services['cms'] = 'WordPress'
					services['cmsversion'] = ret['plugins']['WordPress']['version']
					print 'services changed:\t', services
			
			return retinfo

		#except urllib2.HTTPError,e:
		except TypeError, e:
			pass