#!/usr/bin/python2.7
#coding:utf-8
#
import urllib2

info = {
	'NAME':'Robots.txt Sensitive Information',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
}

def Audit(services):
	if services.has_key('url'):
		try:
			url = services['url'] + 'robots.txt'
			#print url
			ret = urllib2.urlopen(url).read()
			retinfo = {'level':'info','content':ret}
			
			return retinfo
		#except urllib2.HTTPError,e:
		except TypeError, e:
			pass
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	pass