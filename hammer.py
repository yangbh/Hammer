#!/usr/bin/python2.7
#coding:utf-8

import sys
import getopt
import re

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def show():
	print'''
	####################################################
	##
	##
	##
	##	
	##	author	:  yangbh
	##	email  	:  
	####################################################
	'''

def usage():
	print "Usage: hammer.py [options] -u url\n"
	print "\t-u --url: url address, like http://www.leesec.com/"
	print "\t-h: help"
	print "\nExamples:"
	print "\thammer.py -u http://www.leesec.com/\n"
	sys.exit(0)

def main():
	# step1: get arguments
	show()
	try :
		opts, args = getopt.getopt(sys.argv[1:], "hu:")
	except getopt.GetoptError:
		usage()

	_url = None

	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt == '-u':
			_url = arg
		else:
			pass
	if _url == None:
		usage()

	m = re.match('(http[s]?)://([^:^/]+):?([^/]*)/',_url)
	_http_type,_host,_ports,_domain = None,None,None,None
	if m:
		_http_type = m.group(1)
		_host = m.group(2)
		_ports = m.group(3)
		_domain = _host[(_host.find('.')+1):]
		print _http_type,_host,_ports,_domain

	# step2: init syspath
	basepath = sys.path[0]
	sys.path.append(basepath +'/lib')
	sys.path.append(basepath +'/plugins')
	sys.path.append(basepath +'/bin')

	# step3: get subdomains
	from lib.knock_class import SubDomain

	checksubdomain = True
	if checksubdomain == True:
		
		sb = SubDomain(_domain)
		#sb.help()
		if 	sb.CheckForWildcard(sb.host) != False:
			sys.exit(1)

		sb.checkzone(sb.host)
		sb.subscan(sb.host,sb.wordlist)
		print sb.found
	
	sys.exit(0)

	# step4: run scans
	from lib.scanner_class import Scanner
	
	sn =Scanner(_url)
	sn.getServices()
	sn.startScan()
	print ">>>scan result:"
	print sn.result
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()