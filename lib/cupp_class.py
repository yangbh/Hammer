#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import os
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class Cupp(object):
	"""docstring for Cupp"""
	def __init__(self, object= None):
		super(Cupp, self).__init__()
		if type(object) == type(None):
			pass
		if type(object) == str:
			self.username = object
		if type(object) == list:
			pass
		self.pwd = []

	def GenPwdFromFile(self,pwdfile):
		if pwdfile == None:
			pwdfile = 'db/password_small.txt'
		ret = []
		fp = open(pwdfile,'r')
		for eachline in fp:
			ret.append(eachline)
		self.pwd = ret
		return ret

	def GenPwdByRule(self, ruledict=None,rulefile=None):
		'''
		rule dict format example:
			ruledict = {'username':'zhuzhuxia','domain':'knownsec'}
		'''
		if rulefile == None:
			rulefile =  'db/rulefile_by_zhuzhuxia.txt'
		if ruledict == None:
			ruledict ={}

		ret = []
		fp = open(rulefile,'r')
		for eachline in fp:
			linsep_len = len(os.linesep)
			eachline = eachline[:-linsep_len]
			if eachline !='' and eachline[0] != '#' :
				for key in ruledict.keys():
					eachline = eachline.replace('%'+key+'%',ruledict[key])
				ret.append(eachline)
		self.pwd = ret
		return ret
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	heigepwd = Cupp('superhei')
	ruledict = {'username':'heige','domain':'knownsec'}
	print heigepwd.GenPwdByRule(ruledict)