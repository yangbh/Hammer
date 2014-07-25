#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

BASEDIR = __file__.replace('/lib/crawler/dummy.pyc','')
BASEDIR = BASEDIR.replace('/lib/crawler/dummy.py','')

LIBDIR = BASEDIR + '/lib'
PLUGINDIR = BASEDIR + '/plugins'
CACHEDIR = BASEDIR + '/cache'

# system path
sys.path.append(BASEDIR)
sys.path.append(LIBDIR)
sys.path.append(PLUGINDIR)