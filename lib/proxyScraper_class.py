#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import time
import random
import requests
import futures
import json

import globalVar

from pprint import pprint
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------

class ProxyScraper:
	def __init__(self):
		self.proxies = []

	def scrap_proxies_1(self):
		#works only for xroxy.com
		#url I use http://www.xroxy.com/proxylist.php?port=Standard&type=All_http&ssl=&country=&latency=1000&reliability=9000#table
		#but feel free to use other parameters
		proxylist_url = 'http://www.xroxy.com/proxylist.php?port=Standard&type=All_http&ssl=&country=&latency=2000&reliability=7500&sort=reliability&desc=true'
		headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
		url = proxylist_url+('&pnum=0')

		print url
		r = requests.get(url, headers=headers)
		# 获取页数
		soup = BeautifulSoup(r.content)
		soup.prettify()
		numbers = int(soup.findAll('small')[-1].find('b').text)
		pages = int(numbers/10) + 1
		# pages = len(soup.findAll('small')[-2].findAll('a'))
		print 'pages=',pages
		# 解析每页
		self.parse_document(r.content)
		for x in xrange(1,pages):
			url = proxylist_url+('&pnum=%d' % x)
			print url
			r = requests.get(url, headers=headers)
			self.parse_document(r.content)

	def parse_document(self, xml):
		'''
		@xml
		'''
		soup = BeautifulSoup(xml)
		soup.prettify()

		for tr in soup.findAll('tr','row0')+soup.findAll('tr','row0'):
			# print 'tr=',tr
			a = tr.findAll('a')
			ip = a[1].text.strip('\n')
			port = a[2].text.strip('\n')
			proxy_type = a[3].text.strip('\n')
			ssl = a[4].text.strip('\n') == str('true')
			country = a[5].text.strip(u'\xa0')

			td = tr.findAll('td')
			latency = int(td[-3].text.strip('\n'))
			reliability = float(td[-2].text.strip('\n'))

			self.proxies.append((ip,port,proxy_type,ssl,country,latency,reliability))
			print ip,port,proxy_type,ssl,country,latency,reliability
	
	def getTime(self,proxyurl,basicurl='http://www.baidu.com'):
		'''return mico seconds 
		@proxyurl
		@basicurl
		'''
		if proxyurl.startswith('http://'):
			proxies = {'http':proxyurl}
		elif proxyurl.startswith('https://'):
			proxies = {'https':proxyurl}

		repeattimes = 2
		timetotal = 0
		for x in xrange(1,repeattimes+1):
			timesec = 30
			start = time.time()
			try:
				rq = requests.get(basicurl,proxies=proxies,timeout=30)
				end = time.time()
				timesec = end - start
			except IOError,e:
				print IOError,e

			timetotal += int(timesec*1000)

		timeavrage = int(timetotal/repeattimes)
		return timeavrage

	def check_proxies(self,basicurl='http://www.baidu.com',timeout=20000):
		'''
		@basicurl:
		@timeout:
		'''
		proxies_avalible = []
		for each_proxy in self.proxies:
			proxy_type = 'http' if each_proxy[3] else 'https'
			proxy_url = '%s://%s:%s' % (proxy_type,each_proxy[0],each_proxy[1])
			print 'proxy_url=',proxy_url
			timesec = self.getTime(proxy_url)
			print 'timesec=',timesec
			if timesec<timeout:
				proxies_avalible.append((each_proxy[0],each_proxy[1],each_proxy[2],each_proxy[3],each_proxy[4],timesec,each_proxy[6]))
		pprint(proxies_avalible)
		return proxies_avalible
		
	def format_proxie(self,proxies=None,type=0):
		'''
		@proxies
		@type
		'''
		if proxies == None:
			proxies = self.proxies

		if type == 0:
			return proxies
		elif type == 1:
			str_proxies = []
			for each_proxy in proxies:
				str_proxy = 'http://'
				if each_proxy[3]:
					str_proxy = 'https://'
				str_proxy += each_proxy[0] + each_proxy[1]
				str_proxies.append(str_proxy)
			return str_proxies
		else:
			return 'type error'

	def proxies_submit(self,proxies=None,server=None,token=None):
		'''
		@proxies
		@server
		@token
		'''
		if server == None:
			server = globalVar.server
		if token == None:
			token = globalVar.token
		if proxies == None:
			proxies = self.proxies

		# pprint(proxies)
		url = 'http://' + server + '/proxy_add.php'
		postdata = {'token': token, 'proxies': json.dumps(proxies)}
		# print postdata
		rq = requests.post(url,data=postdata)
		print rq.text
		if rq.status_code == 200 and 'success' in rq.text:
			print 'submit proxies success'
		else:
			print 'submit proxies failed'

	def proxies_get(self,num=1000,server=None,token=None):
		'''
		@num
		@server
		@token
		'''
		if server == None:
			server = globalVar.server
		if token == None:
			token = globalVar.token
		try:
			url = 'http://' + server + '/proxy_search.php'
			data = {'token': token,'num': num}
			rq = requests.post(url,data=data)
			if rq.status_code == 200:
				self.proxies = json.loads(rq.text)
				pprint(self.proxies)
				print 'get proxies success'
			else:
				print 'get proxies failed'
		except IndexError,e:
			print 'IndexError',e
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	server='www.hammer.org'
	token='dEc6Yof8bgWwRrD0KNDc643Pe2kspXa2'
	ps = ProxyScraper()
	# ps.scrap_proxies_1()
	# ps.check_proxies()
	# ps.proxies_submit(None,server,token)
	ps.proxies_get(1000,server,token)

