#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

BASEDIR = __file__.replace('/plugins/Web_Applications/dummy.pyc','')
BASEDIR = BASEDIR.replace('/plugins/Web_Applications/dummy.py','')

LIBDIR = BASEDIR + '/lib'
PLUGINDIR = BASEDIR + '/plugins'
CACHEDIR = BASEDIR + '/cache'

# system path
sys.path.append(BASEDIR)
sys.path.append(LIBDIR)
sys.path.append(PLUGINDIR)

from pprint import pprint

from lib.common import genFilename
# from lib.ruleFile_class import RuleFile
# from lib.nmap_class import NmapScanner
# from lib.neighborHost_class import NeighborHost
# from lib.knock_class import SubDomain
# from lib.theHarvester_class import TheHarvester
# from lib.whatWeb_class import WhatWeb
from lib.spider.domain import GetFirstLevelDomain
# from lib.crawler.crawlerFile import CrawlerFile