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


BASEDIR = __file__.replace('/lib/dummy.pyc','')
BASEDIR = BASEDIR.replace('/lib/dummy.py','')

LIBDIR = BASEDIR + '/lib'
PLUGINDIR = BASEDIR + '/plugins'
# CACHEDIR = BASEDIR + '/cache'

# system path
if BASEDIR not in sys.path:
	sys.path.append(BASEDIR)
if LIBDIR not in sys.path:
	sys.path.append(LIBDIR)
if PLUGINDIR not in sys.path:
	sys.path.append(PLUGINDIR)