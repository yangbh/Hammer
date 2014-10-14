#!/usr/bin/python2.7
#coding:utf-8
'''
Time: 2014-06-24
Author: Yangbh
Func: Gather web proxy interfaces from  http://www.youdaili.cn/
'''
import requests
import threading

from bs4 import BeautifulSoup
from urlparse import urljoin

lock = threading.Lock()

def downNse(href,nsename):
	try:
		lock.acquire()
		print href
		lock.release()
		nsefile = requests.get(href).text
		fp = open('../cache/nmapscripts/'+nsename,'w')
		fp.write(nsefile.encode('utf8'))
		fp.close()
	except Exception,e:
		print 'Exception',e


def main():
	url = 'https://svn.nmap.org/nmap/scripts/'
	a=requests.get(url)
	soup = BeautifulSoup(a.text)
	results = soup.findAll('a',href=True)
	threads = []

	for a in results:
		#必须将链接encode为utf8, 因为中文文件链接如 http://aa.com/文件.pdf 
		#在bs4中不会被自动url编码，从而导致encodeException
		nsename = a.getText()
		if nsename.endswith('.nse'):
			href = a.get('href').encode('utf8')
			href = urljoin(url, href)#处理相对链接的问题
			t = threading.Thread(target=downNse,args=(href,nsename))
			threads.append(t)

	i = 0
	maxthreads = 50
	while i<len(threads):
		if i+maxthreads >len(threads):
			numthreads = len(threads) - i
		else:
			numthreads = maxthreads
		print 'threads:',i,' - ', i + numthreads

		# start threads
		for j in range(numthreads):
			threads[i+j].start()

		# wait for threads
		for j in range(numthreads):
			threads[i+j].join()

		i += maxthreads

if __name__ == '__main__':
	main()