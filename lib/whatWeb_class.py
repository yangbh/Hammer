#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import os
import hashlib

class WhatWeb(object):
	"""WhatWeb class"""
	def __init__(self, url,outfile=''):
		super(WhatWeb, self).__init__()
		self.url = url
		if outfile:
			self.outfile = outfile
		else:
			self.outfile = '../cache/whatweb/' + hashlib.md5(url).hexdigest() + '.json'

	def  scan(self):
		'''start whatweb scan'''
		url = self.url
		outfile = self.outfile
		shellcmd='./WhatWeb/whatweb -q --log-json=' +outfile +' '+url
		print 'shellcmd=',shellcmd
		if os.path.isfile(outfile):
			os.remove(outfile)
		os.system(shellcmd)