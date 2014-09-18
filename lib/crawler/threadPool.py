#!/usr/bin/python2.7
#coding:utf-8

# ----------------------------------------------------------------------------------------------------
# filename: threadPool.py
# func: 该模块包含工作线程与线程池的实现。
# author: lvyaojia
# web: https://github.com/lvyaojia/crawler
# modifed by mody at 2014-07-23
# ----------------------------------------------------------------------------------------------------

import logging
import traceback
from threading import Thread, Lock
from Queue import Queue,Empty

#log = logging.getLogger('Main.threadPool')
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class Worker(Thread):

	def __init__(self, threadPool):
		Thread.__init__(self)
		self.threadPool = threadPool
		self.daemon = True
		self.state = None
		self.start()

	def stop(self):
		self.state = 'STOP'

	def run(self):
		while True:
			if self.state == 'STOP':
				break
			try:
				func, args, kargs = self.threadPool.getTask(timeout=1)
			except Empty:
				continue
			try:
				self.threadPool.increaseRunsNum() 
				result = func(*args, **kargs)
				self.threadPool.decreaseRunsNum()
				if result:
					self.threadPool.putTaskResult(*result)
				self.threadPool.taskDone()
			except Exception, e:
				#log.critical(traceback.format_exc())
				print 'Exception:\t',e
				print traceback.format_exc()

class ThreadPool(object):

	def __init__(self, threadNum):
		self.pool = [] #线程池
		self.threadNum = threadNum  #线程数
		self.lock = Lock() #线程锁
		self.running = 0	#正在run的线程数
		self.taskQueue = Queue() #任务队列
		self.resultQueue = Queue() #结果队列
	
	def startThreads(self):
		for i in range(self.threadNum): 
			self.pool.append(Worker(self))
	
	def stopThreads(self):
		for thread in self.pool:
			thread.stop()
			thread.join()
		del self.pool[:]
	
	def putTask(self, func, *args, **kargs):
		self.taskQueue.put((func, args, kargs))

	def getTask(self, *args, **kargs):
		task = self.taskQueue.get(*args, **kargs)
		return task

	def taskJoin(self, *args, **kargs):
		self.taskQueue.join()

	def taskDone(self, *args, **kargs):
		self.taskQueue.task_done()

	def putTaskResult(self, *args):
		self.resultQueue.put(args)

	def getTaskResult(self, *args, **kargs):
		return self.resultQueue.get(*args, **kargs)

	def increaseRunsNum(self):
		self.lock.acquire() #锁住该变量,保证操作的原子性
		self.running += 1 #正在运行的线程数加1
		self.lock.release()

	def decreaseRunsNum(self):
		self.lock.acquire() 
		self.running -= 1 
		self.lock.release()

	def getTaskLeft(self):
		#线程池的所有任务包括：
		#taskQueue中未被下载的任务, resultQueue中完成了但是还没被取出的任务, 正在运行的任务
		#因此任务总数为三者之和
		return self.taskQueue.qsize()+self.resultQueue.qsize()+self.running

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	pass