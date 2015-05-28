#!/usr/bin/python2.7
#coding:utf-8

import requests
# 导入hammer模块各种库
from dummy import *

# 插件信息
info = {
	'NAME':'Robots.txt Sensitive Information',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
	'DESCRIPTION':'robots.txt文件扫描',
	'VERSION':'1.0',
	'RUNLEVEL':2
}
opts = {
	'url':'http://www.leesec.com',	#'target ip'
}
# opts = [
# 	['url','http://www.leesec.com','target url'],
# ]

# 任务分配函数Assign
def Assign(services):
	if services.has_key('url'):
		return True
	return False

# 漏洞检测函数Audit
def Audit(services):
	url = services['url']+ '/robots.txt'
	rq = requests.get(url,allow_redirects=False,timeout=30)
	if rq.status_code == 200 and 'Disallow: ' in rq.text:
		# 漏洞反馈函数security
		security_note(url) 
		# 调试输出函数logger,默认等级为
		logger('Find %srobots.txt' % url)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.leesec.com'}
	Audit(services)
	pprint(services)