#!/usr/bin/python2.7
#coding:utf-8

import logging
import multiprocessing
from dummy import BASEDIR

#
#	server info
#
server = ''
token = ''

#
# shared variables
#
manager = multiprocessing.Manager()
# 	tasks
done_tasks = manager.list()
undone_tasks = manager.list()
#	targets
target_lock = multiprocessing.Lock()
# done_targets = []
# undone_targets =[]
done_targets = manager.list()
undone_targets = manager.list()
willdone_targets = manager.list()

#
#	main scan task
#
# scan_task_dict just like
# {'pid': 3280,
# 'scanID': None,
# 'subtargets': {},
# 'target': 'http://www.leesec.com/',
# 'server': 'www.hammer.org'}
scan_task_dict = {}
scan_task_dict_lock = multiprocessing.Lock()
depth_now = 0

#
#	for each sub scan task
#
# plugin_now just like
# 'Neighborhood-Host Scanning'
plugin_now = ''

plugin_now_lock = multiprocessing.Lock()


# logger
# 每import globalVar 一次，就会执行一次，因此限制只执行一次
# Set up a specific logger with our desired output level
mainlogger = None
# print dir()
# print locals()
# print globals()
# # print globalVar.mainlogger
# if 'mainlogger' not in dir():
# 	print '------------1------------'
# 	mainlogger = logging.getLogger('main')
# 	mainlogger.setLevel(logging.INFO)
# 	# 定义handler的输出格式formatter    
# 	# formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')  
# 	formatter = logging.Formatter('[%(name)s] - [%(process)d] - [%(levelname)s] - %(message)s')  

# 	# # 创建一个handler，用于写入日志文件    
# 	# fh = logging.FileHandler(BASEDIR+'/output/scan.log','a')    
# 	# # 再创建一个handler，用于输出到控制台    
# 	ch = logging.StreamHandler()  

# 	fi = logging.Filter('main')

# 	# fh.addFilter(fi)
# 	ch.addFilter(fi)

# 	# fh.setFormatter(formatter)
# 	ch.setFormatter(formatter)

# 	# mainlogger.addHandler(fh)
# 	mainlogger.addHandler(ch)

# 	# mainlogger.info('Hello World')
# 	# print 'hello world'
logger = None