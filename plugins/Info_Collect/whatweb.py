#!/usr/bin/python2.7
#coding:utf-8

import os
import re
import urllib2
from lib.whatWeb_class import WhatWeb


info = {
	'NAME':'Web Application Recognition',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
}

def Audit(services,output=''):
	if services.has_key('url'):
		try:
			url = services['url']
			wb = WhatWeb(url)
			wb.scan()
			ret = wb.getResult()
			#print ret
			retinfo = {'level':'info','content':ret}
			
			if ret.has_key('plugins'):
				# wordpress
				if ret['plugins'].has_key('WordPress'):
					#print services
					services['cms'] = 'WordPress'
					if ret['plugins']['WordPress'].has_key('version'):
						services['cmsversion'] = ret['plugins']['WordPress']['version']
					
			elif False:
				pass
			
			return retinfo

		except urllib2.URLError,e:
			#print 'urllib2.URLError: ',e
			output += 'urllib2.URLError: ' + str(e) + os.linesep
		except urllib2.HTTPError,e:
			#print 'urllib2.HTTPError: ',e
			output += 'urllib2.HTTPError: ' + str(e) + os.linesep
		except TypeError, e:
			#print 'TypeError: ',e
			output += 'TypeError: ' + str(e) + os.linesep