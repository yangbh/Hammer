#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import re
import time
import copy
import urllib2
import socket
import multiprocessing
import multiprocessing.pool
import ipaddress
import logging

import globalVar
# from globalVar import mainlogger

from pprint import pprint
from pluginLoader_class import PluginLoader
from spider.domain import GetFirstLevelDomain
from webInterface_class import WebInterface
from dummy import *

'''
这是一个scan基类
你可以重写BasicScanner的setTasks函数
'''
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def procFunc(pluginheader,pluginfilepath):
	try:
		if type(pluginheader) == PluginLoader:
			pl = pluginheader
			globalVar.mainlogger.info('pluginfilepath=%s' % pluginfilepath)
			globalVar.mainlogger.info('service=%s' % str(pl.services))
			pl.runAudit(pluginfilepath)
			globalVar.mainlogger.debug('returnning pl')			

			return pl.services
		else:
			globalVar.mainlogger.error('pl is not a pluginLoader_class.PluginLoader class')
			return None
	except (KeyboardInterrupt, SystemExit):
		globalVar.mainlogger.info('Exiting...')
		return None
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)

# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
class PluginMultiRunner(object):
	"""docstring for Scanner"""
	def __init__(self,server=None,token=None,target=None,pluginfilepath=None,pluginargs=None,threads=None,loglever='INFO'):
		super(PluginMultiRunner, self).__init__()
		self.server = server
		self.token = token
		self.target = target
		self.pluginfilepath = BASEDIR +'/' +pluginfilepath
		self.pluginargs = pluginargs
		if threads and type(threads) == int:
			self.threads = int(threads)
		else:
			self.threads = multiprocessing.cpu_count()

		self.args = {'server':self.server,'target':self.target,'loglevel':self.loglevel,'threads':self.threads}

		# web接口
		self.web_interface = None
		if server and token:
			self.web_interface = WebInterface(server,token)
		# 任务
		self.services = []
		# 扫描结果
		self.result = {}
		# pluginLoaders
		
		self.pls = []

		# log 模块
		globalVar.mainlogger = logging.getLogger('main')
		if loglever == 'DEBUG':
			globalVar.mainlogger.setLevel(logging.DEBUG)
		else:
			globalVar.mainlogger.setLevel(logging.INFO)

		# 定义handler的输出格式formatter    
		# formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')  
		formatter1 = logging.Formatter('[%(process)d] - [%(levelname)s] - %(message)s')  
		formatter2 = logging.Formatter('%(message)s')  
		# 创建一个handler，用于写入日志文件  
		filepath = BASEDIR+'/output/scan.log'
		if os.path.isfile(filepath):
			os.remove(filepath)
		fh = logging.FileHandler(filepath,'a')    
		# 再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler()  

		fi = logging.Filter('main')

		fh.addFilter(fi)
		ch.addFilter(fi)

		fh.setFormatter(formatter1)
		ch.setFormatter(formatter1)

		globalVar.mainlogger.addHandler(fh)
		globalVar.mainlogger.addHandler(ch)

		globalVar.mainlogger.info('[*] Start an new scan')
		globalVar.mainlogger.info('\tserver  =%s' % server)
		globalVar.mainlogger.info('\ttoken    =%s' % token)
		globalVar.mainlogger.info('\ttarget  =%s' % target)
		globalVar.mainlogger.info('\tthreads=%d' % self.threads)
	
	def _getServiceType(self,target):
		m = re.search('(http[s]?)://([^:^/]+):?([^/]*)/?',target)
		if m:
			return 'url'
		else:
			m = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',target)
			if m:
				return 'ip'
			else:
				return 'host'

	def _noticeStartToWeb(self):
		''' '''
		# print '>>notice server start scan'
		globalVar.mainlogger.info('Notice server start scan')
		if self.web_interface == None:
			# print'server not exists'
			globalVar.mainlogger.error('\tserver not exists')
			return False
		#	save Scan table at first
		# print 'self.target\t',self.target
		self.web_interface.task_start(self.target,self.target)
			
	def _initGlobalVar(self):
		# process information
		# print 'in scaner_class_mp process pid=\t',os.getpid()
		# print 'id(globalVar)=\t',id(globalVar)
		# print globals()
		pid = os.getpid()
		globalVar.scan_task_dict_lock.acquire()
		globalVar.scan_task_dict['pid'] = pid
		globalVar.scan_task_dict['target'] = self.target
		globalVar.scan_task_dict['server'] = self.web_interface.server
		globalVar.scan_task_dict['token'] = self.web_interface.token
		globalVar.scan_task_dict['subtargets'] = {}
		globalVar.scan_task_dict['scanID'] = self.web_interface.id
		globalVar.scan_task_dict_lock.release()

	def _saveResultToWeb(self):
		globalVar.mainlogger.info('Saving scan result to server')
		if self.web_interface == None:
			globalVar.mainlogger.error('\tserver not exists')
			return False
		else:
			self.web_interface.task_end()

	def initInfo(self,target=None):
		try:
			#	Step 1
			globalVar.mainlogger.info('[*][*] Step1: init starting info')
			
			if target==None:
				target = self.target
			
			targets = []
			# file type target
			if os.path.isfile(target):
				for eachLine in f:
					eachLine = eachLine.replace('\r','')
					eachLine = eachLine.replace('\n','')
					targets.append(eachLine)
			
			# ip range type
			else:
				m = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,2})?$',target)
				if m:
					ipnet = list(ipaddress.ip_network(unicode(target)).hosts())
					for eachipad in ipnet:
						targets.append(eachipad.compressed)
				else:
					targets.append(target)
		
			argdict = {}
			if self.pluginargs:
				pluginargs = self.pluginargs.split(';')
				for eacharg in pluginargs:
					if '=' in eacharg:
						exec(eacharg)
						eacharg = eacharg.split('=')
						argdict[eacharg[0]] = eval(eacharg[0])
				globalVar.mainlogger.debug('argdict=%s' % str(argdict))

			for each_target in targets:
				service = {'mode':'nogather'}
				service_type = self._getServiceType(each_target)
				service[service_type] = each_target
				if len(argdict):
					service.update(argdict)
				self.services.append(service)

			globalVar.mainlogger.info('Targets:')
			for service in self.services:
				globalVar.mainlogger.info('\t'+str(service))

			self._noticeStartToWeb()
			self._initGlobalVar()
		except IndexError,e:
		# except Exception,e:
			globalVar.mainlogger.error('Exception:'+str(e))

	def scan(self):
		''' '''
		try:
			globalVar.mainlogger.info('[*][*] Step3: run each sub task')
			
			proPool = MyPool(self.threads)

			for each_service in self.services:
				pl = PluginLoader(None,each_service,self.target)
				proPool.apply_async(procFunc,(pl,self.pluginfilepath))

			# 改用map_async的方式
			# proPool = multiprocessing.Pool(10)
			# proPool = MyPool(multiprocessing.cpu_count())
			# p = proPool.map_async(procFunc,self.pls)
			proPool.close()
			try:
				proPool.join()
			except KeyboardInterrupt,e:
				globalVar.mainlogger.error('Caught KeyboardInterrupt, terminating workers')

			globalVar.mainlogger.info('[*] All Done')
			self._saveResultToWeb()

		except IndexError,e:
		# except Exception,e:
			globalVar.mainlogger.error('Exception:'+str(e))

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	# server = '0xff.sinaapp.com/web/'
	server = 'www.hammer.org'
	token = 'dqc8mcv6ukaso3fsj1qvujss06'

	target = 'http://www.leesec.com'
	sn = PluginMultiRunner(_server,_token,_target,_plugin,_plugin_arg)
	sn.initInfo()
	sn.scan()