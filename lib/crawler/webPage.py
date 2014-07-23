#!/usr/bin/python2.7
#coding:utf-8

# ----------------------------------------------------------------------------------------------------
# filename: WebPage.py
# func: 该模块用于下载网页源代码, 允许自定义header与使用代理服务器
# author: lvyaojia
# web: https://github.com/lvyaojia/crawler
# modifed by mody at 2014-07-23
# ----------------------------------------------------------------------------------------------------

import re
import traceback
import logging
import requests

#log = logging.getLogger('WebPage')
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class WebPage(object):
	def __init__(self, url):
		self.url = url
		self.pageSource = None
		self.customeHeaders()
		print self.fetch()

	def fetch(self, retry=2, proxies=None):
		'''获取html源代码'''
		try:
			#设置了prefetch=False，当访问response.text时才下载网页内容,避免下载非html文件
			response = requests.get(self.url, headers=self.headers, timeout=10, prefetch=False, proxies=proxies)
			print url,response
			if self._isResponseAvaliable(response):
				self._handleEncoding(response)
				self.pageSource = response.text
				return True
			else:
				#log.warning('Page not avaliable. Status code:%d URL: %s \n' % (
				#	response.status_code, self.url) )
				pass
		except Exception,e:
			if retry>0: #超时重试
				return self.fetch(retry-1)
			else:
				print 'error',e
				#log.debug(str(e) + ' URL: %s \n' % self.url)
				pass
		return None

	def customeHeaders(self, **kargs):
		#自定义header,防止被禁,某些情况如豆瓣,还需制定cookies,否则被ban
		#使用参数传入可以覆盖默认值，或添加新参数，如cookies		
		self.headers = {
			'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset' : 'gb18030,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding' : 'gzip,deflate,sdch',
			'Accept-Language' : 'en-US,en;q=0.8',
			'Connection': 'keep-alive',
			#设置Host会导致TooManyRedirects, 因为hostname不会随着原url跳转而更改,可不设置
			#'Host':urlparse(self.url).hostname
			'User-Agent' : 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
			'Referer' : self.url,
		}
		self.headers.update(kargs)

	def getDatas(self):
		return self.url, self.pageSource

	def _isResponseAvaliable(self, response):
		#网页为200时再获取源码, 只选取html页面。 
		if response.status_code == requests.codes.ok:
			if 'html' in response.headers['Content-Type']:
				return True
		return False

	def _handleEncoding(self, response):
		#requests会自动处理编码问题.
		#但是当header没有指定charset并且content-type包含text时,
		#会使用RFC2616标准，指定编码为ISO-8859-1
		#因此需要用网页源码meta标签中的charset去判断编码
		if response.encoding == 'ISO-8859-1':
			charset_re = re.compile("((^|;)\s*charset\s*=)([^\"']*)", re.M)
			charset=charset_re.search(response.text) 
			charset=charset and charset.group(3) or None 
			response.encoding = charset

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()