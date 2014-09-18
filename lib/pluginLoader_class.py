#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
from dummy import BASEDIR
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class PluginLoader(object):
	"""docstring for PluginLoader"""
	def __init__(self, pluginpath=None, services = None,outputpath=''):
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

		# output file
		if outputpath == None or outputpath == '':
			self.outputfile = ''
		elif services.has_key('ip'):
			self.outputfile = BASEDIR + '/output/' + outputpath + '/' + services['ip']
		elif services.has_key('url'):
			threadName = services['url']
			tmpurl = threadName.replace('://','_')
			tmpurl = tmpurl.replace(':','_')
			tmpurl = tmpurl.replace('/','')
			self.outputfile = BASEDIR + '/output/' + outputpath + '/' + tmpurl
		else:
			self.outputfile = ''

	def _saveRunningInfo(self,info='',isinit=False,isret=False):
		''' '''
		if self.outputfile == '':
			return False
		# output basic iniformation
		if isinit == True:
			# check if path is exists first
			outputpath = os.path.dirname(self.outputfile)
			if os.path.isdir(outputpath) == False:
				# maybe should use os.makedirs
				try:
					os.makedirs(outputpath)
				except:
					pass

			tmp = info
			if self.services.has_key('ip'):
				tmp += '*'*25 + '     scan info     '+ '*'*25 + os.linesep
				tmp += '# this is an ip type scan'  + os.linesep
				tmp += 'ip:\t' + self.services['ip'] + os.linesep
				if self.services.has_key('issubdomain'):
					tmp +='issubdomain:\t' + 'True' + os.linesep
				else:
					tmp +='issubdomain:\t' + 'False' + os.linesep

			elif self.services.has_key('url'):
				tmp += '*'*25 + '     scan info     '+ '*'*25 + os.linesep
				tmp += '# this is a http type scan' + os.linesep
				tmp += 'url:\t' + self.services['url'] + os.linesep
				if self.services.has_key('isneighborhost'):
					tmp +='isneighborhost:\t' + 'True' + os.linesep
				else:
					tmp +='isneighborhost:\t' + 'False' + os.linesep
			
			tmp += os.linesep
			tmp += '*'*25 + '   scan services   '+ '*'*25 + os.linesep

			info = tmp
			fp = open(self.outputfile,'w')
			fp.write(info)
			fp.close()
			return True
		# output result
		if isret == True:
			tmp = info

			tmp += os.linesep
			tmp += '*'*25 + '    scan result    '+ '*'*25 + os.linesep
			tmp += 'retinfo:\t' + str(self.retinfo) + os.linesep*2
			tmp += 'services:\t' + str(self.services)
			info = tmp

		if info and info != '':
			fp = open(self.outputfile,'a')
			fp.write(info)
			fp.close()

		return True

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
		self.output += str(self.plugindict) + os.linesep*2

	def runEachPlugin(self, pluginfilepath, services=None):
		print '>>>running plugin:',pluginfilepath
		self.output += '>>>running plugin:' + pluginfilepath  + os.linesep
		
		if services == None:
			services = dict(self.services)

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
				self.output += 'services changed to:\t' + str(services) + os.linesep
			# return info
			if ret and ret != {}:
				#print 'pluginfilepath=\t',pluginfilepath
				ret['type'] = info['NAME']
				print 'ret=\t',ret
				self.retinfo.append(ret)

		# at last, save output infomation
		self._saveRunningInfo(self.output+os.linesep)
		# clear output
		self.output = ''

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
		self._saveRunningInfo(isinit=True)

		for path in self.plugindict:
			if path[-12:]=='Info_Collect':
				auxpath = path
				break

		self._saveRunningInfo(os.linesep+'Step 1. Running Auxiliary Plugins'+os.linesep*2)
		# step1: run auxiliary plugins
		for eachfile in self.plugindict[auxpath]:
			self.runEachPlugin(auxpath+'/'+eachfile)

		self._saveRunningInfo(os.linesep+'Step 2. Running Other Plugins'+os.linesep*2)
		# step2: run other plugins
		for path in self.plugindict:
			if path != auxpath:
				for eachfile in self.plugindict[path]:
					self.runEachPlugin(path+'/'+eachfile)

		self._saveRunningInfo(isret=True)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	basedir = '/root/workspace/Hammer'
	sys.path.append(basedir)
	sys.path.append(basedir+'/lib')
	services={'url':'http://www.eguan.cn'}
	pl = PluginLoader(None,services)
	pl.path = basedir+'/plugins'
	#pl.runEachPlugin('/root/workspace/Hammer/plugins/Info_Collect/spider.py',services)
	pl.runEachPlugin(basedir+'/plugins/Sensitive_Info/backupfile.py',services)
	
	# print pl.loadPlugins()
	# pl.runPlugins()
	# print pl.retinfo
