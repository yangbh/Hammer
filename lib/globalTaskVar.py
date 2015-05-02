#!/usr/bin/python2.7
#coding:utf-8

import logging
import multiprocessing
# from dummy import BASEDIR
# from autoProxyRequests_class import AutoProxyRequests

#	---------------------------------------------------------------
#						主进程
#		ListenTask子进程			TaskDeal子进程
#										SubTarget子进程
#												SubRunPlugin子进程								
#	---------------------------------------------------------------

#
#	server info
#	主进程中初始化之后，不需要修改
server = ''
token = ''

#
# 	shared variables
# 	共享变量
manager = multiprocessing.Manager()

# 	tasks
# 	需要在ListenTask子进程\TaskDeal子进程间共享
done_tasks = manager.list()
undone_tasks = manager.list()

#	logger
logger = None