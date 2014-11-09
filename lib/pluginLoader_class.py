#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import globalVar
from dummy import BASEDIR
from pprint import pprint

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class PluginLoader(object):
	"""docstring for PluginLoader"""
	def __init__(self, pluginpath=None, services = None,outputpath=''):
		super(PluginLoader, self).__init__()
		if pluginpath == None:
			pluginpath = BASEDIR +'/plugins'
		self.path = pluginpath
		# print 'self.path=',self.path

		self.services = services

		self.plugindict = {}
		self.retinfo = []
		self.output = ''

		# output file
		outputpath = outputpath.replace('://','_')
		outputpath = outputpath.replace('/','')

		if services.has_key('ip'):
			self.outputfile = BASEDIR + '/output/' + outputpath + '/' + services['ip']
		elif services.has_key('url'):
			threadName = services['url']
			tmpurl = threadName.replace('://','_')
			tmpurl = tmpurl.replace(':','_')
			tmpurl = tmpurl.replace('/','')
			self.outputfile = BASEDIR + '/output/' + outputpath + '/' + tmpurl
		elif services.has_key('host'):
			self.outputfile = BASEDIR + '/output/' + outputpath + '/' + services['host']

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

			elif self.services.has_key('url'):
				tmp += '*'*25 + '     scan info     '+ '*'*25 + os.linesep
				tmp += '# this is a http type scan' + os.linesep
				tmp += 'url:\t' + self.services['url'] + os.linesep
			
			elif self.services.has_key('host'):
				tmp += '*'*25 + '     scan info     '+ '*'*25 + os.linesep
				tmp += '# this is an host type scan'  + os.linesep
				tmp += 'host:\t' + self.services['host'] + os.linesep

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

	def _initSubProcess(self):
		# sub porcess information
		pid = os.getpid()
		# parent process information
		ppid = os.getppid()
		# print 'pid=\t',os.getpid()
		tmpdict = {}
		tmpdict['pid'] = pid
		tmpdict['ppid'] = ppid
		tmpdict['target'] = self.services
		try:
			# only sub process scan will invovied in scan_task_dict
			if self.services.has_key('noSubprocess') and self.services['noSubprocess'] == True:
				pass
			else:
				# globalVar.scan_task_dict_lock.acquire()
				print 'in pluginLoader porcess pid=\t',os.getpid()
				print 'id(globalVar)=\t',id(globalVar)
				globalVar.scan_task_dict['subtargets'] = tmpdict
				pprint(globalVar.scan_task_dict)
				# globalVar.scan_task_dict_lock.release()
		except Exception,e:
			print 'Exception',e

	def _getPluginInfo(self,pluginfilepath):
		# print '>>>running plugin:',pluginfilepath
		modulepath = pluginfilepath.replace(BASEDIR+'/plugins/','')
		modulepath = modulepath.replace('.py','')
		modulepath = modulepath.replace('.','')
		modulepath = modulepath.replace('/','.')


		importcmd = 'from ' + modulepath + ' import info'
		# importcmd += '\nprint info'
		# exec_code = compile(importcmd,'','exec')
		# importcmd = 'from temp.explugin import Audit'
		# print 'importcmd=',importcmd
		# print sys.path
		exec(importcmd)

		# print info
		return info
		# info = {
		# 	'NAME':'Port and Service Discover',
		# 	'AUTHOR':'yangbh',
		# 	'TIME':'20140707',
		# 	'WEB':'',
		# 	'DESCRIPTION':'端口扫描',
		# 	'VERSION':'1.0',
		# 	'RUNLEVEL':0
		# }
		# return info

	def loadPlugins(self, path=None):
		self._initSubProcess()
		#print '>>>loading plugins'
		self.output = '>>>loading plugins'  + os.linesep
		if path == None:
			path = self.path
		ret = {}
		for root, dis, files in os.walk(path):  
			ret[root] =[]
			for eachfile in files:
				if eachfile != '__init__.py' and '.pyc' not in eachfile and eachfile != 'dummy.py' and eachfile.endswith('.py'):
					ret[root].append(eachfile)

		self.plugindict = ret
		# print self.plugindict
		self.output += str(self.plugindict) + os.linesep*2

	def runEachPlugin(self, pluginfilepath, services=None):
		try:
			print '>>>running plugin:',pluginfilepath
			self.output += '>>>running plugin:' + pluginfilepath  + os.linesep
			
			# init globalVar
			plugininfo = self._getPluginInfo(pluginfilepath)
			# pprint(plugininfo)
			pluginname = plugininfo['NAME']
			# globalVar.plugin_now_lock.acquire()
			globalVar.plugin_now = pluginname
			# print id(globalVar)
			# pprint(globalVar.plugin_now)
			# globalVar.plugin_now_lock.release()

			if services == None:
				services = dict(self.services)

			modulepath = pluginfilepath.replace(BASEDIR+'/plugins/','')
			modulepath = modulepath.replace('.py','')
			modulepath = modulepath.replace('.','')
			modulepath = modulepath.replace('/','.')
			# print modulepath

			#from dummy import *
			importcmd = 'global services' + os.linesep
			# importcmd += 'import globalVar' + os.linesep
			# print '1id(globalVar)=',id(globalVar)
			# importcmd += 'from common import genFilename,security_note,security_info,security_warning,security_hole' + os.linesep
			#importcmd += 'from dummy import *' + os.linesep
			importcmd += 'from ' + modulepath + ' import Audit,info'

			# print 'importcmd=',importcmd
			exec(importcmd)

			# print 'in running plugin'
			# print 'plugin pid=\t',os.getpid()
			# print 'id(globalVar)=\t',id(globalVar)
			# print 'globalVar.scan_task_dict=\t',globalVar.scan_task_dict
			if locals().has_key('Audit'):
				# MAudit = copy.copy(Audit)
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
		except IndexError,e:
		# except Exception,e:
			print 'Exception',e

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


		# for test
		# path1 = BASEDIR + '/plugins/Info_Collect'
		# path2 = BASEDIR + '/plugins/System'
		# self.plugindict = {path1:['whatweb.py'],path2:['iisshort.py']}

		for path in self.plugindict:
			if path[-12:]=='Info_Collect':
				auxpath = path
				break

		self._saveRunningInfo(os.linesep+'Step 1. Running Auxiliary Plugins'+os.linesep*2)
		# step1: run auxiliary plugins
		if self.services.has_key('alreadyrun') and self.services['alreadyrun'] == True:
			pass
		else:
			for eachfile in self.plugindict[auxpath]:
				self.runEachPlugin(auxpath+'/'+eachfile)

		self._saveRunningInfo(os.linesep+'Step 2. Running Other Plugins'+os.linesep*2)
		# step2: run other plugins
		for path in self.plugindict:
			if path != auxpath:
				for eachfile in self.plugindict[path]:
					self.runEachPlugin(path+'/'+eachfile)

		self._saveRunningInfo(isret=True)

def main():
	basedir = '/Users/mody/study/Python/Hammer'
	sys.path.append(basedir)
	sys.path.append(basedir+'/lib')
	services={'url':'http://www.leesec.com'}
	pl = PluginLoader(None,services)
	pl.path = basedir+'/plugins'
	pl.runEachPlugin(basedir+'/plugins/Info_Collect/portscan.py',services)
	# pl.runEachPlugin(basedir+'/plugins/Sensitive_Info/backupfile.py',services)
	
	# print pl.loadPlugins()
	# pl.runPlugins()
	# print pl.retinfo
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	import multiprocessing
	p = multiprocessing.Pool()
	p.apply_async(main)
	p.close()
	p.join()
