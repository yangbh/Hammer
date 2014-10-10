#!/usr/bin/python2.7
#coding:utf-8

import multiprocessing

#	main scan task

# scan_task_dict just like
# {'pid': 3280,
# 'scanID': None,
# 'subtargets': {},
# 'target': 'http://www.leesec.com/'}

scan_task_dict = {}

scan_task_dict_lock = multiprocessing.Lock()


#	for each sub scan task

# plugin_now just like
# 'Neighborhood-Host Scanning'
plugin_now = ''

plugin_now_lock = multiprocessing.Lock()