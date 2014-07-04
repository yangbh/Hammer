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
# info = {'type':'robots.txt',  
#		'level':'low',
#		'url': vulnerability url,
#		'content':content
#		}

import urllib2

"""docstring for robots"""
info = [
		['NAME','robots.txt file check'],
		['AUTHOR','yangbh'],
		['TIME','20140701'],
		['WEB','']
		]
		
def Audit(services):
		#print 'Audit run'
		#print services
		#print security_info
		if services.has_key('url'):
			try:
				url = services['url'] + 'robots.txt'
				#print url
				ret = urllib2.urlopen(url).read()
				retinfo = {'type':'robots.txt info','level':'info','url':url,'content':ret}
				
				return retinfo
			#except urllib2.HTTPError,e:
			except TypeError, e:
				pass
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	rb = Robots()
	rb.run(services)