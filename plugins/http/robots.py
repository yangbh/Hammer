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

class Robots():
	"""docstring for robots"""
	info = [
		['NAME','robots.txt file check'],
		['AUTHOR','yangbh'],
		['TIME','20140701'],
		['WEB','']
		]
	def run():
		if 'http' in service.keys:
			try:
				url = service['http']['type'] + '://' + service['http']['host'] +':' +service['http']['port'] +'/robots.txt'
				ret = urllib2.urlopen(urlopen).read()

				sensitive_info = url + ret
				security_info = {'level':'low','content',sensitive_info}
				audit_result.append(security_info)
				
			except HTTPError,e:
				pass
