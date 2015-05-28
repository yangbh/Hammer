#!/usr/bin/python2.7
#coding:utf-8

import os
import sys
import getopt
import json
# import re
sys.path.append('./lib')
# from scanner_class_mp import Scanner

import globalVar

from pprint import pprint
from common import genFileName_v2
from commonFun import genTargetName
from scanner_class_basic import Scanner
from scanner_class_pluginrunner import PluginMultiRunner
# from listener_class import Listener
from listener_class_mp import Listener
from consoler_class import Consoler
from consoleUser_class import WebUser
from plugin2sql import loadPlugins
from proxyScraper_class import ProxyScraper
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
	print "Usage: hammer.py [Auth] [Options] [Targets]\n"
	# print "\t-u --url: url address, like http://www.leesec.com/"
	print "[Auth]"
	print "\t-s --server: your hammer web server host address, like www.hammer.org"
	print "\t-t --token: token, find it in http://www.hammer.org/user.php"
	print "[Options]"
	print "\t-u --update-plugins: update new added plugins to web"
	print "\t   --update-proxies: update proxies to web server"
	print "\t   --update-config: update config to web server"
	print "\t-v --verbose: increase verbosity level"
	print "\t   --threads: max number of process, default cpu number"
	print "\t   --auto-proxy: use auto proxy, make sure server exist proxies first"
	print "\t-h: help"
	print "[Targets]"
	print "\t-T --target: target, can be an ip address, an url or an iprange"
	print "\t   --no-gather: do not use information gather module"
	print "\t   --gather-depth: information gather depth, default 1"
	print "\t   --conf-file: config file, default be conf/basic.conf"
	print "\t-p --plugin: run a plugin type scan"
	print "\t   --plugin-arg: plugin argus"
	print "\t-l --listen: listen mode"
	print "\t   --max-size: scan pool max size, default 50"
	print "\t--console: console mode"
	print "[Examples]"
	print "\thammer.py -s www.hammer.org -t 3r75... --update-plugins plugins/Info_Collect/"
	print "\thammer.py -s www.hammer.org -t 3r75... --console"
	print "\thammer.py -T http://testphp.vulnweb.com"
	print "\thammer.py --conf-file conf/basic.conf"
	print "\thammer.py -T vulnweb.com --conf-file conf/basic.conf"
	print "\thammer.py -p plugins/System/dnszone.py -T vulnweb.com"
	print "\thammer.py -l"
	sys.exit(0)

def main():

	try :
		opts, args = getopt.getopt(sys.argv[1:], "hvls:t:u:T:p:",['help','verbose=','server=','token=','update-plugins=','update-proxies','update-config','auto-proxy','target=','plugin=','plugin-arg=','no-gather','gather-depth=','threads=','conf-file=','listen','console'])
	except getopt.GetoptError,e:
		print 'getopt.GetoptError',e
		usage()

	# default arguments
	_target = None
	_server = None
	_token = None
	# _gather_flag = True
	_listen = False
	_console = False
	_gather_depth = 1
	_vv = 'INFO'
	_plugin_arg=None
	_threads = None
	_maxsize = 50
	_update_proxy = False
	_update_config = False
	_auto_proxy = False
	_conf_file = 'conf/basic.conf'

	for opt, arg in opts:
		if opt in ('-h','--help'):
			show()
			usage()
		elif opt in ('-v'):
			_vv = 'DEBUG'
		elif opt in ('--no-gather'):
			# _gather_flag = False
			_gather_depth = 0
		elif opt in ('--gather-depth'):
			_gather_depth = int(arg)
		elif opt in ('-s','--server'):
			_server = arg
		elif opt in ('-t','--token'):
			_token = arg
		elif opt in ('-u','--update-plugins'):
			if arg:
				_pluginpath = arg
			else:
				_pluginpath = 'plugins/'
		elif opt in ('--update-proxies'):
			_update_proxy = True
		elif opt in ('--update-config'):
			_update_config = True
		elif opt in ('--auto-proxy'):
			_update_proxy = True
		elif opt in ('--conf-file'):
			_conf_file = arg
		elif opt in ('--threads'):
			_threads = int(arg)
		elif opt in ('-p','--plugin'):
			_plugin = arg
		elif opt in ('--plugin-arg'):
			_plugin_arg = arg
		elif opt in ('-T','--target'):
			_target = arg
		elif opt in ('-l','--listen'):
			_listen = True
		elif opt in ('--max-size'):
			_maxsize = int(arg)
		elif opt in ('-c','--console'):
			_console = True
		else:
			pass

	# 控制台方式
	if _console:
		# print 'running console'
		cn = Consoler()
		cn.run()
		return

	if _server and _token:
		pass
	else:
		try:
			user = WebUser()
			if user.server and user.token:
				_server = user.server
				_token = user.token

			# init global var
			globalVar.server = _server
			globalVar.token = _token
			if _auto_proxy:
				ps = ProxyScraper()
				ps.proxies_get(1000)
				globalVar.proxyRequest.add_proxies(ps.format_proxie(type=1))

		except Exception,e:
			print 'Exception',e
			if e[0] == 'WebUser.loginfail':
				usage()
				return

	# pprint(globalVar.proxyRequest.proxies)
	# globalVar.proxyRequest

	# 其它方式
	if _server and _token:
		show()

		if _listen:
			# 监听模式
			li = Listener(server=_server, token=_token, loglevel=_vv, maxsize=_maxsize)
			li.run()
			return

		# update proxies
		if _update_proxy:
			ps = ProxyScraper()
			ps.scrap_proxies_1()
			ps.proxies_submit()
			return
		
		# update plugins
		if '_pluginpath' in dir() and _pluginpath:
			# print '_pluginpath=',_pluginpath
			# print '_server=',_server
			# print '_token=',_token
			loadPlugins(_pluginpath,_server,_token)
			return

		# update config
		if '_update_config' in dir() and _update_config:
			if '_conf_file' in dir() and os.path.isfile(_conf_file):
				pass

		if '_conf_file' in dir() and os.path.isfile(_conf_file):			
			# set global config
			config = json.load(open(_conf_file,'r'))
			config['global']['server'] = _server
			config['global']['token'] = _token
			if _target:
				config['global']['target'] = _target
				# 注意targetname直接在config的key,而不是config['global']的key
				# 参考dist_hi.php
				config['targetname'] = genTargetName(_target)
			else:
				_target = config['global']['target']
			if _threads:
				config['global']['threads'] = _threads
			else:
				 _threads = config['global']['threads']
			if _vv:
				config['global']['loglevel'] = _vv
			else:
				_vv = config['global']['loglevel']
			if _gather_depth:
				config['global']['gatherdepth'] = _gather_depth
			else:
				_gather_depth = config['global']['gatherdepth']

			globalVar.config = dict(config)	
			conffile = 'cache/conf/' + genFileName_v2(_target) + '.json'
			json.dump(globalVar.config,open(conffile,'w'))
		

			if '_plugin' in dir() and _plugin:
				# 单插件模式
				# plugin type scan
				sn = PluginMultiRunner(server=_server,token=_token,target=_target,loglevel=_vv,threads=_threads,pluginfilepath=_plugin,pluginargs=_plugin_arg)
				sn.initInfo()
				sn.scan()
			else:
				# 自收集模式
				sn = Scanner(conffile=conffile)
				sn.safeRun()
				#  sn.initInfo()
				# sn.infoGather()
				# sn.scan()

	else:
		usage()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()