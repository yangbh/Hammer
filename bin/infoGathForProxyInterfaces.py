#!/usr/bin/python2.7
#coding:utf-8
'''
Time: 2014-06-24
Author: Yangbh
Func: Gather web proxy interfaces from  http://www.youdaili.cn/
'''
import urllib2
import re
import time
import thread
import httplib
import socket

import sys
sys.path.insert(0, '../lib')

try:
		import mysql_class
except ImportError:
		print '[!] mysql_class not found.'
		sys.exit(0)

result = []
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def getInterfaces():
	readnum = 10
	interfaces = []

	# step 1: get http://www.youdaili.cn/index.html
	indexurl = 'http://www.youdaili.cn/Daili/http/index.html'
	indexurl_cont = urllib2.urlopen(indexurl).read() 
	#print indexhtml
	urls = re.findall('<a href="([^"]+)" target="_blank"><font color=#FF7300>【HTTP代理】</font>',indexurl_cont)
	
	# step 2: get aticals
	for eachurl in urls:
		eachurl_cont = urllib2.urlopen(eachurl).read()
		tmp = re.findall('(\r\n|<p>){1}([\d\.]+):([^@]+)@([^#]+)#([^<]+)(<br />|</p>){1}',eachurl_cont)
		for each_tmp in tmp:
			useful_tmp = each_tmp[1:-1]
			#print useful_tmp
			interfaces.append(useful_tmp)
			for value in useful_tmp:
				print value + '\t',
			print ''

	return interfaces
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def getTime(interface,basicurl='http://www.baidu.com'):
	global result

	proxyurl = interface[2].lower() + '://' + interface[0] + ':' +interface[1]

	proxy_handler = urllib2.ProxyHandler({"http" : proxyurl})
	opener = urllib2.build_opener(proxy_handler)
	
	start = time.time()
	try:
		opener.open(basicurl,timeout=300)
	except urllib2.URLError,e:
		print 'urllib2.URLError',e
		start = 0
		time.sleep(1)
	except httplib.BadStatusLine,e:
		print 'httplib.BadStatusLine',e
	except socket.timeout,e:
		print 'socket.timeout',e
	except socket.error,e:
		print 'socket.error',e
	end = time.time()
	timesec = end - start

	tmp = list(interface)
	tmp.append(timesec)
	tmp = tuple(tmp)
	#print tmp

	result.append(tmp)

	print proxyurl,'\t\ttimesec=',timesec

	return timesec
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def main():
	''' '''
	maxthread = 10
	basicurl = 'http://www.baidu.com'
	# step 1: get interfaces
	interfaces = getInterfaces()
	#print interfaces
	# step 2: get each interface timesec
	i = 0
	length = len(interfaces)
	while i<length:
		j = 0
		while j<maxthread:
			thread.start_new_thread(getTime,(interfaces[i+j],basicurl))
			j +=1
			i +=1
		time.sleep(5)

	# step 3: insert into mysql db
	#sql = mysql_class.MySQLHelper('192.168.1.2','mac_usr','mac_pwd')
	#sql.selectDb('hammer')


# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()