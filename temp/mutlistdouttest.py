#!/usr/bin/python2.7
#coding:utf-8


import sys
import thread
import time

def timer(threadname):
    saveout = sys.stdout
    fsock = open(threadname,'w')
    sys.stdout = fsock
    for i in xrange(1,10):
    	print '-'
    	time.sleep(2)
    sys.stdout = saveout
    fsock.close()
   
 
def test(): #Use thread.start_new_thread() to create 2 new threads
    thread.start_new_thread(timer, ('1.txt',))
    thread.start_new_thread(timer, ('2.txt',))
 
if __name__=='__main__':
    timer('1.log')