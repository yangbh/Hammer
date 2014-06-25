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
import MySQLdb

import sys
sys.path.insert(0, '../lib')

try:
	import mysql_class
except ImportError:
	print '[!] mysql_class not found.'
	sys.exit(0)

maxinterfaces = 100
maxarticles = 1
maxpages = 10
repeattimes = 2

result = []
mutex = thread.allocate_lock()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def getInterfaces():
	readnum = 10
	interfaces = []

	# step 1: get http://www.youdaili.cn/index.html
	indexurl = 'http://www.youdaili.cn/Daili/http/index.html'
	indexurl_cont = urllib2.urlopen(indexurl).read() 
	#print indexurl_cont
	urls = re.findall('<a href="([^"]+)" target="_blank"><font color=#FF7300>【HTTP代理】</font>',indexurl_cont)
	if len(urls)>maxarticles:
		urls=urls[0:maxarticles]
	
	# step 2: get aticals
	for eachurl in urls:
		print 'reading article: ', eachurl
		eachurl_cont = urllib2.urlopen(eachurl).read()
		# get pages
		tmp = re.search('<li><a>\xe5\x85\xb1([\d])*\xe9\xa1\xb5: </a></li>', eachurl_cont)
		if tmp.group(1):
			tmp2=int(tmp.group(1))
			pages = tmp2 if tmp2<maxpages else maxpages
		else:
			pages = 1
		print 'pages=', pages

		# page 1
		print 'reading page 1: ', eachurl
		tmp = re.findall('(\r\n|<p>){1}([\d\.]+):([^@]+)@([^#]+)#([^<]+)(<br />|</p>){1}',eachurl_cont)
		for each_tmp in tmp:
			useful_tmp = each_tmp[1:-1]
			#print useful_tmp
			interfaces.append(useful_tmp)
			for value in useful_tmp:
				print value + '\t',
			print ''
		#  other pages
		for x in xrange(1,pages):
			page_url = eachurl[0:-5] + '_' + str(x+1) +'.html'
			print 'reading page ',x+1,':', page_url
			eachurl_cont = urllib2.urlopen(page_url).read()
			tmp = re.findall('(\r\n|<p>){1}([\d\.]+):([^@]+)@([^#]+)#([^<]+)(<br />|</p>){1}',eachurl_cont)
			for each_tmp in tmp:
				useful_tmp = each_tmp[1:-1]
				#print useful_tmp
				interfaces.append(useful_tmp)
				for value in useful_tmp:
					print value + '\t',
				print ''

	interfaces = list(set(interfaces))
	#for each in interfaces:
	#	for value in each:
	#		print value + '\t',
	#	print ''
	return interfaces
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def getTime(interface,basicurl='http://www.baidu.com'):
	global result, mutex

	proxyurl = interface[2].lower() + '://' + interface[0] + ':' +interface[1]

	proxy_handler = urllib2.ProxyHandler({"http" : proxyurl})
	opener = urllib2.build_opener(proxy_handler)
	
	timetotal = 0
	printresult = proxyurl + '\r\n'
	for x in xrange(1,repeattimes+1):
		printresult += '\t'+str(x)+':\t'
		timesec = 600
		start = time.time()
		try:
			opener.open(basicurl,timeout=60)
			end = time.time()
			timesec = end - start
			printresult += str(timesec)
		except urllib2.URLError, e:
			printresult += 'urllib2.URLError ' + str(e)
		except httplib.BadStatusLine, e:
			printresult += 'httplib.BadStatusLine ' + str(e)
		except socket.timeout, e:
			printresult += 'socket.timeout ' + str(e)
		except socket.error, e:
			printresult += 'socket.error' + str(e)

		printresult +='\r\n'
		timetotal += int(timesec)

	timeavrage = int(timetotal/repeattimes)
	printresult += '\ttimeavrage=\t' + str(timeavrage) + '\r\n'

	tmp = list(interface)
	tmp.append(timesec)
	tmp = tuple(tmp)

	if mutex.acquire(5):
		#print tmp
		if printresult:
			print printresult
		if timeavrage<60:
			result.append(tmp)
		mutex.release()

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
	length = len(interfaces) if len(interfaces)<maxinterfaces else maxinterfaces
	while i<length:
		j = 0
		while j<maxthread:
			thread.start_new_thread(getTime,(interfaces[i+j],basicurl))
			j +=1
			i +=1
		i+=1
		time.sleep(1)

	tmp = sorted(result, key=lambda result : result[-1])
	sort_result = []
	for each_tmp in tmp:
		tt = []
		tt.append(each_tmp[0])
		tt.append(int(each_tmp[1]))
		tt += list(each_tmp[2::])
		#print tt
		sort_result.append(tuple(tt))
	#print sort_result

	# step 3: insert into mysql db
	try:
		sql = mysql_class.MySQLHelper('localhost','ham_usr','ham_pwd')
		sql.selectDb('hammer')
		sql.cur.execute('DELETE FROM Proxy')
		sql.cur.execute('ALTER TABLE  Proxy AUTO_INCREMENT = 1')
		#sqlcmd = "INSERT INTO Proxy(IP_Addr,Port,Http_Type,Address,Time) VALUES(%s,%s,%s,%s,%s)"
		#sql.cur.executemany(sqlcmd,sort_result)
		sql.commit()
		sql.close()
	except MySQLdb.Error,e:
		print 'MySQLdb.Error', e
	except MySQLdb.IntegrityError, e:
		print 'MySQLdb.IntegrityError', e
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()