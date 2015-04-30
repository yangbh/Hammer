#!/usr/bin/python2.7
#coding:utf-8

import os
import json
import yaml
import requests

import globalVar

from dummy import BASEDIR
from consoleColor_class import *

class WebUser(object):
	"""docstring for WebUser"""
	def __init__(self,conffile=BASEDIR+'/conf/hammer.yaml'):
		super(WebUser, self).__init__()
		self.conffile 	= conffile
		self.server = None
		self.token	= None
		self.id		= None
		self.name	= None
		self.taskid = None

		self.loadInfo()

		if self.checklogin:
			color.cprint("[*] Login success",GREEN)
		else:
			color.cprint("[*] Login failed",RED)
			

	def checklogin(self,server,token):
		'''检测server&token'''
		try:
			server = server if server else self.server
			token = token if token else self.token
			serverurl = 'http://' + server + '/login.php'
			postdata = {'token':token}

			r = requests.post(serverurl,data=postdata)
			# print r.status_code
			if r.url.endswith('index.php'):
				return True
			return False

		except Exception,e:
			color.cprint("[!] Err:%s"%e,RED)

	def loadInfo(self):
		'''从配置文件加载用户信息，若配置文件内信息不全则提示'''
		if os.path.isfile(self.conffile):
			fp = open(self.conffile)
		else:
			fp = open(self.conffile,'a')
		try:
			conf = yaml.load(fp)
			# print conf
			self.server = conf['server']
			self.token 	= conf['token']
			self.id 	= conf['id']
			self.name 	= conf['name']
			self.taskid = conf['taskid']

		except Exception,e:
			print 'Seems user info not inited',e
		finally:
			fp.close()

	def setUserInfo(self,server=None,token=None):
		'''设置用户的信息，但是暂时不存入配置文件'''
		try:
			conf = {}
			if server:
				self.server = server
			if token:
				self.token = token

		except IndexError,e:
			print 'IndexError',e

	def refreshTaskID(self):
		'''创建一个新的task'''
		try:
			serverurl = 'http://' + self.server + '/scans_add.php'
			postdata = {'token':self.token,'type':'start','url':'console'}

			r = requests.post(serverurl,data=postdata)
			# print r.status_code
			if r.status_code == 200:
				self.taskid = json.loads(r.text)['id']
				self.dumpInfo()

		except Exception,e:
			color.cprint("[!] Err:%s"%e,RED)

	def rsyncUserInfo(self):
		'''用户使用set命令将信息缓存在内存，再通过此同步用户信息函数验证用户凭证
		正确则获取用户信息，但是不存入配置文件
		不正确则不存入配置文件，并将程序中的用户信息回滚'''
		try:
			serverurl = 'http://' + self.server +'/user_setting.php'
			postdata = {'token':self.token,'type':'getinfo'}

			r = requests.post(serverurl,data=postdata)
			# print r.status_code
			if r.status_code == 200:
				# print r.text
				ret = json.loads(r.text)
				code = ret['code']
				info = ret['info']
				if code and ret.has_key('data'):
					# print ret
					self.id = ret['data']['id']
					self.name = ret['data']['name']
					
					return

			# otherwise, roll back
			color.cprint("[!] Err: connect wrong, roll back user infomation",RED)
			fp = open(self.conffile)
			conf = yaml.load(fp)
			# print conf
			self.server = conf['server']
			self.token = conf['token']

		except Exception,e:
			color.cprint("[!] Err:%s"%e,RED)

	def dumpInfo(self):
		'''将程序中的用户信息写入配置文件'''
		try:
			fp= open(self.conffile)
			conf = yaml.load(fp)
			conf = {} if conf==None else conf
			fp.close()
			conf['server'] = self.server
			conf['token'] = self.token
			conf['id'] = self.id
			conf['name'] = self.name
			conf['taskid'] = self.taskid
			fp = open(self.conffile, "w")
			yaml.dump(conf,fp)
			fp.close()
		except Exception,e:
			color.cprint("[!] Err:%s"%e,RED)
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	user = WebUser()
	user.setUserInfo('www.hammer.org','dEc6Yof8bgWwRrD0KNDc643Pe2kspXa2')
	user.dumpsInfo()
	print user.name