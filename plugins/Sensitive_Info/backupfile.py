#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
import threading

from urlparse import urlparse
from dummy import *

info = {
	'NAME':'Backup Files Download Vulnerability',
	'AUTHOR':'yangbh',
	'TIME':'20140716',
	'WEB':'',
	'DESCRIPTION':'Tries to find sensitive backup files.'
}

ret = ''
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def getCrawlerHrefs(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		urls = cf.getSection('Hrefs')
		return urls
	except Exception,e:
		print 'Exception:\t',e
		return [url]

def getCrawlerFiles(url):
	''' '''
	try:
		files = []
		hrefs = getCrawlerHrefs(url)
		#pprint(hrefs)
		for eachhref in hrefs:
			pos = eachhref.find('?')
			if pos == -1:
				continue
			linkfile = eachhref[:pos]
			linkfile = linkfile[::-1]
			if linkfile.find('.',0,10) == -1:
				continue
			files.append(linkfile[::-1])
		return files
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
	
	#pprint(paths)
	urls = []
	dictfile = BASEDIR + '/lib/db/backup_file.dict'
	dicts = getDict(dictfile)
	#print 'dicts=\t',dicts
	files = getCrawlerFiles(url)
	#print 'files=\t',files
	for eachfile in files:
		for eachdict in dicts:
			urls.append(eachfile+eachdict)

	# ret = list(set(urls))
	# ret.sort()
	return urls

def httpcrack(url,lock):
	global ret
	printinfo = None
	flg = False
	try:
		 httpcode = urllib2.urlopen(url).getcode()
		 if httpcode == 200:
		 	printinfo = url + '\t code:' + httpcode + os.linesep
		 	flg = True
	except Exception,e:
		if type(e) == urllib2.HTTPError:
			if e.getcode() in [401,403]:
				flg = True
			printinfo = url + '\t code:' + str(e.getcode()) + os.linesep
		else:
			printinfo = url + '\tException' + str(e) + os.linesep

	lock.acquire()
	if printinfo:
		print printinfo,
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
		pprint(urls)

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
	url='http://www.hengtiansoft.com'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)