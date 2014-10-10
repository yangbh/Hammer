#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
import socket
import threading

from urlparse import urlparse
from dummy import *

info = {
	'NAME':'Probe File Discover',
	'AUTHOR':'yangbh',
	'TIME':'20140716',
	'WEB':'',
	'DESCRIPTION':'Tries to find sensitive files. such as phpinfo.php、fckeditor、user.txt、password.txt'
}

ret = ''
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def getCrawlerPaths(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		urls = cf.getSection('Paths')
		return urls
	except Exception,e:
		print 'Exception:\t',e
		return [url]

def getCrawlerFileExts(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		exts = cf.getSection('FileExtensions')
		return exts
	except Exception,e:
		print 'Exception:\t',e
		return []

def getDict(filename):
	''' '''
	try:
		ret = [] 
		fp = open(filename,'r')
		for eachline in fp:
			eachline = eachline.replace('\r','')
			eachline = eachline.replace('\n','')
			if eachline == '':
				continue
			if eachline[0] == '#':
				continue
			ret.append(eachline)
		fp.close()
		return ret
	except Exception,e:
		print 'Exception:\t',e
		return []

def generateUrls(url):
	''' '''
	urls = []
	dictfile = BASEDIR + '/lib/db/probe_file.dict'
	dicts = getDict(dictfile)
	#print 'dicts=\t',dicts

	exts = getCrawlerFileExts(url)
	#print 'exts=\t',exts

	paths = getCrawlerPaths(url)
	#print 'paths=\t',paths

	for eachpath in paths:
		for eachdict in dicts:
			if eachdict.find('.php') != -1 and '.php' not in exts:
				continue
			urls.append(eachpath+eachdict)

	# ret = list(set(urls))
	# ret.sort()
	return urls

def httpcrack(url,lock):
	global ret
	printinfo = None
	flg = False

	for i in range(3):
		try:
			ul = urllib2.urlopen(url)
			httpcode = ul.getcode()
			if httpcode == 200:
			 	httpcont = ul.read()
			 	# print url
			 	# print httpcont
			 	# print httpcont.find('Frederico Caldeira Knabben')
			 	flg = True
				if httpcont.find('<title>phpinfo()</title>') != -1:
					printinfo =  '<phpinfo>' + url + os.linesep
				elif url.endswith('readme.txt'):
					printinfo =  '<readme.txt>' + url + os.linesep
				elif url.find('fckeditor')  != -1 and httpcont.find('Frederico Caldeira Knabben') != -1:
					printinfo =  '<fckeditor>' + url + os.linesep
			 	else:
			 		flg = False
			break
		except socket.timeout,e:
			continue
		except Exception,e:
			if type(e) == urllib2.HTTPError:
				if e.getcode() in [401,403]:
					flg = True
					if url.find('/.svn') != -1:
						printinfo =  '<svn>' + url + '\t code:' + str(e.getcode()) + os.linesep
					else:
						printinfo = url + '\t code:' + str(e.getcode()) + os.linesep
				else:
					printinfo = url + '\t code:' + str(e.getcode()) + os.linesep
			else:
				printinfo = url + '\tException' + str(e) + os.linesep
			break

	lock.acquire()
	if printinfo:
		print printinfo,
		if flg:
			ret += printinfo
	lock.release()

	return(flg,printinfo)

def Audit(services):
	retinfo = {}
	output = ''
	if services.has_key('url'):
		output += 'plugin run' + os.linesep
		urls = generateUrls(services['url'])
		#print 'urls=\t'
		#pprint(urls)

		#  threads
		lock = threading.Lock()
		threads = []
		maxthreads = 20

		for url in urls:
			th = threading.Thread(target=httpcrack,args=(url,lock))
			threads.append(th)
		i = 0
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
	
	if ret != '':
		retinfo = {'level':'low','content':ret}
		security_warming(str(ret))

	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url='http://www.eguan.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)