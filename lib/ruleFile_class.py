##!/usr/bin/python2.7
#coding:utf-8

import os
import traceback

from pprint import pprint
from dummy import BASEDIR, LIBDIR

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
class RuleFile(object):
	"""docstring for RuleFile"""
	def __init__(self, rulefile, ruleargs):
		super(RuleFile, self).__init__()
		self.file = rulefile
		self.args = ruleargs
		self.ret = []

	def _repeatOnece(self,rulelines):
		ret = []
		for eachtmp in rulelines:
			if eachtmp.find('%') == -1:
				ret.append(eachtmp)
				continue
			#flag = False
			for eacharg in self.args.keys():
				if eachtmp.find('%'+eacharg+'%') != -1:
					#print 'eacharg=\t',eacharg
					if type(self.args[eacharg]) == str:
						eachtmp = eachtmp.replace('%'+eacharg+'%',self.args[eacharg])
						ret.append(eachtmp)

					elif type(self.args[eacharg]) == list:
						for eachcom in self.args[eacharg]:
							#print 'eachcom=\t',eachcom
							tt = eachtmp.replace('%'+eacharg+'%',eachcom)
							ret.append(tt)
					#flag = True
					break

		# if len(ret) == 0:
		# 	return rulelines
		return ret

	def _getRules(self):
		''' '''
		try:
			fp = open(self.file,'r')
			for eachline in fp:
				if eachline == os.linesep:
					continue
				if eachline[0] == '#':
					continue
				tmp = eachline.replace('\r','')
				tmp = tmp.replace('\n','')
				# tmp = eachline.replace(os.linesep,'')
				# print 'eachline=\t',tmp

				if tmp.find('%') == -1:
					self.ret.append(tmp)
					continue

				rulelines = [tmp]
				#print 'rulelines=\t',rulelines
				flag = True
				while  flag:
					newrulelines = self._repeatOnece(rulelines)
					# print 'oldrulelines=\t',rulelines
					# print 'newrulelines=\t',newrulelines
					# if newrulelines == rulelines:
					# 	break
					flag = False
					for eachline in newrulelines:
						if eachline.find('%') != -1:
							flag = True

					rulelines = newrulelines
				
				self.ret += rulelines

			fp.close()

		except Exception,e:
			print 'Exception',e
			print traceback.format_exc()
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	rulefile = LIBDIR + '/db/compresed_file.rule'
	ruleargs = {'host':'www.eguan.cn','com':['com1','com2']}
	rf = RuleFile(rulefile,ruleargs)
	rf._getRules()
	pprint(rf.ret)