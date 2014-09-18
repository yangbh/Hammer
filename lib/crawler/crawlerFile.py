#!/usr/bin/python2.7
#coding:utf-8

import os
import traceback

from dummy import BASEDIR
from lib.common import genFilename

class CrawlerFile(object):
	"""docstring for CrawlerFile"""
	def __init__(self,filename='',url=None):
		super(CrawlerFile, self).__init__()
		self.file = filename
		self.url = url
		if url:
			self.file = BASEDIR + '/cache/crawler/' + genFilename(url) + '.txt'

	def getSection(self,sectionname):
		try:
			fp = open(self.file,'r')
			flag = False
			ret = []
			for eachline in fp:
				eachline = eachline.replace('\r','')
  				eachline = eachline.replace('\n','')
				if eachline == '':
					continue

				if eachline == '['+sectionname+']':
					#print eachline
					flag = True
					continue
				if flag:
					if eachline[0] == '[':
						break
					ret.append(eachline)
			fp.close()
			return ret

		except Exception,e:
			print 'Exception:\t',e
			# print traceback.format_exc()
		return [self.url]

	def saveSection(self,sectionname,contentlist,coverfile=False):
		try:
			if coverfile:
				fp = open(self.file,'w')
			else:
				fp = open(self.file,'a')

			fp.write(os.linesep+'['+sectionname+']'+os.linesep)
			for eachline in contentlist:
				#print eachline
				fp.write(eachline+os.linesep)
			fp.close()
			return True
		except Exception,e:
			print 'Exception:\t',e
			# print traceback.format_exc()
		return False
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	url='http://www.eguan.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	cf = CrawlerFile(url=url)