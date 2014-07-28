#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
import threading

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
def getCrawlerPaths(url):
	''' '''
	try:
		filename = BASEDIR + '/cache/crawler/' + genFilename(url) + '.txt'
		#print 'filename=\t',filename
		paths = []
		baseulp = urlparse(url)

		fp = open(filename,'r')
		for eachline in fp:
			eachline = eachline.replace(os.linesep,'')
			#print eachline
			eachulp = urlparse(eachline)
			if baseulp.scheme == eachulp.scheme and baseulp.netloc == eachulp.netloc:
				fullpath = eachulp.path
				if fullpath.find('.') == -1 and fullpath.endswith('/') == False:
					fullpath += '/'
				pos = 0
				while True:
					pos = fullpath.find('/',pos)
					if pos == -1:
						break
					tmppth = eachulp.scheme + '://' + eachulp.netloc + eachulp.path[:pos]
					if tmppth.endswith('/'):
						#tmppth = tmppth[:-1]
						continue
					if tmppth not in paths:
						paths.append(tmppth)
					pos +=1

		fp.close()
		return paths
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

def httpcrack(url,lock):
	global ret
	printinfo = url + os.linesep
	flg = False
	try:
		 httpcode = urllib2.urlopen(url).getcode()
		 if httpcode == 200:
		 	printinfo += 'exists' + os.linesep
		 	flg = True
	except Exception,e:
		printinfo += 'Exception' + str(e) + os.linesep

	lock.acquire()
	print printinfo
	if flg:
		ret += printinfo
	lock.release()

	return(flg,printinfo)

def Audit(service):
	retinfo = {}
	output = ''
	if services.has_key('url'):
		output += 'plugin run' + os.linesep
		urls = generateUrls(services['url'])
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
		retinfo = {'level':'middle','content':ret}

	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://localhost'}
	pprint(Audit(services))
	pprint(services)