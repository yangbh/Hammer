#!/usr/bin/python2.7
#coding:utf-8
'''
Time: 2014-06-17
Author: Yangbh
Func: Gather company information from wooyun.org, including company name and host
'''
import urllib2
import sqlite3
import re

WooYunDB = '../cache/wooyun.sqlite3'

# --------------------------------------------------
# 
# --------------------------------------------------
def runsql(sql):
    '''execute a sql'''
    conn = sqlite3.connect(WooYunDB)
    conn.execute(sql)
    conn.commit()
    conn.close()
# --------------------------------------------------
# 
# -------------------------------------------------
def geturl(url):
	pass
# --------------------------------------------------
# 
# --------------------------------------------------
def main():
	comps=[]
	for x in xrange(1,50):
		url = 'http://wooyun.org/corps/page/'+str(x)
	
		try:  
			html = urllib2.urlopen(url).read() 
			comps = re.findall('">([0-9]{4}-[0-9]{2}-[0-9]{2})</td>\r\n\t\t\t\t\t<td width="\w+"><a[^>]+>([^<]+)</a></td>\r\n\t\t\t\t\t<td width="\w+"><a[^>]+>([^<]+)</a>',html)
			for eachcomp in comps:
				#print eachcomp[0],eachcomp[1].decode('utf-8'),eachcomp[2]
				print eachcomp[0],eachcomp[1],eachcomp[2]
			if len(comps) != 20:
				break

		except urllib2.URLError, e:  
		    print e.reason 	
	
# --------------------------------------------------
# 
# --------------------------------------------------
if __name__ == '__main__':
	main()