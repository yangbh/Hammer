#!/usr/bin/python2.7
#coding:utf-8

import readline

from consoleTab_class import Completer
from consoleColor_class  import *
from consolePlugin_class import *

class Load(object):
	'''Load mst plugin'''
	def __init__(self,loglevel='WARNING'):
		super(Load, self).__init__()

		# commands = ['help', 'back', 'cls', 'info','opts', 'set', 'run']
		# comp = Completer(commands)
		# # we want to treat '/' as part of a word, so override the delimiters
		# readline.set_completer_delims(' \t\n;')
		# readline.parse_and_bind("tab: complete")
		# readline.set_completer(comp.complete)

	def start(self,plutype,pluname):
		try:
			mm=m("plugins/%s.py"%pluname)
			while 1:
				mm.printp(plutype,pluname)
				pcmd=raw_input('>').strip()
				if   pcmd == 'back' or pcmd == 'exit':
					break
				elif pcmd == 'help':
					mm.pluhelp()
				elif pcmd == 'cls':
					mm.cls()
				elif pcmd == 'info':
					mm.info()
				elif pcmd == 'opts':
					mm.opt()
				elif pcmd == 'run':
					mm.run()
				elif pcmd == 'load':
					mm.load()
				elif pcmd == 'set':
					color.cprint("[?] USAGE:set <PARAM> <VALUE>",YELLOW)
				elif len(pcmd.split(" "))==2:
					ptmp=pcmd.split(" ")
					if ptmp[0] == "load":
						if len(ptmp[0])>0 and len(ptmp[1])>0:
							execfile("plugins/load/%s.py"%ptmp[1])
				elif len(pcmd.split(" "))==3:
					ptmp=pcmd.split(" ")
					if ptmp[0] == "set":
						if len(ptmp[1])>0 and len(ptmp[2])>0:
							mm.setp(ptmp[1],ptmp[2])
		except KeyboardInterrupt:
			color.cprint("\n[!] CTRL+C EXIT !",RED)
		except Exception,e:
			color.cprint("[!] ERR:%s"%e,RED)


if __name__ == '__main__':
	print __doc__
else:
	load=Load()
