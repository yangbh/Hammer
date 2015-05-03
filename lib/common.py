#!/usr/bin/python2.7
#coding:utf-8

import os
import json
import requests
# print '3333'

import globalVar
# print '4444'

from urlparse import urlparse
from pprint import pprint

# ----------------------------------------------------------------------------------------------------
# 	
# ----------------------------------------------------------------------------------------------------
def genFilename(url):
	ulp = urlparse(url)
	name = ulp.scheme + '_' + ulp.netloc.replace(':','_')
	return name

def genFileName_v2(target):
	# multi targets
	target = target.replace('\n','_')
	if len(target) > 256:
		target = target[:256]
	# single target
	target = target.replace('://','_')
	target = target.replace('/','')
	target = target.replace(':','')

	return target

def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)

# ----------------------------------------------------------------------------------------------------
# 	web plugin interfaces
# ----------------------------------------------------------------------------------------------------
def getScanInfo():
	# globalVar.scan_task_dict_lock.acquire()
	# pprint(globalVar.scan_task_dict)
	scanid = globalVar.scan_task_dict['scanID']
	server = globalVar.scan_task_dict['server']
	token = globalVar.scan_task_dict['token']
	# globalVar.scan_task_dict_lock.release()
	return {'scanid':scanid,'server':server,'token':token}

def getSubProInfo():
	# print 'getting sub process info'
	# globalVar.scan_task_dict_lock.acquire()
	services = globalVar.scan_task_dict['subtargets']
	# print 'services:'
	# print(services)
	# globalVar.scan_task_dict_lock.release()
	target = None
	if services.has_key('target'):
		if services['target'].has_key('ip'):
			target = services['target']['ip']
		elif services['target'].has_key('url'):
			target = services['target']['url']
		elif services['target'].has_key('host'):
			target = services['target']['host']
	# print 'target=',target
	return {'target':target}

def getPluginInfo():
	# globalVar.plugin_now_lock.acquire()
	# pprint(globalVar.plugin_now)
	pluginname = globalVar.plugin_now
	# globalVar.plugin_now_lock.release()
	return {'pluginname':pluginname}

def vuln_add(scanid=None,subtarget=None,pluginname=None,vulnlevel=None,vulninfo=None,server=None,token=None):
	try:
		serverurl = 'http://' + server +'/vulns_add.php'
		# cookies = {'TOKEN':token}
		retinfo = {}
		retinfo['scanid'] = scanid
		retinfo['pluginname'] = pluginname
		retinfo['subtarget'] = subtarget
		retinfo['vulnlevel'] = vulnlevel
		retinfo['vulninfo'] = vulninfo
		
		postdata = {'type':'add','token':token,'retinfo':json.dumps(retinfo)}
		# pprint(postdata)

		r = requests.post(serverurl,data=postdata)
		if r.status_code == 200 and r.text != '':
			# print r.text
			logger(r.text)
		else:
			# print 'return error, please check token and server'
			logger('return error, please check token and server')
		pass
	except requests.HTTPError,e:
		# print 'requests.HTTPError', e
		logger('requests.HTTPError'+str(e))

def security_note(vulnInfo):
	try:
		# print globals()
		# print 'in security_note'
		# print 'plugin pid=\t',os.getpid()
		# print 'id(globalVar)=\t',id(globalVar)
		# print 'globalVar.scan_task_dict=\t',globalVar.scan_task_dict
		scaninfo = getScanInfo()
		# print 'scaninfo:'
		# pprint(scaninfo)
		scanID = scaninfo['scanid']
		server = scaninfo['server']
		token = scaninfo['token']

		subproinfo = getSubProInfo()
		# print 'subproinfo:'
		# pprint(subproinfo)
		subTarget = subproinfo['target']

		plugininfo = getPluginInfo()
		# print 'plugininfo:'
		# pprint(plugininfo)
		pluginName = plugininfo['pluginname']
		# print scanID,server,token,subTarget,pluginName,vulnInfo
		logger('%d %s %s %s %s %s' % (scanID,server,token,subTarget,pluginName,vulnInfo),'WARNING')
		vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='info',vulninfo=vulnInfo,server=server,token=token)
		return
	except KeyError,e:
		print 'KeyError',e

def security_info(vulnInfo):
	try:
		# print 'in security_info'
		scaninfo = getScanInfo()
		# print 'scaninfo:'
		# pprint(scaninfo)
		scanID = scaninfo['scanid']
		server = scaninfo['server']
		token = scaninfo['token']

		subproinfo = getSubProInfo()
		# print 'subproinfo:'
		# pprint(subproinfo)
		subTarget = subproinfo['target']

		plugininfo = getPluginInfo()
		# print 'plugininfo:'
		# pprint(plugininfo)
		pluginName = plugininfo['pluginname']
		# print scanID,server,token,subTarget,pluginName,vulnInfo
		logger('%d %s %s %s %s %s' % (scanID,server,token,subTarget,pluginName,vulnInfo),'WARNING')
		vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='low',vulninfo=vulnInfo,server=server,token=token)
		return
	except KeyError,e:
		print 'KeyError',e
def security_warning(vulnInfo):
	try:
		scaninfo = getScanInfo()
		scanID = scaninfo['scanid']
		server = scaninfo['server']
		token = scaninfo['token']

		subproinfo = getSubProInfo()
		subTarget = subproinfo['target']

		plugininfo = getPluginInfo()
		pluginName = plugininfo['pluginname']
		# print scanID,server,token,subTarget,pluginName,vulnInfo
		logger('%d %s %s %s %s %s' % (scanID,server,token,subTarget,pluginName,vulnInfo),'WARNING')
		vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='medium',vulninfo=vulnInfo,server=server,token=token)
		return
	except KeyError,e:
		print 'KeyError',e

def security_hole(vulnInfo):
	try:
		scaninfo = getScanInfo()
		scanID = scaninfo['scanid']
		server = scaninfo['server']
		token = scaninfo['token']

		subproinfo = getSubProInfo()
		subTarget = subproinfo['target']

		plugininfo = getPluginInfo()
		pluginName = plugininfo['pluginname']
		# print scanID,server,token,subTarget,pluginName,vulnInfo
		logger('%d %s %s %s %s %s' % (scanID,server,token,subTarget,pluginName,vulnInfo),'WARNING')
		vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='high',vulninfo=vulnInfo,server=server,token=token)
		return
	except KeyError,e:
		print 'KeyError',e

def add_target(target):
	''' 添加一个扫描任务的Target'''
	# print globals()
	# print 'in add_target'
	# print 'plugin pid=\t',os.getpid()
	# print 'id(globalVar.undone_targets)=\t',id(globalVar.undone_targets)
	# print 'globalVar.undone_targets=',globalVar.undone_targets
	# globalVar.target_lock.acquire()
	if target not in globalVar.done_targets and target not in globalVar.undone_targets:
		# http 类型的target 可能存在一站多地址
		# 
		globalVar.undone_targets.append(target)
	# globalVar.target_lock.release()
	# print 'globalVar.undone_targets=',globalVar.undone_targets
	logger('Adding a target: %s' % target)

def add_task(task):
	'''
	添加一个扫描任务，单位为task
	task目前可以为basic type scan、plugin type scan
	'''
	globalVar.undone_tasks.append(task)
	logger('Adding a task:%s' % task)

# ----------------------------------------------------------------------------------------------------
# 	logging 接口
# ----------------------------------------------------------------------------------------------------
def logger(log,loglevel='DEBUG'):
	if globalVar.mainlogger != None:
		if loglevel == 'INFO':
			globalVar.mainlogger.info(log)
		elif loglevel == 'WARNING':
			globalVar.mainlogger.warning(log)
		elif loglevel == 'ERROR':
			globalVar.mainlogger.error(log)
		elif loglevel == 'CRITICAL':
			globalVar.mainlogger.critical(log)		
		else:
			globalVar.mainlogger.debug(log)
	else:
		print 'globalVar.mainlogger has not been valued'
		print(log)
	# logger = globalVar.mainlogger
	# print 'globalVar.mainlogger=',globalVar.mainlogger

# 注：
# 因为python的import机制，所以直接在common.py中print globalVar.mainlogger=
# globalVar.mainlogger始终为None,这是因为多次import common其实只导入一次，也
# 就是最初的那次，而此时内存中的 globalVar.mainlogger 已经在scanner_Class中被
# 赋值利用函数，然后在插件中调用此函数，那么访问到的就是内存中现在的赋值后的
# globalVar.mainlogger了

# pprint(globalVar.scan_task_dict)
# reload(globalVar)
# print 'globalVar.mainlogger=',globalVar.mainlogger
# print 'globalVar.scan_task_dict=',globalVar.scan_task_dict
# print 'logger=',logger
# ----------------------------------------------------------------------------------------------------
# 	
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	security_note('vuln test')
