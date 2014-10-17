#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

BASEDIR = __file__.replace('/lib/crawler/dummy.pyc','')
BASEDIR = BASEDIR.replace('/lib/crawler/dummy.py','')

LIBDIR = BASEDIR + '/lib'
# PLUGINDIR = BASEDIR + '/plugins'
# CACHEDIR = BASEDIR + '/cache'

# system path
if BASEDIR not in sys.path:
	sys.path.append(BASEDIR)
if LIBDIR not in sys.path:
	sys.path.append(LIBDIR)
