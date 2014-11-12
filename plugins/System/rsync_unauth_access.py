#!/usr/bin/python2.7
#coding:utf-8

import os
from dummy import * 

info = {
	'NAME':'Rsync Unauthorized Access',
	'AUTHOR':'yangbh',
	'TIME':'20141112',
	'WEB':'http://drops.wooyun.org/papers/161',
	'DESCRIPTION':'Rsync 配置不当导致未授权访问'
}

def Audit(services):
	retinfo = None
	output = ''
	if services.has_key('ip') and services.has_key('ports'):
		if 873 in services['ports']:
			ip = services['ip']
			cmd_res = os.popen('rsync -av --timeout=10 '+ ip +'::').read()
			# print cmd_res
			if 'rsync: failed' in cmd_res:
				return
			else:
				output = cmd_res
				security_warning(cmd_res)

	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'ip':'10.183.0.51','ports':[873]}
	pprint(Audit(services))
	pprint(services)