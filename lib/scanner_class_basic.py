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
def procFunc(pluginheader):
	try:
		if type(pluginheader) == PluginLoader:
			pl = pluginheader
			pl.loadPlugins()
			pl.runPlugins()
			globalVar.mainlogger.debug('returnning pl')			
			# return pl
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
	def __init__(self,server=None,token=None,target=None,loglever='INFO'):
		super(Scanner, self).__init__()
		self.server = server
		self.token = token
		self.target = target

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
		globalVar.mainlogger.info('\tserver='+server)
		globalVar.mainlogger.info('\ttoken='+token)
		globalVar.mainlogger.info('\ttarget='+target)

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
			# print '>>>Step1: init starting info'
			globalVar.mainlogger.info('[*][*] Step1: init starting info')
			self.services = []
			if target==None:
				target = self.target
			targets = []
			if target:
				# ip range type
				m = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,2})?$',target)
				if m:
					ipnet = list(ipaddress.ip_network(unicode(target)).hosts())
					for eachipad in ipnet:
						targets.append(eachipad.compressed)
				else:
					# one ip
					m = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',target)
					if m:
						targets.append(target)

					else:
						# url type
						m = re.match('(http[s]?)://([^:^/]+):?([^/]*)/?',target)
						if m:
							http_type = m.group(1)
							# print m.group(2)
							n = re.search('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\/\d{1,2})?$',m.group(2))
							# ip
							if n:
								# print 'is an ip type url'
								ip = m.group(2)
								if target[-1] == '/':
									target = target[:-1]
								targets.append(ip)
								targets.append(target)
							else:
								host = m.group(2)
								ports = m.group(3)
								# print host
								ip = socket.gethostbyname(host)
								domain = GetFirstLevelDomain(host)
								# print 'ip=',ip
								if target[-1] == '/':
									target = target[:-1]
								targets.append(ip)
								targets.append(target)
								targets.append(domain)
						else:
							# host type
							domain = GetFirstLevelDomain(target)
							targets.append(domain)


			globalVar.target_lock.acquire()
			globalVar.undone_targets += targets
			globalVar.target_lock.release()

			for each_target in globalVar.undone_targets:
				service = {}
				service_type = self._getServiceType(each_target)
				# print service_type
				service[service_type] = each_target
				self.services.append(service)

			# pprint(self.services)
			globalVar.mainlogger.info('Targets:')
			for service in self.services:
				globalVar.mainlogger.info('\t'+str(service))

			self._noticeStartToWeb()
			self._initGlobalVar()
		except IndexError,e:
		# except Exception,e:
			# print 'Exception:',e
			globalVar.mainlogger.error('Exception:'+str(e))

	def infoGather(self,depth=1):
		try:
			#	Step 2
			# print '>>>Step2: gathing info'
			globalVar.mainlogger.info('[*][*] Step2: gathing info')
			
			self.services = []
			for i in range(depth):
				# print '>>>',i,'<<<'
				# print globalVar.done_targets
				# print 'id(globalVar.undone_targets)=\t',id(globalVar.undone_targets)
				# print 'globalVar.undone_targets=',globalVar.undone_targets
				
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
					proPool = MyPool(multiprocessing.cpu_count())
					p = proPool.map_async(procFunc,pls)
					proPool.close()
					try:
						proPool.join()
					except KeyboardInterrupt,e:
						print "Caught KeyboardInterrupt, terminating workers"

					results = p.get()

					# newpls = []
					# for res in results:
					# 	newpls.append(res)
					# self.pls = self.pls + newpls

					for service in results:
						service['alreadyrun'] = True
						self.services.append(service)

			# for pl in self.pls:
			# 	service = pl.services
			# 	service['alreadyrun'] = True
			# 	self.services.append(service)
			# self.pls = []

			for each_target in globalVar.undone_targets:
				service = {}
				service_type = self._getServiceType(each_target)
				# print service_type
				service[service_type] = each_target
				self.services.append(service)

			# pprint(self.services)
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
			# print '>>>Step3: run each sub task'
			globalVar.mainlogger.info('[*][*] Step3: run each sub task')
			
			self.pls = []
			for each_service in self.services:
				pl = PluginLoader(None,each_service,self.target)
				self.pls.append(pl)

			results = []

			# 改用map_async的方式
			# proPool = multiprocessing.Pool(10)
			proPool = MyPool(multiprocessing.cpu_count())
			p = proPool.map_async(procFunc,self.pls)
			proPool.close()
			try:
				proPool.join()
			except KeyboardInterrupt,e:
				# print "Caught KeyboardInterrupt, terminating workers"
				# while True:
				# print '---------->>hahahaha main thread caught ctrl+c'
				globalVar.mainlogger.error('Caught KeyboardInterrupt, terminating workers')

			# print '>>>>>>>>>>>>>>>>>>All Done<<<<<<<<<<<<<<<<'s
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
