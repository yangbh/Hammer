#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import os
import urllib2
import re
import socket

class neiborDomain(object):
	"""docstring for neiborDomain"""
	def __init__(self, ip):
		super(neiborDomain, self).__init__()
		m = re.match('(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',ip)
		if m:
			self.ip = m.group(0)
		else:
			self.domain = ip
			self.ip = socket.gethostbyname(ip)

	def getFromBing(self, ip=None):
		if ip == None:
			ip = self.ip
		interface_url = 'http://cn.bing.com/search?count=100&q=ip:%3a'
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5"
		headers["Accept"] = "text/plain"
		url = interface_url + ip
		req = urllib2.Request(url,headers=headers)
		ret = urllib2.urlopen(req).read()
		return ret

	
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	nebordom = neiborDomain('www.leesec.com')
	print nebordom.getFromBing()