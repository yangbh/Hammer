#!/usr/bin/python2.7
#coding:utf-8

from dummy import *

info = {
	'NAME':'SQL Injection Vulnerability',
	'AUTHOR':'yangbh',
	'TIME':'20141216',
	'WEB':'https://github.com/stamparm/DSXS',
	'DESCRIPTION':'sql 注入检测',
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
	['timeout',600,'pulgin run max time'],	
]


def getCrawlerHrefs(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		urls = cf.getSection('Hrefs')
		return urls
	except Exception,e:
		# print 'Exception:\t',e
		logger('Exception:\t'+str(e))
		return [url]

def Assign(services):
	if services.has_key('url') and not services.has_key('cms'):
		return True
	return False

def Audit(services):
	url = services['url']
	hrefs = getCrawlerHrefs(url)
	# pprint(hrefs)
	ds = MultiDSSS()
	for href in hrefs:
		if '=' in href:
			ds.addUrl(href)
	# pprint(ds.targets)
	ds.multiScan()
	# pprint(ds.results)
	for result in ds.results:
		if result[2]:
			security_hole(result[0])
			logger('find sql injection, %s\t' % result[0])
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url='http://testphp.vulnweb.com'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	Audit(services)
	pprint(services)