#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

BASEDIR = os.path.realpath(__file__).replace('/plugins/Info_Collect/dummy.pyc','')
BASEDIR = BASEDIR.replace('/plugins/Info_Collect/dummy.py','')

LIBDIR = BASEDIR + '/lib'
# PLUGINDIR = BASEDIR + '/plugins'
# CACHEDIR = BASEDIR + '/cache'

# system path
if BASEDIR not in sys.path:
	sys.path.append(BASEDIR)
if LIBDIR not in sys.path:
	sys.path.append(LIBDIR)

from pprint import pprint

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# very important
# here it is common, not lib.common, because of python import strategies
from common import genFilename,security_note,security_info,security_warning,security_hole,add_target
from common import logger
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from lib.nmap_class import NmapScanner
from lib.neighborHost_class import NeighborHost
# from lib.knock_class import SubDomain
from lib.theHarvester_class import TheHarvester
from lib.whatWeb_class import WhatWeb
# print 'yeah2'
#from lib.spider.spider import Spider,Strategy,UrlObj
try:
	from lib.crawler.crawler import Crawler,Strategy
except Exception,e:
	print Exception,e
	sys.exit(2)
# print 'yeah1'
from lib.spider.domain import GetFirstLevelDomain