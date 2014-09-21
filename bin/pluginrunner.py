#!/usr/bin/python2.7
#coding:utf-8

import os
import sys
from dummy import BASEDIR,PLUGINDIR,LIBDIR
sys.path.append(BASEDIR)
sys.path.append(LIBDIR)
from lib.pluginLoader_class import PluginLoader

def useage():
	print '\texample: python pluginrunner.py plugins/'
	sys.exit(1)

def main():
	#print sys.argv
	#print os.getcwd()
	if len(sys.argv) != 2:
		useage()

	pluginpath = sys.argv[1]
	if pluginpath[0] == '/':
		pass
	else:
		pluginpath = os.getcwd() + '/' + pluginpath
	print 'pluginpath:\t',pluginpath

	code = 'info={};services={};' + os.linesep
	fp = open(pluginpath,'r')
	code += fp.read()
	fp.close()
	
	print code
	exec(code)

	print 'info=\t',info
	print 'services=\t',services
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()