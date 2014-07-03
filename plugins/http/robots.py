#!/usr/bin/python2.7
#coding:utf-8

# global variables
# service = {'http':
# 				{'type':'https',
# 				'host':'www.baidu.com,
# 				'port':'80',
# 				'cms':{'name':'Discuz',
#					'version':'v7'}},
# 			'ftp':
# 				{'ip':'111.111.111.111',
# 				'port','21'}}

import urllib2

class Robots():
	"""docstring for robots"""
	info = [
		['NAME','robots.txt file check'],
		['AUTHOR','yangbh'],
		['TIME','20140701'],
		['WEB','']
		]
		
	def run(self,services):
			if services.has_key('url'):
				try:
					url = services['url'] + 'robots.txt'
					print url
					ret = urllib2.urlopen(url).read()
					security_info = {'type':'sensitive info','level':'low','content':url+ret}
				#except urllib2.HTTPError,e:
				except TypeError, e:
					pass
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	rb = Robots()
	rb.run(services)