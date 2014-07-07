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
	def __init__(self, pluginpath=None):
		super(PluginLoader, self).__init__()
		if pluginpath == None:
			pluginpath = os.path.dirname(__file__)[:-3] +'plugins'
		if pluginpath[-1] =='/':
			pluginpath = pluginpath[:-1]
		self.path = pluginpath
		#print self.path
		if self.path not in sys.path:
			sys.path.append(sys.path)

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
				if eachfile != '__init__.py' and '.pyc' not in eachfile:
					ret[root].append(eachfile)

		self.plugindict = ret
		print self.plugindict

	def runEachPlugin(self,pluginfilepath,services):
		print '>>>running plugin:',pluginfilepath
		if os.path.basename == '__init__.py':
			return
		modulepath = pluginfilepath.replace(self.path+'/','')
		modulepath = modulepath.replace('.py','')
		modulepath = modulepath.replace('.','')
		modulepath = modulepath.replace('/','.')
		#print modulepath

		importcmd = 'from ' + modulepath + ' import *'
		exec(importcmd)
		#print importcmd
		#print os.getcwd()
		
		if locals().has_key('Scan'):
			print '\tPlugin function Assign loaded'
			Scan(services)
		if locals().has_key('Audit'):
			print '\tPlugin function Audit loaded'
			tmp = Audit(services)
			self.retinfo.append(tmp)


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

	def runPlugins(self,services):
		# find auxiliary path and 
		for path in self.plugindict:
			if path[-9:]=='auxiliary':
				auxpath = path
				break
		# step1: run auxiliary plugins
		for eachfile in self.plugindict[auxpath]:
			self.runEachPlugin(auxpath+'/'+eachfile,services)

		# step2: run other plugins
		for path in self.plugindict:
			if path != auxpath:
				for eachfile in self.plugindict[path]:
					self.runEachPlugin(path+'/'+eachfile,services)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	pl = PluginLoader()
	print pl.loadPlugins()
	services={}
	pl.runPlugins(services)