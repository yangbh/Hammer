#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

def getbasedir():
	cwd = os.getcwd()
	filepath = __file__
	print cwd
	print fil
	tmp = __file__.replace(cwd+'/','')
	tmp = cwd + tmp
	return os.path.dirname(tmp)


def getPortByService(services,scname):
	'''find ports by service name'''
	try:
		ret = []
		for eachport in services['port_detail'].keys():
			if services['port_detail'][eachport]['name'] == sc:
				ret.append(eachport)
				#break
		print ret
		return ret
	except KeyError,e:
		print 'KeyError:\t', e


BASEDIR = __file__.replace('/bin/dummy.pyc','')
BASEDIR = BASEDIR.replace('/bin/dummy.py','')

LIBDIR = BASEDIR + '/lib'
PLUGINDIR = BASEDIR + '/plugins'
CACHEDIR = BASEDIR + '/cache'

# system path
sys.path.append(BASEDIR)
sys.path.append(LIBDIR)
sys.path.append(PLUGINDIR)