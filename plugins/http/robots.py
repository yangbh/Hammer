#!/usr/bin/python2.7
#coding:utf-8
#
import urllib2

"""docstring for robots"""
info = [
		['NAME','robots.txt file check'],
		['AUTHOR','yangbh'],
		['TIME','20140701'],
		['WEB','']
		]
		
def Audit(services):
		if services.has_key('url'):
			try:
				url = services['url'] + 'robots.txt'
				#print url
				ret = urllib2.urlopen(url).read()
				retinfo = {'host':services['host'],'type':'robots.txt info','level':'info','url':url,'content':ret}
				
				return retinfo
			#except urllib2.HTTPError,e:
			except TypeError, e:
				pass
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	rb = Robots()
	rb.run(services)