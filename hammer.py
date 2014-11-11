#!/usr/bin/python2.7
#coding:utf-8

import sys
import getopt
import re
sys.path.append('./lib')
# from scanner_class_mp import Scanner
from scanner_class_basic import Scanner
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
	print "Usage: hammer.py [Options] [Targets]\n"
	# print "\t-u --url: url address, like http://www.leesec.com/"
	print "[Options]"
	print "\t-s --server: your hammer web server host address, like www.hammer.org"
	print "\t-t --token: token, find it in http://www.hammer.org/user.php"
	print "\t-U --update-plugins: update new added plugins to web"
	print "\t-h: help"
	print "[Targets]"
	print "\t-T --target: target, can be an ip address, an url or an iprange"
	print "[Examples]"
	print "\thammer.py -s www.hammer.org -t 3r75... -U plugins/Info_Collect/"
	print "\thammer.py -s www.hammer.org -t 3r75... -T http://www.leesec.com/"
	print "\thammer.py -s www.hammer.org -t 3r75... -T 192.168.1.1/24"
	# print ''
	sys.exit(0)

def main():
	show()
	try :
		opts, args = getopt.getopt(sys.argv[1:], "hs:t:U:T:",['help','server=','token=','update-plugins=','target='])
	except getopt.GetoptError,e:
		print 'getopt.GetoptError',e
		usage()

	_url = None
	_server = None
	_token = None


	for opt, arg in opts:
		if opt in ('-h','--help'):
			usage()
		elif opt in ('-s','--server'):
			_server = arg
		elif opt in ('-T','--target'):
			_target = arg
		elif opt in ('-t','--token'):
			_token = arg
		elif opt in ('-U','--update-plugins'):
			if arg:
				_pluginpath = arg
			else:
				_pluginpath = 'plugins/'
		else:
			pass

	if _server and _token:
		if '_pluginpath' in dir():
			# print '_pluginpath=',_pluginpath
			# print '_server=',_server
			# print '_token=',_token
			loadPlugins(_pluginpath,_server,_token)

		elif '_target' in dir():
			sn = Scanner(_server,_token,_target)
			sn.initInfo()
			sn.infoGather()
			sn.scan()

		else:
			usage()
	else:
		usage()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()