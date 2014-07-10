#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import os
import hashlib
import json
CURRENT_PATH=os.path.dirname(__file__)
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class WhatWeb(object):
	"""WhatWeb class"""
	def __init__(self, url,outfile=''):
		super(WhatWeb, self).__init__()
		self.url = url
		if outfile:
			self.outfile = outfile
		else:
			self.outfile = CURRENT_PATH + '/' + '../cache/whatweb/' + hashlib.md5(url).hexdigest() + '.json'

	def scan(self):
		'''start whatweb scan'''
		url = self.url
		outfile = self.outfile
		shellcmd = CURRENT_PATH + '/' + './WhatWeb/whatweb -q --log-json=' +outfile +' '+url
		#print 'shellcmd=',shellcmd
		if os.path.isfile(outfile):
			os.remove(outfile)
		os.system(shellcmd)

	def getResult(self,format='dict'):
		''' '''
		try:
			fp = open(self.outfile,'r')
			
			if format == 'str':
				cont = fp.read()
				linesep_len = len(os.linesep)
				cont = cont[:-lensep_len]
				ret = cont
			elif format == 'dict':
				ret = json.load(fp)
			else:
				ret = FALSE

			fp.close()
		except TypeError,e:
			print 'TypeError',e

		return ret
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	leesec = WhatWeb('www.leesec.com')
	leesec.scan()
	print leesec.getResult()