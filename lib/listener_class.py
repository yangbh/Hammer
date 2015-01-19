#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import uuid
import json
import time
import platform
import requests
import threading
import logging

import globalVar

from pprint import pprint
from scannerLoader_class import ScannerLoader
from dummy import *


def get_mac_address():
	mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
	return ":".join([mac[e:e+2] for e in range(0,11,2)] )

class Listener(object):
	"""docstring for Listener"""
	def __init__(self, server, token, loglevel = 'INFO'):
		super(Listener, self).__init__()
		self.server = server
		self.token = token
		self.loglevel = loglevel
		self.os = platform.system()
		self.mac = get_mac_address()
		self.lock = threading.Lock()
		self.tasks = []
		self.flag = True


		self.loghandler = []
		# log 模块,确保赋值一次
		if globalVar.logger is None:
			globalVar.logger = logging.getLogger('root')
			if loglevel == 'DEBUG':
				globalVar.logger.setLevel(logging.DEBUG)
			else:
				globalVar.logger.setLevel(logging.INFO)

			#	logging handler
			formatter = logging.Formatter('[%(asctime)s] - [%(process)d] - [%(levelname)s] - %(message)s')  
			# 创建一个handler，用于写入日志文件  
			filepath = BASEDIR+'/output/listen.log'
			if os.path.isfile(filepath):
				os.remove(filepath)
			fh = logging.handlers.RotatingFileHandler(filepath,maxBytes=10*1024*1024,backupCount=5)    
			# 再创建一个handler，用于输出到控制台
			ch = logging.StreamHandler()  
			
			fi = logging.Filter('')

			fh.addFilter(fi)
			ch.addFilter(fi)

			fh.setFormatter(formatter)
			ch.setFormatter(formatter)

			self.loghandler.append(ch)
			self.loghandler.append(fh)

			self._initLogging()

		globalVar.logger.info('[*] Start a new scan')
		globalVar.logger.info('\tserver\t=%s' % server)
		globalVar.logger.info('\ttoken\t=%s' % token)
		globalVar.logger.info('\tloglevel\t=%s' % loglevel)

	def _initLogging(self):
		globalVar.logger.info('before test')
		for handler in self.loghandler:
			globalVar.logger.addHandler(handler)
		globalVar.logger.info('after test')
	
	def _removeLogging(self):
		globalVar.logger.info('before test')
		for handler in self.loghandler:
			globalVar.logger.removeHandler(handler)
		globalVar.logger.info('after test')

	def listen_task(self):
		'''
		持续监听,访问server，监听是否存在未完成的task
		若server有返回task信息，则将task信息写入task pool
		'''
		while self.flag:
			try:
				serverurl = 'http://' + self.server +'/dist_hi.php'
				postdata = {'token':self.token,'os':self.os,'mac':self.mac,'type':'start'}

				r = requests.post(serverurl,data=postdata)
				# print r.status_code
				if r.status_code == 200:
					# print r.text
					ret = json.loads(r.text)
					code = ret['code']
					info = ret['info']
					data = ret['data']
					globalVar.logger.debug('worker: hello server, any task?')
					globalVar.logger.debug('server:%s' % info)
					if code and 'no task' not in info:
						globalVar.logger.info('[*] new task %s' % data['target'])
						globalVar.logger.debug('%s' % data)
						if type(data)==dict:
							self.lock.acquire()
							self.tasks.append(data)
							self.lock.release()

				else:
					globalVar.logger.error('return error, please check token and server')
				pass
			except requests.HTTPError,e:
				globalVar.logger.error('requests.HTTPError %s' %e)

			time.sleep(10)

	def deal_task(self):
		'''
		持续执行task
		'''
		while self.flag:
			try:
				if len(self.tasks):
					self.lock.acquire()
					arg = self.tasks[0]
					del(self.tasks[0])
					self.lock.release()
					globalVar.logger.debug('prepare to run a task: %s' % arg['target'])
					sl = ScannerLoader(self.server, self.token, arg)
					sl.run()

					globalVar.logger.info('[*] done: %s' % arg['target'])
					# notice server this task done
					serverurl = 'http://' + self.server +'/dist_hi.php'
					postdata = {'token':self.token,'os':self.os,'mac':self.mac,'type':'end','taskid':arg['taskid']}

					r = requests.post(serverurl,data=postdata)
					# print r.status_code
					if r.status_code == 200:
						globalVar.logger.debug('worker: hello server, one task done, taskid: %s' % arg['taskid'])
						globalVar.logger.debug('server: %s' % r.text)

			except Exception,e:
				globalVar.logger.error('Exception: %s' % e)

			time.sleep(20)

	def run(self):
		'''
		开启监听与处理两个线程
		'''
		listenth = threading.Thread(target=self.listen_task)
		dealth = threading.Thread(target=self.deal_task)

		listenth.start()
		dealth.start()
		try:
			while True:
				time.sleep(10)
		except KeyboardInterrupt,e:
			globalVar.logger.debug("Caught KeyboardInterrupt, terminating lisent and deal threads")
			self.flag = False

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	listen = Listener('www.hammer.org', 'dEc6Yof8bgWwRrD0KNDc643Pe2kspXa2')
	listen.listen_task()
