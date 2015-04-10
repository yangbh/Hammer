#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import random
import requests
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

	def add_proxies(self,proxies=[]):
		''' 添加代理接口'''
		for proxy in self.proxies:
			self.proxies.append(proxy)
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
	from proxyScraper_class import ProxyScraper
	# apr = AutoProxyRequests()
	# a = apr.get('http://www.baidu.com')
	# print a.text
	ps = ProxyScraper()
	ps.scrap_proxies_1()
	ps.check_proxies()