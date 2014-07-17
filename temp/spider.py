#!/usr/bin/python2.7
#coding:utf-8

import os
import sys
#sys.path.append('/Users/mody/study/Python/Hammer')
#sys.path.append('/Users/mody/study/Python/Hammer/lib')
from lib.spider.spider import Spider,Strategy,UrlObj
from lib.dummy import BASEDIR

info = {
	'NAME':'Web Spider',
	'AUTHOR':'yangbh',
	'TIME':'20140717',
	'WEB':'',
	'DESCRIPTION':'crawl a website and save urls into cache dir'
}

def Audit(services,output=''):
	if services.has_key('url'):

	 	root = services['url']
		strategy = Strategy(max_depth=3, max_count=5000,
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
	services={'url':'http://www.hengtiansoft.com'}
	Audit(services)