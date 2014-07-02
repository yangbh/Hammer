#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class PluginLoader(object):
	"""docstring for PluginLoader"""
	def __init__(self, pluginpath=None):
		super(PluginLoader, self).__init__()
		if pluginpath == None:
			pluginpath = '../plugins/'
		self.path = pluginpath
		self.plugindict = {}

	def loadPlugins(self, path=None):
		if path == None:
			path = self.path
		ret = {}
		for root, dis, files in os.walk(path):  
			ret[root] =[]
			for eachfile in files:
				if eachfile != '__init__.py':
					ret[root].append(eachfile)

		self.plugindict = ret

	def runEachPlugin(self,pluginfilepath):
		fp = open(pluginfilepath)
		code = fp.read()


	def runPlugins(self):
		for path in self.plugindict:
			for eachfile in self.plugindict[path]:	
				self.runEachPlugin(path+eachfile)

# ----------------------------------------------------------------------------------------------------
#

# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	pl = PluginLoader('../plugins/')
	print pl.loadPlugins()
