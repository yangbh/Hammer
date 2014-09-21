#!/usr/bin/python2.7
#coding:utf-8

import threading
import copy

class myThread(threading.Thread):
	def __init__(self, lock,threadID):
		'''@summary: 初始化对象。
		@param lock: 琐对象。
		@param threadName: 线程名称。
		'''
		super(myThread, self).__init__()  #注意：一定要显式的调用父类的初始 化函数。
		self.lock = lock
		self.threadID = threadID

	def run(self):
		''''''
		importcmd = 'from app import Audit'
		exec(importcmd)
		if locals().has_key('Audit'):
			MAudit = copy.deepcopy(Audit)
			ret = MAudit()
			self.lock.acquire()
			print id(Audit)
			print id(MAudit)
			print 'thread',self.threadID,':',ret
			self.lock.release()

if __name__ == '__main__':
	lock = threading.Lock()
	threads = []
	for i in range(100):
		t = myThread(lock,i)
		threads.append(t)

	for eachmthpl in threads:
		eachmthpl.start()

	for eachmthpl in threads:
		eachmthpl.join()

