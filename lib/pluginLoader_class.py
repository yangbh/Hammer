#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import re
from dummy import PLUGINDIR
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class PluginLoader(object):
	"""docstring for PluginLoader"""
	def __init__(self, pluginpath=None, services = None):
		super(PluginLoader, self).__init__()
		if pluginpath == None:
			pluginpath = os.path.dirname(__file__)[:-3] +'plugins'
		if pluginpath[-1] =='/':
			pluginpath = pluginpath[:-1]
		self.path = pluginpath
		#print self.path
		if self.path not in sys.path:
			sys.path.append(sys.path)
		self.services = services

		self.plugindict = {}
		self.retinfo = []

	def loadPlugins(self, path=None):
		print '>>>loading plugins'
		if path == None:
			path = self.path
		ret = {}
		for root, dis, files in os.walk(path):  
			ret[root] =[]
			for eachfile in files:
				if eachfile != '__init__.py' and '.pyc' not in eachfile and eachfile != 'dummy.py':
					ret[root].append(eachfile)

		self.plugindict = ret
		print self.plugindict

	def runEachPlugin(self, pluginfilepath, services=None):
		if services == None:
			services = self.services

		print '>>>running plugin:',pluginfilepath
		# 1. do not execute __init__.py
		if os.path.basename(pluginfilepath) == '__init__.py':
			return

		modulepath = pluginfilepath.replace(self.path+'/','')
		modulepath = modulepath.replace('.py','')
		modulepath = modulepath.replace('.','')
		modulepath = modulepath.replace('/','.')
		#print modulepath

		importcmd = 'global services'
		importcmd += os.linesep+'from ' + modulepath + ' import *'


		exec(importcmd)

		
		if locals().has_key('Audit'):
			print '\tPlugin function Audit loaded'
			ret = Audit(services)
			if self.services != services:
				self.services = services
			if ret:
				ret['type'] = info['NAME']
				self.retinfo.append(ret)

		# fp = open(pluginfilepath)
		# code = fp.read()
		# fp.close()
		# #classname = os.path.basename(pluginfilepath)
		# tt = re.search('class(\s+)([^\(]*)\(',code)
		# classname = tt.group(2)

		# #code += os.linesep + "from dummy import *"
		# code += os.linesep +'tmp = ' + classname + '()'
		# code += os.linesep +'tmp.run(services)'
		# print code
		# execfile(pluginfilepath)

		# if 'security_info' in dir():
		# 	print security_info()
		# #del security_info

	def runPlugins(self, services=None):
		if services == None:
			services = self.services
		# find auxiliary path and 
		
		for path in self.plugindict:
			if path[-12:]=='Info_Collect':
				auxpath = path
				break

		# step1: run auxiliary plugins
		for eachfile in self.plugindict[auxpath]:
			self.runEachPlugin(auxpath+'/'+eachfile)

		# step2: run other plugins
		for path in self.plugindict:
			if path != auxpath:
				for eachfile in self.plugindict[path]:
					self.runEachPlugin(path+'/'+eachfile)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services={}
	pl = PluginLoader(None,services)
	print pl.loadPlugins()
	pl.runPlugins()
	print pl.retinfo