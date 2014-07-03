#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import re
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class PluginLoader(object):
	"""docstring for PluginLoader"""
	CURRENT_PATH=os.path.dirname(__file__)
	def __init__(self, pluginpath=None):
		super(PluginLoader, self).__init__()
		if pluginpath == None:
			pluginpath = CURRENT_PATH +'/' + '  ../plugins/'
		self.path = pluginpath
		self.plugindict = {}
		self.retinfo = {}

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

	def runEachPlugin(self,pluginfilepath,services):
		fp = open(pluginfilepath)
		code = fp.read()
		fp.close()
		#classname = os.path.basename(pluginfilepath)
		tt = re.search('class(\s+)([^\(]*)\(',code)
		classname = tt.group(2)

		#code += os.linesep + "from dummy import *"
		code += os.linesep +'tmp = ' + classname + '()'
		code += os.linesep +'tmp.run(services)'
		print code
		execfile(pluginfilepath)

		if 'security_info' in dir():
			print security_info()
		#del security_info

	def runPlugins(self,services):
		for path in self.plugindict:
			for eachfile in self.plugindict[path]:	
				self.runEachPlugin(path+'/'+eachfile,services)

# ----------------------------------------------------------------------------------------------------
#

# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	pl = PluginLoader('../plugins/')
	print pl.loadPlugins()
