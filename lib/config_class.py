#!/usr/bin/python2.7
#coding:utf-8

from configobj import ConfigObj
from dummy import BASEDIR

class Config(object):
	"""docstring for Config"""
	def __init__(self, conffile='BASEDIR'+'/conf/basic.conf'):
		super(Config, self).__init__()
		self.conffile = conffile
		self.config = ConfigObj(conffile)

	def _check(self):
		'''
		'''
		try:
			if self.config['server'] != '':
				pass
		except	Exception,e:
			# print 'Exception',e
			return False



