#!/usr/bin/python2.7
#coding:utf-8

import os
import readline
import logging

import globalVar

from dummy import BASEDIR
from consoleCache_class import Cache
from consoleTab_class import Completer

class Consoler(object):
	"""docstring for Consoler"""
	def __init__(self,loglevel='WARNING'):
		super(Consoler, self).__init__()
		self.cache = Cache()
		self.cache.start()

		commands = ['help','exit','cls','set','connect','show','search','use',
				'back', 'cls', 'info','opts','run']
		comp = Completer(commands)
		# we want to treat '/' as part of a word, so override the delimiters
		readline.set_completer_delims(' \t\n;')
		readline.parse_and_bind("tab: complete")
		readline.set_completer(comp.complete)

		self.loghandler = []
		# log 模块,确保赋值一次
		if globalVar.mainlogger is None:
			globalVar.mainlogger = logging.getLogger('root')
			if loglevel == 'DEBUG':
				globalVar.mainlogger.setLevel(logging.DEBUG)
			elif loglevel == 'WARNING':
				globalVar.mainlogger.setLevel(logging.WARNING)
			else:
				globalVar.mainlogger.setLevel(logging.INFO)

			#	logging handler
			formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')  
			# 创建一个handler，用于写入日志文件  
			# filepath = BASEDIR+'/output/console.log'
			# if os.path.isfile(filepath):
				# os.remove(filepath)
			# fh = logging.handlers.RotatingFileHandler(filepath,maxBytes=10*1024*1024,backupCount=5)    
			# 再创建一个handler，用于输出到控制台
			ch = logging.StreamHandler()  
			
			fi = logging.Filter('')

			# fh.addFilter(fi)
			ch.addFilter(fi)

			# fh.setFormatter(formatter)
			ch.setFormatter(formatter)

			self.loghandler.append(ch)
			# self.loghandler.append(fh)

			self._initLogging()

		globalVar.mainlogger.info('Start console mode')

	def _initLogging(self):
		# globalVar.mainlogger.info('before test')
		for handler in self.loghandler:
			globalVar.mainlogger.addHandler(handler)
		# globalVar.mainlogger.info('after test')
	
	def _removeLogging(self):
		# globalVar.mainlogger.info('before test')
		for handler in self.loghandler:
			globalVar.mainlogger.removeHandler(handler)
		# globalVar.mainlogger.info('after test')

	def run(self):
		try:
			while True:
				self.cache.printhammer()
				cmd=raw_input('>').strip()
				if   cmd == 'help':
					self.cache.mainhelp()
				elif cmd == 'exit':
					self.cache.mainexit()
				elif cmd == 'cls' :
					self.cache.cls()
				elif cmd == 'use':
					self.cache.usage("use")
				elif cmd == 'show':
					self.cache.usage("show")
				elif cmd == 'search':
					self.cache.usage("search")
				elif cmd == 'banner':
					self.cache.banner()
				elif cmd == 'set':
					self.cache.usage("set")
				elif cmd == 'connect':
					self.cache.connect()
				elif len(cmd.split(" ")) == 2:
					cnd = cmd.split(" ")
					c   = cnd[0]
					g   = cnd[1]
					if    c == 'search':
						if len(g)>0 and len(g.split(" "))>0:
							self.cache.search(g)
						else:
							self.cache.usage("search")
					elif  c == 'show':
						if   g in ['info','com','sens','sys','pwd','web','all']:
							self.cache.showplus(g)
						elif g == 'user':
							self.cache.showuser()
						else:
							self.cache.usage("show")
					elif  c == 'use':
						if len(g) > 0 or len(g.split(" ")) > 0:
							self.cache.load(g)
						else:
							self.cache.usage("use")
					elif  c == 'set':
						self.cache.usage('set')

				elif len(cmd.split(" ")) == 3:
					c,g1,g2 = cmd.split(" ")
					if c == 'set':
						self.cache.setconf(g1, g2)

				elif len(cmd) > 0:
					self.cache.execmd(cmd)
		except KeyboardInterrupt:
			self.cache.mainexit()
		except Exception,e:
			self.cache.errmsg(e)

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	cn = Consoler()
	cn.run()
