#!/usr/bin/python2.7
#coding:utf-8

import os
import re
import urllib2
from dummy import *

info = {
	'NAME':'Web Application Recognition',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
	'DESCRIPTION':'CMS识别',
	'VERSION':'1.0',
	'RUNLEVEL':1
}
opts = {
	'url':'http://www.sel.zju.edu.cn',	#'target ip'
	'timeout':300,
}
# opts = [
# 	['url','http://www.sel.zju.edu.cn','target url'],
# 	['timeout',300,'pulgin run max time'],
# ]

def Assign(services):
	if services.has_key('url'):
		return True
	return False

def Audit(services):
	try:
		url = services['url']
		wb = WhatWeb(url)
		wb.scan()
		ret = wb.getResult()
		
		if ret.has_key('plugins'):
			retinfo = {'level':'info','content':ret['plugins']}
			security_info(str(ret['plugins']))
			
			# 概率大的放在前面
			# already test
			# wordpress
			if ret['plugins'].has_key('WordPress'):
				#print services
				services['cms'] = 'WordPress'
				if ret['plugins']['WordPress'].has_key('version'):
					services['cmsversion'] = ret['plugins']['WordPress']['version'][0]

			# Discuz
			elif ret['plugins'].has_key('Discuz'):
				#print services
				services['cms'] = 'Discuz'
				if ret['plugins']['Discuz'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Discuz']['version'][0]
			
			# not test yet
			# AWStats:
			elif ret['plugins'].has_key('AWStats'):
				#print services
				services['cms'] = 'AWStats'
				if ret['plugins']['AWStats'].has_key('version'):
					services['cmsversion'] = ret['plugins']['AWStats']['version'][0]
			# DeDeCms:
			elif ret['plugins'].has_key('DeDeCms'):
				#print services
				services['cms'] = 'DeDeCms'
				if ret['plugins']['DeDeCms'].has_key('version'):
					services['cmsversion'] = ret['plugins']['DeDeCms']['version'][0]
			# DotNetCMS:
			elif ret['plugins'].has_key('DotNetCMS'):
				#print services
				services['cms'] = 'DotNetCMS'
				if ret['plugins']['DotNetCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['DotNetCMS']['version'][0]
			# dvbbs:
			elif ret['plugins'].has_key('dvbbs'):
				#print services
				services['cms'] = 'dvbbs'
				if ret['plugins']['dvbbs'].has_key('version'):
					services['cmsversion'] = ret['plugins']['dvbbs']['version'][0]
			# Ecshop:
			elif ret['plugins'].has_key('Ecshop'):
				#print services
				services['cms'] = 'Ecshop'
				if ret['plugins']['Ecshop'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Ecshop']['version'][0]
			
			# miss version
			# Emlog:
			elif ret['plugins'].has_key('Emlog'):
				#print services
				services['cms'] = 'Emlog'
				if ret['plugins']['Emlog'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Emlog']['version'][0]
			# EmpireCMS:
			elif ret['plugins'].has_key('EmpireCMS'):
				#print services
				services['cms'] = 'EmpireCMS'
				if ret['plugins']['EmpireCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['EmpireCMS']['version'][0]
			# EspCMS:
			elif ret['plugins'].has_key('EspCMS'):
				#print services
				services['cms'] = 'EspCMS'
				if ret['plugins']['EspCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['EspCMS']['version'][0]
			# FoosunCMS:
			elif ret['plugins'].has_key('FoosunCMS'):
				#print services
				services['cms'] = 'FoosunCMS'
				if ret['plugins']['FoosunCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['FoosunCMS']['version'][0]
			# HdWiki:
			elif ret['plugins'].has_key('HdWiki'):
				#print services
				services['cms'] = 'HdWiki'
				if ret['plugins']['HdWiki'].has_key('version'):
					services['cmsversion'] = ret['plugins']['HdWiki']['version'][0]
			# Hikvision:
			elif ret['plugins'].has_key('Hikvision'):
				#print services
				services['cms'] = 'Hikvision'
				if ret['plugins']['Hikvision'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Hikvision']['version'][0]
			# KesionCMS:
			elif ret['plugins'].has_key('KesionCMS'):
				#print services
				services['cms'] = 'KesionCMS'
				if ret['plugins']['KesionCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['KesionCMS']['version'][0]
			# KingCMS:
			elif ret['plugins'].has_key('KingCMS'):
				#print services
				services['cms'] = 'KingCMS'
				if ret['plugins']['KingCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['KingCMS']['version'][0]
			# LjCMS:
			elif ret['plugins'].has_key('LjCMS'):
				#print services
				services['cms'] = 'LjCMS'
				if ret['plugins']['LjCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['LjCMS']['version'][0]
			# PHP168:
			elif ret['plugins'].has_key('PHP168'):
				#print services
				services['cms'] = 'PHP168'
				if ret['plugins']['PHP168'].has_key('version'):
					services['cmsversion'] = ret['plugins']['PHP168']['version'][0]
			# phpCMS:
			elif ret['plugins'].has_key('phpCMS'):
				#print services
				services['cms'] = 'phpCMS'
				if ret['plugins']['phpCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['phpCMS']['version'][0]
			# PHPWind:
			elif ret['plugins'].has_key('PHPWind'):
				#print services
				services['cms'] = 'PHPWind'
				if ret['plugins']['PHPWind'].has_key('version'):
					services['cmsversion'] = ret['plugins']['PHPWind']['version'][0]
			# PowerEasy:
			elif ret['plugins'].has_key('PowerEasy'):
				#print services
				services['cms'] = 'PowerEasy'
				if ret['plugins']['PowerEasy'].has_key('version'):
					services['cmsversion'] = ret['plugins']['PowerEasy']['version'][0]
			# qiboSoft:
			elif ret['plugins'].has_key('qiboSoft'):
				#print services
				services['cms'] = 'qiboSoft'
				if ret['plugins']['qiboSoft'].has_key('version'):
					services['cmsversion'] = ret['plugins']['qiboSoft']['version'][0]
			# SiteServer:
			elif ret['plugins'].has_key('SiteServer'):
				#print services
				services['cms'] = 'SiteServer'
				if ret['plugins']['SiteServer'].has_key('version'):
					services['cmsversion'] = ret['plugins']['SiteServer']['version'][0]
			# southidc:
			elif ret['plugins'].has_key('southidc'):
				#print services
				services['cms'] = 'southidc'
				if ret['plugins']['southidc'].has_key('version'):
					services['cmsversion'] = ret['plugins']['southidc']['version'][0]
			# Zoomla:
			elif ret['plugins'].has_key('Zoomla'):
				#print services
				services['cms'] = 'Zoomla'
				if ret['plugins']['Zoomla'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Zoomla']['version'][0]

			# HTTPServer
			if ret['plugins'].has_key('HTTPServer'):
				if ret['plugins']['HTTPServer'].has_key('string'):
					# string key is a list, so use [0]
					services['HTTPServer'] = ret['plugins']['HTTPServer']['string'][0]
				if ret['plugins']['HTTPServer'].has_key('os'):
					# string key is a list, so use [0]
					services['os'] = ret['plugins']['HTTPServer']['os'][0]
			
			if ret['plugins'].has_key('Microsoft-IIS'):
				if ret['plugins']['Microsoft-IIS'].has_key('version'):
					# string key is a list, so use [0]
					services['Microsoft-IIS'] = ret['plugins']['Microsoft-IIS']['version'][0]

			# X-Powered-By
			if ret['plugins'].has_key('X-Powered-By'):
				if ret['plugins']['X-Powered-By'].has_key('string'):
					# string key is a list, so use [0]
					services['X-Powered-By'] = ret['plugins']['X-Powered-By']['string'][0]

		elif False:
			pass
		
	except Exception,e:
		pass		
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	import sys
	url='http://www.eguan.cn'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)