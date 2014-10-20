#!/usr/bin/python2.7
#coding:utf-8

import sys
import getopt
import re
sys.path.append('./lib')
from scanner_class_mp import Scanner
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def show():
	print'''
   ██░ ██  ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
  ▓██░ ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
  ▒██▀▀██░▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ░▓█ ░██ ░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
  ░▓█▒░██▓ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ▒ ░▒░ ░  ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
   ░  ░░ ░  ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
   ░  ░  ░      ░  ░       ░          ░      ░  ░   ░     
  
	'''

def usage():
	print "Usage: hammer.py [options] -u url\n"
	# print "\t-u --url: url address, like http://www.leesec.com/"
	print "[options]"
	print "\t-s --server: your hammer web server host address, like www.hammer.org"
	print "\t-t --token: token, find it in http://www.hammer.org/user.php"
	print "\t-h: help"
	print "[Examples]"
	print "\thammer.py -u http://www.leesec.com/ -s www.hammer.org -t 3r75... \n"
	sys.exit(0)

def main():
	show()
	try :
		opts, args = getopt.getopt(sys.argv[1:], "hs:t:u:",['help','server=','token=','url='])
	except getopt.GetoptError:
		usage()

	_url = None
	_server = None
	_token = None

	for opt, arg in opts:
		if opt in ('-h','--help'):
			usage()
		elif  opt in ('-u','--url'):
			_url = arg
			if _url[-1] != '/':
				_url += '/'
		elif opt in ('-s','--server'):
			_server = arg
		elif opt in ('-t','--token'):
			_token = arg
		else:
			pass
	if _url == None:
		usage()

	if _url and _server and _token:
		sn = Scanner(_url,_server,_token)
		sn.startScan()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()