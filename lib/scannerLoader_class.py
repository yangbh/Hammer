#!/usr/bin/python2.7
#coding:utf-8

from scanner_class_basic import Scanner
from scanner_class_pluginrunner import PluginMultiRunner

class ScannerLoader(object):
	"""docstring for ScannerLoader"""
	def __init__(self, server, token, arg):
		super(ScannerLoader, self).__init__()
		self.server = server
		self.token = token
		self.arg = arg


	def run(self):
		try:
			# basic mode scanner
			if self.arg['mode'] == '1':
				sn = Scanner(server=self.server,token=self.token,\
					target=self.arg['target'],\
					threads=int(self.arg['global']['threads']) if self.arg['global']['threads']!= '' else None,\
					loglevel=self.arg['global']['loglevel'] if self.arg['global']['loglevel']!= '' else 'INFO',\
					gatherdepth=int(self.arg['global']['gatherdepth']) if self.arg['global']['gatherdepth']!= '' else 1)
				sn.initInfo()
				sn.infoGather()
				sn.scan()
			# plugin mode scanner
			elif self.arg['mode'] == '2':
				sn = PluginMultiRunner(server=self.server,token=self.token,\
					target=self.arg['target'],\
					threads=int(self.arg['global']['threads']) if self.arg['global']['threads']!= '' else None,\
					pluginfilepath=self.arg['pluginfilepath'],\
					pluginargs=self.arg['pluginargs'])
				sn.initInfo()
				sn.scan()
		except IndexError,e:
		# except Exception,e:
			print 'Exception',e

