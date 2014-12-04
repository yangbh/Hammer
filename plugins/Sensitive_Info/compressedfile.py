#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
import socket
import threading
import futures
import requests

from urlparse import urlparse
from dummy import *

info = {
	'NAME':'Compresed Files Download Vulnerability',
	'AUTHOR':'yangbh',
	'TIME':'20140716',
	'WEB':'',
	'DESCRIPTION':'Tries to find sensitive compressd files. such as .zip、.rar、.gz、.tar.gz、.gz'
}

ret = ''
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
http404page = ''

def get404Page(url='404.html'):
	try:
		print url
		rq = requests.get(url,timeout=30)
		http404page = rq.text
		return http404page
	except Exception,e:
		print 'Exception',e
		return None

def getCrawlerPaths(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		urls = cf.getSection('Paths')
		return urls
	except Exception,e:
		print 'Exception:\t',e
		return [url]

def generateUrls(url):
	baseulp = urlparse(url)
	host = baseulp.netloc

	paths = getCrawlerPaths(url)
	#pprint(paths)
	
	urls = []
	rulefile = BASEDIR + '/lib/db/compresed_file.rule'
	for eachpath in paths:
		eachulp = urlparse(eachpath)
		if eachulp.path == '':
			host = eachulp.netloc
			domain = GetFirstLevelDomain(host)
			args = {'host':host,'com':domain}

		else:
			pos = eachulp.path.rfind('/')
			tmp = eachulp.path[pos+1:]
			args = {'com':tmp}

		rf = RuleFile(rulefile,args)
		rf._getRules()
		for i in rf.ret:
			urls.append(eachpath + '/' +i)

	ret = list(set(urls))
	ret.sort()
	return ret

def httpcrack(url):
	global ret, http404page
	printinfo = None
	flg = False
	# print url
	for i in range(3):
		# 改用requests库
		try:
			rq = requests.get(url,allow_redirects=False,timeout=30)
			print url,rq.status_code
			if rq.status_code in [200,403] and rq.text != http404page:
				# if '404' not in rq.text:
				# 	pass
				printinfo = url + '\t code:' + str(rq.status_code) + os.linesep
				security_warning(url + '\t code:' + str(rq.status_code))
				flg = True
			break
		# 一些并发导致的异常
		except Exception,e:
			print 'Exception',e
		# try:
		# 	httpcode = urllib2.urlopen(url).getcode()
		# 	if httpcode == 200:
		# 	 	printinfo = url + '\tcode:' + str(httpcode) + os.linesep
		# 	 	flg = True
		# 	break
		# except socket.timeout,e:
		# 	continue
		# except Exception,e:
		# 	if type(e) == urllib2.HTTPError:
		# 		if e.getcode() in [401,403]:
		# 			flg = True
		# 		printinfo = url + '\tcode:' + str(e.getcode()) + os.linesep
		# 	else:
		# 		printinfo = url + '\tException' + str(e) + os.linesep
		# 	break

	# lock.acquire()
	# if printinfo:
	# 	print printinfo,
	# 	if flg:
	# 		ret += printinfo
	# lock.release()

	return(flg,printinfo)

def Assign(services):
	if services.has_key('url'):
		return True
	return False

def Audit(services):
	global ret, http404page
	retinfo = {}
	output = 'plugin run' + os.linesep

	# first get http404 code page
	http404page = get404Page(services['url']+'/404.html')
	
	urls = generateUrls(services['url'])
	# pprint(urls)

	#  threads
	lock = threading.Lock()
	threads = []
	maxthreads = 20

	# for url in urls:
	# 	th = threading.Thread(target=httpcrack,args=(url,lock))
	# 	threads.append(th)
	# i = 0
	# while i<len(threads):
	# 	if i+maxthreads >len(threads):
	# 		numthreads = len(threads) - i
	# 	else:
	# 		numthreads = maxthreads
	# 	print 'threads:',i,' - ', i + numthreads

	# 	# start threads
	# 	for j in range(numthreads):
	# 		threads[i+j].start()

	# 	# wait for threads
	# 	for j in range(numthreads):
	# 		threads[i+j].join()

	# 	i += maxthreads

	# 改用futures模块
	# with futures.ThreadPoolExecutor(max_workers=maxthreads) as executor:     #默认10线程
	# 	future_to_url = dict((executor.submit(httpcrack, url), url) for url in urls)

	with futures.ThreadPoolExecutor(max_workers=maxthreads) as executor:
		# Start the load operations and mark each future with its URL
		future_to_url = dict((executor.submit(httpcrack, url), url) for url in urls)
		# try:
		for future in futures.as_completed(future_to_url):
			url = future_to_url[future]
			try:
				ret = future.result()
			except Exception as exc:
				print('%r generated an exception: %s' % (url, exc))
			else:
				print('%r returns: %s' % (url, str(ret)))
		
		# except (KeyboardInterrupt, SystemExit):
		# 	print "Exiting..."
		# 	return (retinfo,output)
	if ret != '':
		retinfo = {'level':'medium','content':ret}

	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url='http://testphp.vulnweb.com'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)