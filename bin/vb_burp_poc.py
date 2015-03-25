#!/usr/bin/python2.7
#coding:utf-8

import sys
import time
import requests
import futures
import threading

# 把字符串转成时间戳  
def string_toIntTime(string):  
	return time.mktime(time.strptime(string, "%Y-%m-%d %H:%M:%S"))

# 生成图片基础路径
def genPicPath(itm):
	basicurl = 'http://i.3001.net/images/'
	tpa = time.strftime('%Y%m%d',time.localtime(itm))
	basicurl += tpa
	return basicurl

def burpPath(url):
	for i in range(5):
		try:
			a = requests.get(url)
			
			if a.status_code == 200:
				print url,'success'
				return 'success'
			else:
				print url,'fail'
				return 'fail'
			break
		# exceptions cased by multi threads
		except IndexError,e:
			# print 'IndexError',e
			pass


def main():
	tm = '2014-10-21 10:14:00'
	if len(sys.argv) ==  2:
		tm = sys.argv[1]
	itm = string_toIntTime(tm)
	print '时间戳：',itm

	basicurl = genPicPath(itm)
	ttm = int(itm) * 10000
	
	# fs = {}
	with futures.ThreadPoolExecutor(max_workers=100) as executor:      #默认10线程
		time.clock()
		for i in xrange(2000000):
			url = basicurl + '/' + str(ttm - i) + '.jpg'
			# print 'starting\t',eachname+':'+eachpwd
			future = executor.submit(burpPath,url)
			# fs[future] = url
			# print eachname+':'+eachpwd +' '+str(f.result())
		print time.clock()

	print time.clock()
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()