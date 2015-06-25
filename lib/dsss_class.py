#!/usr/bin/python2.7
#coding:utf-8

from concurrent import futures
from pprint import pprint
from DSSS.dsss import init_options,scan_page

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class MultiDSSS(object):
	"""DSSS 的多线程版本"""
	def __init__(self,cookie=None,useragent=None,referer=None,proxy=None,threads=10):
		super(MultiDSSS, self).__init__()
		self.cookie = cookie
		self.useragent = useragent if useragent else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"
		self.referer = referer 
		self.proxy = proxy
		self.threads = threads

		self.targets = [] 
		self.results = []

		init_options(self.proxy, self.cookie, self.useragent, self.referer)

	def addUrl(self,url='',data=None):
		self.targets.append((url if url.startswith("http") else "http://%s" % url ,data))

	def scan(self,target):
		return scan_page(target[0],target[1])

	def multiScan(self):
		with futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
			future_to_url = dict((executor.submit(self.scan, target), target) for target in self.targets)
			for future in futures.as_completed(future_to_url):
				target = future_to_url[future]
				try:
					ret = future.result()
				except Exception as exc:
					print('%r generated an exception: %s' % (target, exc))
					# logger('%r generated an exception: %s' % (url, exc))
				else:
					print('%r returns: %s' % (target, str(ret)))
					self.results.append((target[0],target[1],ret))
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	ds = MultiDSSS()
	ds.addUrl('http://www.hrsd.zju.edu.cn/news_info.php?s_id=94')
	ds.addUrl('http://www.cst.zju.edu.cn/index.php?c=Index&a=detail&catid=72&id=2432')
	ds.addUrl('http://www.cps.zju.edu.cn/index.php?c=index&a=detail&id=11047&web=chinese')
	ds.addUrl('http://www.hrsd.zju.edu.cn/news_info.php?s_id=0')
	ds.multiScan()
	pprint(ds.result)