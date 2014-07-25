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
		self.output = ''

	def loadPlugins(self, path=None):
		#print '>>>loading plugins'
		self.output = '>>>loading plugins'  + os.linesep
		if path == None:
			path = self.path
		ret = {}
		for root, dis, files in os.walk(path):  
			ret[root] =[]
			for eachfile in files:
				if eachfile != '__init__.py' and '.pyc' not in eachfile and eachfile != 'dummy.py':
					ret[root].append(eachfile)

		self.plugindict = ret
		#print self.plugindict
		self.output += str(self.plugindict) + os.linesep

	def runEachPlugin(self, pluginfilepath, services=None):
		print '>>>running plugin:',pluginfilepath
		self.output += '>>>running plugin:' + pluginfilepath  + os.linesep
		
		if services == None:
			services = self.services

		modulepath = pluginfilepath.replace(self.path+'/','')
		modulepath = modulepath.replace('.py','')
		modulepath = modulepath.replace('.','')
		modulepath = modulepath.replace('/','.')
		#print modulepath

		#from dummy import *
		importcmd = 'global services' + os.linesep
		#importcmd += 'from dummy import *' + os.linesep
		importcmd += 'from ' + modulepath + ' import Audit,info'

		exec(importcmd)

		
		if locals().has_key('Audit'):
			#print '\tPlugin function Audit loaded'
			ret, output = ({},'')
			try:
				ret,output = Audit(services)
			except:
				pass
			# outputinfo
			if output != '' and output != None:
				self.output += output
			# services info
			if self.services != services:
				self.services = services
				#print 'services changed:\t', services
				self.output += 'services changed:\t' + str(services)
			# return info
			if ret and ret != {}:
				print 'ret=\t',ret
				print 'pluginfilepath=\t',pluginfilepath
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
	sys.path.append('/root/workspace/Hammer')
	sys.path.append('/root/workspace/Hammer/lib')
	services={'url':'http://www.hengtiansoft.com'}
	pl = PluginLoader(None,services)
	pl.path = '/root/workspace/Hammer/plugins'
	pl.runEachPlugin('/root/workspace/Hammer/plugins/Info_Collect/spider.py',services)
	# print pl.loadPlugins()
	# pl.runPlugins()
	# print pl.retinfo
