#!/usr/bin/python2.7
#coding:utf-8

from lib.whatWeb_class import WhatWeb

info = {
	'NAME':'Web Application Recognition',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
}

def Audit(services):
	if services.has_key('host'):
		try:
			host = services['host']
			wb = WhatWeb(host)
			wb.scan()
			ret = wb.getResult()
			#print ret
			retinfo = {'level':'info','content':ret}
			
			if ret.has_key('plugins'):
				# wordpress
				if ret['plugins'].has_key('WordPress'):
					services['cms'] = 'WordPress'
					services['cmsversion'] = ret['plugins']['WordPress']['version']
					print 'services changed:\t', services
				
			elif False:
				pass
			
			return retinfo

		#except urllib2.HTTPError,e:
		except TypeError, e:
			pass