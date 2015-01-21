#!/usr/bin/python2.7
#coding:utf-8

import os
from subprocess import * 
from dummy import * 

info = {
	'NAME':'Rsync Unauthorized Access',
	'AUTHOR':'yangbh',
	'TIME':'20141112',
	'WEB':'http://drops.wooyun.org/papers/161,https://github.com/yaseng/pentest/blob/master/misc/rsync.py',
	'DESCRIPTION':'Rsync 配置不当导致未授权访问',
	'VERSION':'0.2'
}
opts = [
	['ip','221.123.140.66','target ip'],
	['ports',[873],'target ip\'s ports']
]

def Assign(services):
	if services.has_key('ip') and services.has_key('ports'):
		if 873 in services['ports']:
			return True
	return False

def Audit(services):
	ip = services['ip']
	msg_text = os.popen('rsync -av --timeout=10 '+ ip +'::').read()
	# print cmd_res
	if 'rsync: failed' in msg_text:
		return
	else:
		if msg_text :
			msg_arr = msg_text.split('\n')
			if len(msg_arr) > 0:
				logger("%d modules Found" % len(msg_arr))
				for module in msg_arr :
					if module :
						logger("Test %s::%s" % (host,module));
						module = module.strip()
						p = Popen('rsync -av --timeout=10 '+ ip +'::' + module, stdin=PIPE, stdout=PIPE)  
						req = p.stdout.readline()
						if req and len(req and "@ERROR") :
							logger("Anonymous rsync module:" + module + " found !!!")
							security_warning(msg_text + '::' + module)
						# else :
						# 	print req
					# else :
					# 	continue
			else :
				logger("No modules Found", 2)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'ip':'10.183.0.51','ports':[873]}
	pprint(Audit(services))
	pprint(services)