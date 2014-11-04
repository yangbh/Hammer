#!/usr/bin/python2.7
#coding:utf-8

import sys
import getopt
import re
sys.path.append('./lib')
from scanner_class_mp import Scanner
from plugin2sql import loadPlugins
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
	print "Usage: hammer.py [options] [-u url]\n"
	# print "\t-u --url: url address, like http://www.leesec.com/"
	print "[options]"
	print "\t-s --server: your hammer web server host address, like www.hammer.org"
	print "\t-t --token: token, find it in http://www.hammer.org/user.php"
	print "\t-U --update-plugins: update new added plugins to web"
	print "\t-h: help"
	print "[Examples]"
	print "\thammer.py -s www.hammer.org -t 3r75... -u http://www.leesec.com/"
	print "\thammer.py -s www.hammer.org -t 3r75... -U plugins/Info_Collect/"
	# print ''
	sys.exit(0)

def main():
	show()
	try :
		opts, args = getopt.getopt(sys.argv[1:], "hs:t:u:U:",['help','server=','token=','url=','update-plugins='])
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
		elif opt in('-U','--update-plugins'):
			if arg:
				_pluginpath = arg
			else:
				_pluginpath = 'plugins/'
		else:
			pass

	if _server and _token and  _pluginpath:
		# print '_pluginpath=',_pluginpath
		# print '_server=',_server
		# print '_token=',_token
		loadPlugins(_pluginpath,_server,_token)

	elif _url and _server and _token:
		sn = Scanner(_url,_server,_token)
		sn.startScan()

	else:
		usage()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()