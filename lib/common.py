#!/usr/bin/python2.7
#coding:utf-8

from urlparse import urlparse

def genFilename(url):
	ulp = urlparse(url)
	name = ulp.scheme + '_' + ulp.netloc.replace(':','_')
	return name
