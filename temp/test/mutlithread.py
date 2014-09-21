#!/usr/bin/python2.7
#coding:utf-8

import multiprocessing
import time

def callAudit():
	importcmd = 'from app import Audit'
	exec(importcmd)
	if locals().has_key('Audit'):
		ret = Audit()
		print id(Audit)
		print 'thread',':',ret
		return ret

if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=100)
	result = []
	for i in xrange(100):
		msg = "hello %d" %(i)
		result.append(pool.apply_async(callAudit, ()))
	pool.close()
	pool.join()
	for res in result:
		print res.get()
	print "Sub-process(es) done."