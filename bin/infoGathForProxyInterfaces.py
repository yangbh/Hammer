#!/usr/bin/python2.7
#coding:utf-8
'''
Time: 2014-06-24
Author: Yangbh
Func: Gather web proxy interfaces from  http://www.youdaili.cn/
'''
import urllib2
import re

import sys
sys.path.insert(0, '../lib')

try:
		import mysql_class
except ImportError:
		print '[!] mysql_class not found.'
		sys.exit(0)

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def main():
	''' '''
	#sql = mysql_class.MySQLHelper('192.168.1.2','mac_usr','mac_pwd')
	#sql.selectDb('hammer')

	# step 1: get http://www.youdaili.cn/index.html
	url = 'http://www.youdaili.cn/index.html'
	indexhtml=urllib2.urlopen(url).read() 
	print indexhtml

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()