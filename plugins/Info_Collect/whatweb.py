#!/usr/bin/python2.7
#coding:utf-8

import os
import re
import urllib2
from dummy import *

info = {
	'NAME':'Web Application Recognition',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':''
}

def Audit(services):
	retinfo = {}
	output = ''
	if services.has_key('url'):
		output += 'plugin run' + os.linesep
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
					output += 'cms: WordPress' + os.linesep
					if ret['plugins']['WordPress'].has_key('version'):
						services['cmsversion'] = ret['plugins']['WordPress']['version'][0]
						output += 'cmsversion: ' + services['cmsversion'] + os.linesep
				# Discuz
				elif ret['plugins'].has_key('Discuz'):
					#print services
					services['cms'] = 'Discuz'
					output += 'cms: Discuz' + os.linesep
					if ret['plugins']['Discuz'].has_key('version'):
						services['cmsversion'] = ret['plugins']['Discuz']['version'][0]
						output += 'cmsversion: ' + services['cmsversion'] + os.linesep

				# HTTPServer
				if ret['plugins'].has_key('HTTPServer'):
					if ret['plugins']['HTTPServer'].has_key('string'):
						# string key is a list, so use [0]
						services['HTTPServer'] = ret['plugins']['HTTPServer']['string'][0]
						output += 'HTTPServer: ' + services['HTTPServer'] + os.linesep

				# X-Powered-By
				if ret['plugins'].has_key('X-Powered-By'):
					if ret['plugins']['X-Powered-By'].has_key('string'):
						# string key is a list, so use [0]
						services['X-Powered-By'] = ret['plugins']['X-Powered-By']['string'][0]
						output += 'X-Powered-By: ' + services['X-Powered-By'] + os.linesep

			elif False:
				pass
			
			return (retinfo,output)

		except urllib2.URLError,e:
			#print 'urllib2.URLError: ',e
			output += 'urllib2.URLError: ' + str(e) + os.linesep
		except urllib2.HTTPError,e:
			#print 'urllib2.HTTPError: ',e
			output += 'urllib2.HTTPError: ' + str(e) + os.linesep
		except TypeError, e:
			#print 'TypeError: ',e
			output += 'TypeError: ' + str(e) + os.linesep
	# else:
	# 	output += 'plugin does not run' + os.linesep

	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	import sys
	url='http://www.htu.edu.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)