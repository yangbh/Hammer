#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import os
CURRENT_PATH=os.path.dirname(__file__)
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

	def genPwdFromFile(self,pwdfile):
		if pwdfile == None:
			pwdfile = CURRENT_PATH + '/db/password_small.txt'
		ret = []
		fp = open(pwdfile,'r')
		for eachline in fp:
			ret.append(eachline)
		self.pwd = ret
		return ret

	def genPwdByZZXRule(self, ruledict=None,rulefile=None):
		'''
		rule dict format example:
			ruledict = {'username':'zhuzhuxia','domain':'knownsec'}
		'''
		if rulefile == None:
			rulefile =  CURRENT_PATH + '/db/rulefile_by_zhuzhuxia.txt'
			#rulefile = 'db/rulefile_by_zhuzhuxia.txt'
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

	def  genPwdByModyRule(self, ruledict=None,rulefile=None):
		'''
		rule dict is a dict, 
			comm: filepath string, list, such as ['123','abc','!@#']
			username: string
			host: string
			connector: tuple, such as ('@','#','_','$')
		'''

		if rulefile == None:
			rulefile =  CURRENT_PATH + '/db/rulefile_by_mody.txt'
			#rulefile = 'db/rulefile_by_zhuzhuxia.txt'
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

	def  genPwdByCupp(self, ruledict=None,rulefile=None):
		''' '''
		pass

	def  export(self, expfile=None):
		''' '''
		if expfile == None:
			expfile = CURRENT_PATH + '/../temp/pwdfiletmp.txt'

		fp = open(expfile,'w')
		for eachpwd in self.pwd:
			fp.write(eachpwd + os.linesep) 
		fp.close()

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	heigepwd = Cupp('superhei')
	ruledict = {'username':'heige','domain':'knownsec'}
	print heigepwd.genPwdByZZXRule(ruledict)
	heigepwd.export()