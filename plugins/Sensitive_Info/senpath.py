#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
import threading

from urlparse import urlparse
from dummy import *

info = {
	'NAME':'Sensitive File/Directory Discover',
	'AUTHOR':'yangbh',
	'TIME':'20140716',
	'WEB':'',
	'DESCRIPTION':'Sensitive file or directory such as: /admin, /conf, /backup /db'
}

ret = ''
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def getCrawlerPaths(url):
	''' '''
	try:
		urls = []
		filename = BASEDIR + '/cache/crawler/' + genFilename(url) + '_paths.txt'
		fp = open(filename,'r')
		for eachline in fp:
			eachline = eachline.replace(os.linesep,'')
			if eachline == '':
				continue
			urls.append(eachline)

		fp.close()
		return urls
	except Exception,e:
		print 'Exception:\t',e
		return [url]

def getCommonPaths():
	''' '''
	

def Audit(service):
	retinfo = {}
	output = ''
	if services.has_key('url'):
		output += 'plugin run' + os.linesep
		if services.has_key:
			pass

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.hengtiansoft.com'}
	pprint(Audit(services))
	pprint(services)