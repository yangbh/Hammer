#!/usr/bin/python2.7
#coding:utf-8

from dummy import *

info = {
	'NAME':'Probe File Discover',
	'AUTHOR':'yangbh',
	'TIME':'20140716',
	'WEB':'',
	'DESCRIPTION':'Tries to find sensitive files. such as phpinfo.php、fckeditor、user.txt、password.txt'
}

def Audit(service):
	pass

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.hengtiansoft.com'}
	pprint(Audit(services))
	pprint(services)