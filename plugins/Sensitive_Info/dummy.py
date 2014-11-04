#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

BASEDIR = os.path.realpath(__file__).replace('/plugins/Sensitive_Info/dummy.pyc','')
BASEDIR = BASEDIR.replace('/plugins/Sensitive_Info/dummy.py','')

LIBDIR = BASEDIR + '/lib'
# PLUGINDIR = BASEDIR + '/plugins'
# CACHEDIR = BASEDIR + '/cache'

# system path
if BASEDIR not in sys.path:
	sys.path.append(BASEDIR)
if LIBDIR not in sys.path:
	sys.path.append(LIBDIR)

from pprint import pprint

from common import genFilename,security_note,security_info,security_warning,security_hole

from lib.ruleFile_class import RuleFile
# from lib.nmap_class import NmapScanner
# from lib.neighborHost_class import NeighborHost
# from lib.knock_class import SubDomain
# from lib.theHarvester_class import TheHarvester
# from lib.whatWeb_class import WhatWeb
from lib.spider.domain import GetFirstLevelDomain
from lib.crawler.crawlerFile import CrawlerFile