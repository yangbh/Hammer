#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2

info = {
	'NAME':'Robots.txt Sensitive Information',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
}

def Audit(services,output=''):
	if services.has_key('url'):
		try:
			url = services['url']
			if url[-1]!='/':
				url += '/'
			url = url + 'robots.txt'
			#print url
			output += url + os.linesep
			
			respone = urllib2.urlopen(url)
			redirected = respone.geturl()
			if redirected == url:
				ret = respone.read()
				if 'Disallow: ' in ret:
					retinfo = {'level':'info','content':ret}
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
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	pass