#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

info = {
	'NAME':'Web Spider',
	'AUTHOR':'yangbh',
	'TIME':'20140717',
	'WEB':'',
	'DESCRIPTION':'crawl a website and save urls into cache dir'
}

def Audit(services):
	if services.has_key('url') and False:

	 	root = services['url']
		strategy = Strategy(max_depth=10, max_count=5000,
							same_host=True, same_domain=True)
		spider = Spider(strategy)
		spider.setRootUrl(root)
	 	spider.run()
	 	urls = spider.urltable.urls
	 	
	 	cachefilename = root.replace('://','_')
	 	cachefilename = cachefilename.replace(':','_')
	 	cachefilename = cachefilename.replace('/','_')
	 	cachefilename += '.txt'
	 	cachefile = BASEDIR + '/cache/spider/' +cachefilename
	 	
	 	fp = open(cachefile,'w')
	 	for eachurl in urls:
	 		tp = eachurl.url + os.linesep
	 		fp.write(tp)

	 	fp.close()

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	from dummy import *
	services={'url':'http://www.hengtiansoft.com'}
	pprint(Audit(services))
	pprint(services)