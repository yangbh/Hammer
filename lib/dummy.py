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

BASEDIR = __file__.replace('/lib/dummy.pyc','')
BASEDIR = BASEDIR.replace('/lib/dummy.py','')

LIBDIR = BASEDIR + '/lib'
PLUGINDIR = BASEDIR + '/plugins'
CACHEDIR = BASEDIR + '/cache'