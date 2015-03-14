#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import time
import random
import requests

from pprint import pprint
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
#works only for xroxy.com
#url I use http://www.xroxy.com/proxylist.php?port=Standard&type=All_http&ssl=&country=&latency=1000&reliability=9000#table
#but feel free to use other parameters

class ProxyScraper:
	def __init__(self):
		self.proxylist_url = 'http://www.xroxy.com/proxylist.php?port=Standard&type=All_http&ssl=&country=&latency=1000&reliability=7500&sort=reliability&desc=true'
		self.proxies = []

	def scrap_proxies(self):
		headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
		url = self.proxylist_url+('&pnum=0')
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
			url = self.proxylist_url+('&pnum=%d' % x)
			print url
			r = requests.get(url, headers=headers)
			self.parse_document(r.content)

	def parse_document(self, xml):
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
		'''return mico seconds '''
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
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class AutoProxyRequests(object):
	"""docstring for AutoProxyRequests"""
	def __init__(self, proxies=[], **kwargs):
		super(AutoProxyRequests, self).__init__()
		self.proxies = proxies
		self.proxies_http = []
		self.proxies_https = []
		for proxy in self.proxies:
			if proxy.startswith('http://'):
				self.proxies_http.append(proxy)
			elif proxy.startswith('https://'):
				self.proxies_https.append(proxy)
			else:
				print 'unknow type proxy',proxy

	def rand_proxy(self,type='all'):
		if type == 'all' and len(self.proxies):
			return self.proxies[random.randint(0,len(self.proxies))]
		elif type == 'http' and len(self.proxies_http):
			return self.proxies_http[random.randint(0,len(self.proxies_http))]
		elif type == 'https' and len(self.proxies_https):
			return self.proxies_https[random.randint(0,len(self.proxies_https))]
		else:
			print 'unknow type or proxies pool is empty'

	def head(self, url, **kwargs):
		proxy = None
		if url.startswith('https://'):
			porxy = self.rand_proxy('https')
		elif url.startswith('http://'):
			porxy = self.rand_proxy('all')
		else:
			print 'unknow type of url'
		return requests.head(url,proxies=proxy,**kwargs)

	def options(self, url, **kwargs):
		proxy = None
		if url.startswith('https://'):
			porxy = self.rand_proxy('https')
		elif url.startswith('http://'):
			porxy = self.rand_proxy('all')
		else:
			print 'unknow type of url'
		return requests.options(url,proxies=proxy,**kwargs)

	def get(self, url, **kwargs):
		proxy = None
		if url.startswith('https://'):
			porxy = self.rand_proxy('https')
		elif url.startswith('http://'):
			porxy = self.rand_proxy('all')
		else:
			print 'unknow type of url'
		return requests.get(url,proxies=proxy,**kwargs)

	def post(self, url, **kwargs):
		proxy = None
		if url.startswith('https://'):
			porxy = self.rand_proxy('https')
		elif url.startswith('http://'):
			porxy = self.rand_proxy('all')
		else:
			print 'unknow type of url'
		return requests.post(url,proxies=proxy,**kwargs)

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	# apr = AutoProxyRequests()
	# a = apr.get('http://www.baidu.com')
	# print a.text
	ps = ProxyScraper()
	ps.scrap_proxies()
	ps.check_proxies()