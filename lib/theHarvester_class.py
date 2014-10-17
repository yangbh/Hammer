#!/usr/bin/python2.7
#coding:utf-8

from dummy import LIBDIR
import sys

sys.path.append(LIBDIR+'/theHarvester')
sys.path.append(LIBDIR+'/theHarvester/lib')

from discovery import *
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class TheHarvester(object):
	"""docstring for TheHarvester"""
	def __init__(self, arg):
		super(TheHarvester, self).__init__()
		self.arg = arg

	def getSubDomains(self,word,engine='baidu',limit=100,start=0):
		if engine == "google":
			print "[-] Searching in Google:"
			search=googlesearch.search_google(word,limit,start)
			search.process()
			#all_emails=search.get_emails()
			all_hosts=search.get_hostnames()
		if engine == "baidu":
			print "[-] Searching in Baidu:"
			search=baidusearch.search_baidu(word,limit,start)
			search.process()
			#all_emails=search.get_emails()
			all_hosts=search.get_hostnames()

		print all_hosts
		return all_hosts
