#!/usr/bin/python2.7
#coding:utf-8
#
#	2015-03-22 
#		修复globalVar.undone_targets每次运行之后未复原，在多进程状态下没有影响，但是在多线程下却有
		
import os
import sys
import re
import time
import copy
import json
import urllib2
import socket
import multiprocessing
import multiprocessing.pool
# import ipaddress
import netaddr
import logging

import globalVar
# from globalVar import mainlogger

from pprint import pprint
from common import genFilename
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
def procFunc(pluginheader):
	try:
		if type(pluginheader) == PluginLoader:
			pl = pluginheader
			globalVar.mainlogger.info('\tSub Scan Start:\t'+pl.target)
			pl.loadPlugins()
			pl.runPlugins()
			globalVar.mainlogger.debug('returnning pl.services')			
			# return pl
			print pl.services
			return pl.services
		else:
			print 'pl is not a pluginLoader_class.PluginLoader class'
			return None
	except (KeyboardInterrupt, SystemExit):
		print "Exiting..."
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
class Scanner(object):
	"""docstring for Scanner"""
	def __init__(self,conffile):
		super(Scanner, self).__init__()
		config = json.load(open(conffile,'r'))
		pprint(config['global'])
		self.server = config['global']['server']
		self.token = config['global']['token']
		self.target = config['global']['target']
		self.threads = int(config['global']['threads']) if config['global']['threads']!= '' \
														and type(config['global']['threads']) == int \
													else multiprocessing.cpu_count()
		# print "config['global']['gatherdepth']=",config['global']['gatherdepth']
		self.gatherdepth = int(config['global']['gatherdepth']) if config['global']['gatherdepth']!= '' else 0
		# print 'self.gatherdepth=',self.gatherdepth
		self.loglevel = config['global']['loglevel'] if config['global']['threads'] == '' else 'INFO'
		self.args = {'loglevel':self.loglevel,'threads':self.threads,'gatherdepth':self.gatherdepth}

		# web接口
		self.web_interface = None
		if self.server and self.token:
			self.web_interface = WebInterface(self.server,self.token)
		# 任务
		self.services = []
		# 扫描结果
		self.result = {}
		# pluginLoaders
		
		self.pls = []

		self.loghandler = []

		# log 模块,确保赋值一次
		if globalVar.mainlogger is None:
			globalVar.mainlogger = logging.getLogger('main')
			if self.loglevel == 'DEBUG':
				globalVar.mainlogger.setLevel(logging.DEBUG)
			else:
				globalVar.mainlogger.setLevel(logging.INFO)

			#	logging handler
			formatter = logging.Formatter('[%(process)d] - [%(levelname)s] - %(message)s')  
			# 创建一个handler，用于写入日志文件  
			filepath = BASEDIR+'/output/log/' + genFilename(self.target) + '.log'
			if os.path.isfile(filepath):
				os.remove(filepath)
			fh = logging.FileHandler(filepath,'a')    
			# 再创建一个handler，用于输出到控制台
			ch = logging.StreamHandler()  
			
			fi = logging.Filter('main')

			fh.addFilter(fi)
			ch.addFilter(fi)

			fh.setFormatter(formatter)
			ch.setFormatter(formatter)

			self.loghandler.append(ch)
			self.loghandler.append(fh)

			self._initLogging()

		globalVar.mainlogger.info('[*] Start a new scan')
		globalVar.mainlogger.info('\tserver\t=%s' % self.server)
		globalVar.mainlogger.info('\ttoken\t=%s' % self.token)
		globalVar.mainlogger.info('\ttarget\t=%s' % self.target)
		globalVar.mainlogger.info('\tthreads\t=%d' % self.threads)

		# 注意：不能通过以下的方式进行清空
		# globalVar.undone_targets = []
		tmpundone = copy.deepcopy(globalVar.undone_targets)
		for each_target in tmpundone:
			globalVar.undone_targets.remove(each_target)		

	def _initLogging(self):
		# globalVar.mainlogger.info('before test')
		for handler in self.loghandler:
			globalVar.mainlogger.addHandler(handler)
		# globalVar.mainlogger.info('after test')
	
	def _removeLogging(self):
		# globalVar.mainlogger.info('before test')
		for handler in self.loghandler:
			globalVar.mainlogger.removeHandler(handler)
		# globalVar.mainlogger.info('after test')
		globalVar.mainlogger = None

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
		self.web_interface.task_start(self.target,str(self.args))
			
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
		# print '>>>saving scan result to server'
		globalVar.mainlogger.info('Saving scan result to server')
		if self.web_interface == None:
			globalVar.mainlogger.error('\tserver not exists')
			# print'server not exists'
			return False
		else:
			self.web_interface.task_end()

	def initInfo(self,target=None):
		try:
			#	Step 1
			globalVar.mainlogger.info('[*][*] Step1: init starting info')
			self.services = []
			if target==None:
				target = self.target
			targets = []
			for each_target in target.split('\n'):
				# if each_target:
				# 	m = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$',each_target)
				# 	if m:
				# 		ipnet = list(netaddr.IPNetwork(each_target))
				# 		for eachip in ipnet:
				# 			targets.append(eachip.format())
				# 	elif re.match('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',each_target)	\
				# 		or re.match('(http[s]?)://([^:^/]+):?([^/]*)/?',each_target)	\
				# 		or re.match('(?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$',each_target):
				# 		targets.append(each_target)
				if each_target:
					# ip range type
					m = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$',each_target)
					if m:
						ipnet = list(netaddr.IPNetwork(each_target))
						for eachip in ipnet:
							targets.append(eachip.format())
					else:
						# one ip
						m = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',each_target)
						if m:
							targets.append(each_target)

						else:
							# url type
							m = re.match('(http[s]?)://([^:^/]+):?([^/]*)/?',each_target)
							if m:
								http_type = m.group(1)
								# print m.group(2)
								n = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,2})?$',m.group(2))
								# ip
								if n:
									# print 'is an ip type url'
									ip = m.group(2)
									if each_target[-1] == '/':
										each_target = each_target[:-1]
									targets.append(ip)
									targets.append(each_target)
								else:
									host = m.group(2)
									ports = m.group(3)
									# print host
									ip = socket.gethostbyname(host)
									domain = GetFirstLevelDomain(host)
									# print 'ip=',ip
									if each_target[-1] == '/':
										each_target = each_target[:-1]
									targets.append(ip)
									targets.append(each_target)
									targets.append(domain)
							else:
								# host type
								domain = GetFirstLevelDomain(each_target)
								targets.append(domain)

			#	去重
			targets = list(set(targets))

			# for each_target in globalVar.undone_targets:
			for each_target in targets:
				globalVar.undone_targets.append(each_target)
				service = {}
				service_type = self._getServiceType(each_target)
				# print service_type
				service[service_type] = each_target
				self.services.append(service)

			print 'globalVar.undone_targets=',globalVar.undone_targets
			print 'self.services=',
			pprint(self.services)
			globalVar.mainlogger.info('Targets:')
			for service in self.services:
				globalVar.mainlogger.info('\t'+str(service))

			self._noticeStartToWeb()
			self._initGlobalVar()
		except IndexError,e:
		# except Exception,e:
			globalVar.mainlogger.error('Exception:'+str(e))

	def infoGather(self,depth=None):
		print 'self.gatherdepth=',self.gatherdepth
		if depth == None:
			depth = self.gatherdepth
		try:
			#	Step 2
			globalVar.mainlogger.info('[*][*] Step2: gathing info')
			
			self.services = []
			for i in range(depth):
				globalVar.mainlogger.info('[*][*][-] >>> depth: %d <<<' % i)
				# print globalVar.done_targets
				# print 'id(globalVar.undone_targets)=\t',id(globalVar.undone_targets)

				globalVar.depth_now = globalVar.depth_now + 1

				if globalVar.undone_targets:
					# Step1: 
					services = []
					pls = []
					# print globalVar.undone_targets
					tmpundone = copy.deepcopy(globalVar.undone_targets)
					for each_target in tmpundone:
						# print tmpundone
						# print each_target
						service = {}
						service_type = self._getServiceType(each_target)
						# print service_type
						if globalVar.depth_now > self.gatherdepth:
							service['nogather'] = True
						service[service_type] = each_target
						services.append(service)

						globalVar.target_lock.acquire()
						globalVar.undone_targets.remove(each_target)
						globalVar.done_targets.append(each_target)
						globalVar.target_lock.release()

					# pprint(services)
					# sys.exit()
					for each_service in services:
						pl = PluginLoader(BASEDIR+'/plugins/Info_Collect',each_service,'_'+self.target)
						pls.append(pl)

					# globalVar.target_lock.acquire()
					# globalVar.done_targets += globalVar.undone_targets
					# globalVar.undone_targets = []
					# globalVar.target_lock.release()

					# Step2:
					results = []
					# 改用map_async的方式
					# proPool = multiprocessing.Pool(10)
					proPool = MyPool(self.threads)
					p = proPool.map_async(procFunc,pls)
					proPool.close()
					try:
						proPool.join()
					except KeyboardInterrupt,e:
						print "Caught KeyboardInterrupt, terminating workers"

					results = p.get()
					
					for service in results:
						# print service
						service['alreadyrun'] = True
						self.services.append(service)

				print 'globalVar.undone_targets=',globalVar.undone_targets
				print 'self.services=',
				pprint(self.services)


			for each_target in globalVar.undone_targets:
				print each_target
				service = {}
				service_type = self._getServiceType(each_target)
				# print service_type
				service[service_type] = each_target
				service['nogather'] = True
				self.services.append(service)

			globalVar.mainlogger.info('Targets:')
			for service in self.services:
				globalVar.mainlogger.info('\t'+str(service))

		except IndexError,e:
		# except Exception,e:
			globalVar.mainlogger.error('Exception:'+str(e))

	def scan(self):
		''' '''
		try:
			#	Step 3
			globalVar.mainlogger.info('[*][*] Step3: run each sub task')
			
			# globalVar.undone_targets = []
			print 'globalVar.undone_targets=',globalVar.undone_targets
			print 'self.services=',
			pprint(self.services)

			self.pls = []
			for each_service in self.services:
				pl = PluginLoader(None,each_service,self.target)
				self.pls.append(pl)

			results = []

			# 改用map_async的方式
			# proPool = multiprocessing.Pool(10)
			proPool = MyPool(self.threads)
			p = proPool.map_async(procFunc,self.pls)
			proPool.close()
			try:
				proPool.join()
			except KeyboardInterrupt,e:
				# print "Caught KeyboardInterrupt, terminating workers"
				# while True:
				# print '---------->>hahahaha main thread caught ctrl+c'
				globalVar.mainlogger.error('Caught KeyboardInterrupt, terminating workers')

			globalVar.mainlogger.info('[*] All Done')
			# # 改用map_async的方式
			# proPool = MyPool(10)
			# p = proPool.map_async(procFunc,self.pls)
			# try:
			# 	results = p.get()
			# except KeyboardInterrupt,e:
			# 	# proPool.terminate()
			# 	print "Caught KeyboardInterrupt, terminating workers"
			# proPool.terminate()

			# newpls = []
			# for res in results:
			# 	newpls.append(res)
			# self.pls = newpls

			# self._saveResultToFile()
			self._saveResultToWeb()

		except IndexError,e:
		# except Exception,e:
			# print 'Exception',e
			globalVar.mainlogger.error('Exception:'+str(e))

		finally:
			self._removeLogging()

	def run(self):
		self.initInfo();
		self.infoGather();
		self.scan()

	def safeRun(self):
		'''
		'''
		pscanner = multiprocessing.Process(target=self.run)
		pscanner.start()
		pscanner.join()
		
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	# server = '0xff.sinaapp.com/web/'
	server = 'www.hammer.org'
	token = 'dqc8mcv6ukaso3fsj1qvujss06'

	target = 'http://www.leesec.com'
	sn = Scanner(server,token,target)
	sn.initInfo()
	sn.infoGather()
	sn.scan()
	# sn.startScan()
	# print ">>>scan result:"
	#print sn.result
