#!/usr/bin/python2.7
#coding:utf-8

# ----------------------------------------------------------------------------------------------------
# filename: crawler.py
# func: 主要模块，爬虫的具体实现。
# author: lvyaojia
# web: https://github.com/lvyaojia/crawler
# modifed by mody at 2014-07-23
# ----------------------------------------------------------------------------------------------------

import re
import traceback
import logging
import time

from urlparse import urljoin,urlparse
from collections import deque
from locale import getdefaultlocale
try:
	from bs4 import BeautifulSoup 
except:
	from  BeautifulSoup import BeautifulSoup

from database import Database
from webPage import WebPage
from threadPool import ThreadPool

log = logging.getLogger('Main.crawler')
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class Strategy(object):
	default_cookies = {}
	default_headers = {
		'User-Agent': 'SinaSec Webscan Spider',
		'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Cache-Control': 'max-age=0',
		'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
	}

	def __init__(self,max_depth=5,max_count=5000,concurrency=5,timeout=10,time=6*3600,headers=None,
				 cookies=None,ssl_verify=False,same_host=False,same_domain=True,keyword=None):
		self.max_depth = max_depth
		self.max_count = max_count
		self.concurrency = concurrency
		self.timeout = timeout
		self.time = time
		self.headers = self.default_headers
		self.headers.update(headers or {})
		self.cookies = self.default_cookies
		self.cookies.update(cookies or {})
		self.ssl_verify = ssl_verify
		self.same_host = same_host
		self.same_domain = same_domain
		self.keyword =  keyword
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class Crawler(object):
	def __init__(self, args):
		self.depth = args.depth  		#指定网页深度
		self.currentDepth = 1  			#标注初始爬虫深度，从1开始
		self.keyword = args.keyword.decode(getdefaultlocale()[1]) 		#指定关键词,使用console的默认编码来解码
		
		self.database =  Database(args.dbFile)				#数据库
		self.threadPool = ThreadPool(args.threadNum)  		#线程池,指定线程数
		
		self.visitedHrefs = set()   		#已访问的链接
		self.unvisitedHrefs = deque()	#待访问的链接 
		self.unvisitedHrefs.append(args.url) 		#添加首个待访问的链接
		self.isCrawling = False		#标记爬虫是否开始执行任务
		#print 'args.url=\t',args.url

	def start(self):
		print '\nStart Crawling\n'
		if not self._isDatabaseAvaliable():
			print 'Error: Unable to open database file.\n'
		else:
			self.isCrawling = True
			self.threadPool.startThreads() 
			while self.currentDepth < self.depth+1:
				#分配任务,线程池并发下载当前深度的所有页面（该操作不阻塞）
				self._assignCurrentDepthTasks ()
				#等待当前线程池完成所有任务,当池内的所有任务完成时，即代表爬完了一个网页深度
				#self.threadPool.taskJoin()可代替以下操作，可无法Ctrl-C Interupt
				while self.threadPool.getTaskLeft():
					time.sleep(8)
				print 'Depth %d Finish. Totally visited %d links. \n' % (
					self.currentDepth, len(self.visitedHrefs))
				log.info('Depth %d Finish. Total visited Links: %d\n' % (
					self.currentDepth, len(self.visitedHrefs)))
				self.currentDepth += 1
			self.stop()

	def stop(self):
		self.isCrawling = False
		self.threadPool.stopThreads()
		self.database.close()

	def getAlreadyVisitedNum(self):
		#visitedHrefs保存已经分配给taskQueue的链接，有可能链接还在处理中。
		#因此真实的已访问链接数为visitedHrefs数减去待访问的链接数
		return len(self.visitedHrefs) - self.threadPool.getTaskLeft()

	def _assignCurrentDepthTasks(self):
		while self.unvisitedHrefs:
			url = self.unvisitedHrefs.popleft()
			print url
			#向任务队列分配任务
			self.threadPool.putTask(self._taskHandler, url) 
			#标注该链接已被访问,或即将被访问,防止重复访问相同链接
			self.visitedHrefs.add(url)  
 
	def _taskHandler(self, url):
		#先拿网页源码，再保存,两个都是高阻塞的操作，交给线程处理
		print url
		webPage = WebPage(url)
		if webPage.fetch():
			self._saveTaskResults(webPage)
			self._addUnvisitedHrefs(webPage)

	def _saveTaskResults(self, webPage):
		url, pageSource = webPage.getDatas()
		try:
			if self.keyword:
				#使用正则的不区分大小写search比使用lower()后再查找要高效率(?)
				if re.search(self.keyword, pageSource, re.I):
					self.database.saveData(url, pageSource, self.keyword) 
			else:
				self.database.saveData(url, pageSource)
		except Exception, e:
			log.error(' URL: %s ' % url + traceback.format_exc())

	def _addUnvisitedHrefs(self, webPage):
		'''添加未访问的链接。将有效的url放进UnvisitedHrefs列表'''
		#对链接进行过滤:1.只获取http或https网页;2.保证每个链接只访问一次
		url, pageSource = webPage.getDatas()
		hrefs = self._getAllHrefsFromPage(url, pageSource)
		for href in hrefs:
			if self._isHttpOrHttpsProtocol(href):
				if not self._isHrefRepeated(href):
					self.unvisitedHrefs.append(href)

	def _getAllHrefsFromPage(self, url, pageSource):
		'''解析html源码，获取页面所有链接。返回链接列表'''
		hrefs = []
		soup = BeautifulSoup(pageSource)
		results = soup.find_all('a',href=True)
		for a in results:
			#必须将链接encode为utf8, 因为中文文件链接如 http://aa.com/文件.pdf 
			#在bs4中不会被自动url编码，从而导致encodeException
			href = a.get('href').encode('utf8')
			if not href.startswith('http'):
				href = urljoin(url, href)#处理相对链接的问题
			hrefs.append(href)
		return hrefs

	def _isHttpOrHttpsProtocol(self, href):
		protocal = urlparse(href).scheme
		if protocal == 'http' or protocal == 'https':
			return True
		return False

	def _isHrefRepeated(self, href):
		if href in self.visitedHrefs or href in self.unvisitedHrefs:
			return True
		return False

	def _isDatabaseAvaliable(self):
		if self.database.isConn():
			return True
		return False

	def selfTesting(self, args):
		url = 'http://www.baidu.com/'
		print '\nVisiting www.baidu.com'
		#测试网络,能否顺利获取百度源码
		pageSource = WebPage(url).fetch()
		if pageSource == None:
			print 'Please check your network and make sure it\'s connected.\n'
		#数据库测试
		elif not self._isDatabaseAvaliable():
			print 'Please make sure you have the permission to save data: %s\n' % args.dbFile
		#保存数据
		else:
			self._saveTaskResults(url, pageSource)
			print 'Create logfile and database Successfully.'
			print 'Already save Baidu.com, Please check the database record.'
			print 'Seems No Problem!\n'
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	args
	crawler = Crawler(args)
	crawler.start()