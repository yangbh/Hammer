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
			tmp = self.url.replace('://','_')
			tmp = tmp.replace(':','_')
			tmp = tmp.replace('/','')
			self.outfile = CURRENT_PATH + '/' + '../cache/whatweb/' + tmp + '.json'
			#self.outfile = CURRENT_PATH + '/' + '../cache/whatweb/' + hashlib.md5(url).hexdigest() + '.json'

	def scan(self):
		'''start whatweb scan'''
		url = self.url
		outfile = self.outfile
		# 改为--follow-redirect = same-site，而非never
		shellcmd = CURRENT_PATH + '/' + './whatweb/whatweb -q --follow-redirect=same-site --log-json=' +outfile +' '+url
		#shellcmd = 'whatweb -q --follow-redirect=never --log-json=' +outfile +' '+url
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
				# 结果在倒数第二行
				result = ''
				for eachline in fp:
					if eachline and eachline not in ('','\n','{}\n'):
						result = eachline 
				ret = json.loads(result)
			else:
				ret = False

			fp.close()
		except TypeError,e:
			print 'TypeError',e

		return ret
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	import sys
	from pprint import pprint
	url='http://www.sel.zju.edu.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	wb = WhatWeb(url)
	wb.scan()
	pprint(wb.getResult())