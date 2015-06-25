#!/usr/bin/python2.7
#coding:utf-8
import os
import socket
import paramiko
import threading
from concurrent import futures
import sys
import time
from dummy import *

info = {
	'NAME':'SSH Weak Password',
	'AUTHOR':'yangbh',
	'TIME':'20140716',
	'WEB':''
}
opts = {
	'ip':'176.28.50.165',	#'target ip'
	'timeout':3000,
}
# opts = [
# 	['ip','176.28.50.165','target url'],
# 	['timeout',3000,'pulgin run max time'],
# ]
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def getPwds(neighborhosts):
	''' '''
	pwddicts={}
	#usernames = ['root','test','rootroot','admin','administrator']
	usernames=['root','test']

	commonpwd = []
	#pwdfile = '../../lib/db/temp.txt'
	pwdfile = BASEDIR+'/lib/db/password_small.dict'

	fp = open(pwdfile,'r')
	for eachline in fp:
		tp =  eachline.replace('\r','')
		tp =  tp.replace('\n','')
		if tp != '':
			commonpwd.append(tp)
	
	#
	if neighborhosts:
		for eachhost in neighborhosts:
			eachdomain = GetFirstLevelDomain(eachhost)
			tplist = eachdomain.split('.')
			usernames.append(tplist[0])
			usernames.append(eachhost)
			usernames.append(eachdomain)
			commonpwd.append(eachhost)
			commonpwd.append(eachdomain)
			commonpwd.append(tplist[0])

	#
	rulefile = BASEDIR +'/lib/db/passwd_gen.rule'
	for eachuser in usernames:
		pwddicts[eachuser] = list(commonpwd)
		args = {'username':eachuser}
		rf = RuleFile(rulefile,args)
		rf._getRules()
		for i in rf.ret:
			pwddicts[eachuser].append(i)

		pwddicts[eachuser] = sorted(list(set(pwddicts[eachuser])))

	return pwddicts

def ssh2(ip,port,username,passwd,lock):  
	sshcmd = 'ssh://%s:%s@%s:%d' % (username,passwd,ip,port)
	logger(sshcmd)
	for i in range(5):
		try:  
			ssh = paramiko.SSHClient()  
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
			ssh.connect(ip,port,username,passwd,timeout=5) 
			logger('login success %s' % sshcmd)
			ssh.close()
			security_hole(sshcmd)
			break

		except paramiko.AuthenticationException,e:  
			logger('paramiko.AuthenticationException:\t%s' % str(e))
			break
		except socket.timeout,e:
			logger('socket.timeout:\t%s' % str(e))
			break
		except socket.error,e:
			logger('socket.error:\t%s' % str(e))
			break
		except paramiko.SSHException,e:
			#print 'paramiko.SSHException',e
			logger('paramiko.SSHException:\t%s' % str(e))
			time.sleep(1)
		ssh.close()

def getPortByService(services,scname):
	try:
		ret = []
		for eachport in services['port_detail'].keys():
			if services['port_detail'][eachport]['name'] == scname:
				ret.append(eachport)
		print ret
		return ret
	except KeyError,e:
		print 'KeyError:\t', e

def Assign(services):
	if services.has_key('ip') and services.has_key('ports'):
		if 22 in services['ports']:
			# name maybe tcpwrapped
			if services['port_detail'][22]['name'] == 'ssh':
				return True
		else:
			ports = getPortByService(services,'ssh')
			if ports and len(ports):
				return True
	return False

def Audit(services):
	# get ssh port
	ssh_port  = 0
	if 22 in services['ports']:
		# name maybe tcpwrapped
		if services['port_detail'][22]['name'] == 'ssh':
			ssh_port = 22

	else:
		ports = getPortByService(services,'ssh')
		if ports and len(ports):
			ssh_port = ports[0]
	if ssh_port == 0:
		return

	pwddicts = {}
	# 
	neighborhosts = []
	if services.has_key('neighborhosts'):
		neighborhosts = services['neighborhosts']
	pwddicts = getPwds(neighborhosts)

	# pprint(pwddicts)
	#sys.exit(0)

	#  threads
	lock = threading.Lock()
	threads = []
	ip = services['ip']
	maxthreads = 20

	# for eachname in pwddicts.keys():
	# 	for eachpwd in pwddicts[eachname]:
	# 		th = threading.Thread(target=ssh2,args=(ip,ssh_port,eachname,eachpwd,lock))
	# 		threads.append(th)

	# i = 0
	# while i<len(threads):
	# 	if i+maxthreads >len(threads):
	# 		numthreads = len(threads) - i
	# 	else:
	# 		numthreads = maxthreads
	# 	print 'threads:',i,' - ', i + numthreads

	# 	# start threads
	# 	for j in range(numthreads):
	# 		threads[i+j].start()

	# 	# wait for threads
	# 	for j in range(numthreads):
	# 		threads[i+j].join()

	# 	i += maxthreads


	with futures.ThreadPoolExecutor(max_workers=maxthreads) as executor:      #默认10线程
		for eachname in pwddicts.keys():
			for eachpwd in pwddicts[eachname]:
				# print 'starting\t',eachname+':'+eachpwd
				future = executor.submit(ssh2,ip,ssh_port,eachname,eachpwd,lock)
	# if ret != '':
	# 	security_hole(str(ret))
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__': 
	ip='176.28.50.165'
	if len(sys.argv) ==  2:
		ip = sys.argv[1]
	# services={'ip':'127.0.0.1','ports':[80,8080],'port_detail':{22:{'name':'ssh'}}, 'neighborhosts': ['eguan.cn']}
	services={'ip':ip,'ports':[22],'port_detail':{22:{'name':'ssh'}}, 'neighborhosts': ['netlab.pkusz.edu.cn']}
	pprint(Audit(services))
	pprint(services)