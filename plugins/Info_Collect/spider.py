#!/usr/bin/python2.7
#coding:utf-8
import sys
sys.path.append('/root/workspace/Hammer')
from lib.spider.spider import Spider,Strategy,UrlObj

def Audit(services,output=''):
	if services.has_key('url'):

	 	root = services['url']
		strategy = Strategy(max_depth=3, max_count=5000,
	                    		same_host=True, same_domain=True)
		spider = Spider(strategy)
		spider.setRootUrl(root)
	 	spider.run()
	 	print spider.dump()
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__': 
	services={'url':'www.hengtiansoft.com'}
	Audit(services)