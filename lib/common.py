#!/usr/bin/python2.7
#coding:utf-8

import os
import json
import requests

import globalVar
from urlparse import urlparse
from pprint import pprint

# ----------------------------------------------------------------------------------------------------
# 	
# ----------------------------------------------------------------------------------------------------
def genFilename(url):
	ulp = urlparse(url)
	name = ulp.scheme + '_' + ulp.netloc.replace(':','_')
	return name

def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)

# ----------------------------------------------------------------------------------------------------
# 	web plugin interfaces
# ----------------------------------------------------------------------------------------------------
def getScanInfo():
	# globalVar.scan_task_dict_lock.acquire()
	pprint(globalVar.scan_task_dict)
	scanid = globalVar.scan_task_dict['scanID']
	server = globalVar.scan_task_dict['server']
	session = globalVar.scan_task_dict['session']
	# globalVar.scan_task_dict_lock.release()
	return {'scanid':scanid,'server':server,'session':session}

def getSubProInfo():
	# print 'getting sub process info'
	# globalVar.scan_task_dict_lock.acquire()
	services = globalVar.scan_task_dict['subtargets']
	pprint(services)
	# globalVar.scan_task_dict_lock.release()
	target = None
	if services.has_key('target'):
		if services['target'].has_key('ip'):
			target = services['target']['ip']
		elif services['target'].has_key['url']:
			target = services['target']['url']
		elif services['target'].has_key['host']:
			target = services['target']['host']
	# print target
	return {'target':target}

def getPluginInfo():
	# globalVar.plugin_now_lock.acquire()
	pprint(globalVar.plugin_now)
	pluginname = globalVar.plugin_now
	# globalVar.plugin_now_lock.release()
	return {'pluginname':pluginname}

def vuln_add(scanid=None,subtarget=None,pluginname=None,vulnlevel=None,vulninfo=None,server=None,session=None):
	try:
		serverurl = 'http://' + server +'/scans_add.php'
		cookies = {'PHPSESSID':session}
		retinfo = {}
		retinfo['scanid'] = scanid
		retinfo['pluginname'] = pluginname
		retinfo['subtarget'] = subtarget
		retinfo['vulnlevel'] = vulnlevel
		retinfo['vulninfo'] = vulninfo
		
		postdata = {'type':'vuln','retinfo':json.dumps(retinfo)}
		# pprint(postdata)

		r = requests.post(serverurl,cookies=cookies,data=postdata)
		if r.status_code == 200 and r.text != '':
			print r.text
		else:
			print 'return error, please check session and server'
		pass
	except requests.HTTPError,e:
		print 'requests.HTTPError', e

def security_note(vulnInfo):
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
	session = scaninfo['session']

	subproinfo = getSubProInfo()
	# print 'subproinfo:'
	# pprint(subproinfo)
	subTarget = subproinfo['target']

	plugininfo = getPluginInfo()
	# print 'plugininfo:'
	# pprint(plugininfo)
	pluginName = plugininfo['pluginname']
	print scanID,server,session,subTarget,pluginName,vulnInfo
	vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='info',vulninfo=vulnInfo,server=server,session=session)
	return

def security_info(vulnInfo):
	scaninfo = getScanInfo()
	scanID = scaninfo['scanid']
	server = scaninfo['server']
	session = scaninfo['session']

	subproinfo = getSubProInfo()
	subTarget = subproinfo['target']

	plugininfo = getPluginInfo()
	pluginName = plugininfo['pluginname']
	print scanID,server,session,subTarget,pluginName,vulnInfo
	vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='low',vulninfo=vulnInfo,server=server,session=session)
	return

def security_warning(vulnInfo):
	scaninfo = getScanInfo()
	scanID = scaninfo['scanid']
	server = scaninfo['server']
	session = scaninfo['session']

	subproinfo = getSubProInfo()
	subTarget = subproinfo['target']

	plugininfo = getPluginInfo()
	pluginName = plugininfo['pluginname']
	print scanID,server,session,subTarget,pluginName,vulnInfo
	vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='medium',vulninfo=vulnInfo,server=server,session=session)
	return

def security_hole(vulnInfo):
	scaninfo = getScanInfo()
	scanID = scaninfo['scanid']
	server = scaninfo['server']
	session = scaninfo['session']

	subproinfo = getSubProInfo()
	subTarget = subproinfo['target']

	plugininfo = getPluginInfo()
	pluginName = plugininfo['pluginname']
	print scanID,server,session,subTarget,pluginName,vulnInfo
	vuln_add(scanid=scanID,subtarget=subTarget,pluginname=pluginName,vulnlevel='high',vulninfo=vulnInfo,server=server,session=session)
	return
# ----------------------------------------------------------------------------------------------------
# 	
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	security_note('vuln test')
