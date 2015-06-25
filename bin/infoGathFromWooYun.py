#!/usr/bin/python2.7
#coding:utf-8
'''
Time: 2014-06-17
Author: Yangbh
Func: Gather company information from wooyun.org, including company name and host
'''
import urllib2
import re
import socket
import requests
import time

import sys
sys.path.insert(0, '../lib')

try:
	import mysql_class
except ImportError:
	print '[!] mysql_class not found.'
	#print sys.path
	sys.exit(0)

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def main():
	''' '''
	# sql = mysql_class.MySQLHelper('192.168.1.2','mac_usr','mac_pwd')
	# sql.selectDb('hammer')

	comps=[]
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'}
	for x in xrange(1,36):
		url = 'http://wooyun.org/corps/page/'+str(x)
		
		try:  
			rq = requests.get(url,headers=headers)
			time.sleep(2)
			# html = urllib2.urlopen(url).read() 
			html = rq.text
			comps = re.findall('">([0-9]{4}-[0-9]{2}-[0-9]{2})</td>\r\n\t\t\t\t\t<td width="\w+"><a[^>]+>([^<]+)</a></td>\r\n\t\t\t\t\t<td width="\w+"><a[^>]+>([^<]+)</a>',html)
			for eachcomp in comps:
				#print eachcomp[0],eachcomp[1].decode('utf-8'),eachcomp[2]
				print eachcomp[0],eachcomp[1],eachcomp[2]
				continue
				
				sqlcmd="INSERT INTO company(Name,Remark) VALUES('"+eachcomp[1]+"','"+eachcomp[0]+"')"
				print sqlcmd
				sql.cur.execute(sqlcmd)
				
				# IP表
				sqlcmd="SELECT * FROM company WHERE Name='%s' LIMIT 1" % eachcomp[1]
				print sqlcmd
				sql.cur.execute(sqlcmd)
				comp_id=sql.cur.fetchone()[0]
				host=re.search('http[s]?://([^/]+)',eachcomp[2])
				host=host.group(1)
				print host
				ip_addr=socket.gethostbyname(host)
				sqlcmd="INSERT INTO IP(Addr,Comp_ID) VALUES('%s',%d)" %(ip_addr,comp_id)
				print sqlcmd
				sql.cur.execute(sqlcmd)

				# host表
				sqlcmd="SELECT * FROM ip WHERE Addr='%s' LIMIT 1" % ip_addr
				print sqlcmd
				sql.cur.execute(sqlcmd)
				ip_id=sql.cur.fetchone()[0]
				sqlcmd="INSERT INTO host(Value,IP_ID,Comp_ID) VALUES('%s',%d,%d)" %(host,ip_id,comp_id)
				print sqlcmd
				sql.cur.execute(sqlcmd)

			if len(comps) != 20:
				break

		except urllib2.URLError, e:  
		    print e
		except socket.gaierror, e:
			print e
	
	# sql.commit()
	# sql.close()

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()