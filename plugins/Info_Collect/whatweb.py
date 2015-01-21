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
opts = [
	['url','http://testasp.vulnweb.com','target url'],
]

def Assign(services):
	if services.has_key('url'):
		return True
	return False

def Audit(services):
	retinfo = {}
	output = 'plugin run' + os.linesep
	try:
		url = services['url']
		wb = WhatWeb(url)
		wb.scan()
		ret = wb.getResult()
		#print ret
		retinfo = {'level':'info','content':''}
		
		if ret.has_key('plugins'):
			retinfo = {'level':'info','content':ret['plugins']}
			security_info(str(ret['plugins']))
			
			# wordpress
			if ret['plugins'].has_key('WordPress'):
				#print services
				services['cms'] = 'WordPress'
				output += 'cms: WordPress' + os.linesep
				if ret['plugins']['WordPress'].has_key('version'):
					services['cmsversion'] = ret['plugins']['WordPress']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep

			# Discuz
			elif ret['plugins'].has_key('Discuz'):
				#print services
				services['cms'] = 'Discuz'
				output += 'cms: Discuz' + os.linesep
				if ret['plugins']['Discuz'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Discuz']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# AWStats:
			elif ret['plugins'].has_key('AWStats'):
				#print services
				services['cms'] = 'AWStats'
				output += 'cms: AWStats' + os.linesep
				if ret['plugins']['AWStats'].has_key('version'):
					services['cmsversion'] = ret['plugins']['AWStats']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# DeDeCms:
			elif ret['plugins'].has_key('DeDeCms'):
				#print services
				services['cms'] = 'DeDeCms'
				output += 'cms: DeDeCms' + os.linesep
				if ret['plugins']['DeDeCms'].has_key('version'):
					services['cmsversion'] = ret['plugins']['DeDeCms']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# DotNetCMS:
			elif ret['plugins'].has_key('DotNetCMS'):
				#print services
				services['cms'] = 'DotNetCMS'
				output += 'cms: DotNetCMS' + os.linesep
				if ret['plugins']['DotNetCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['DotNetCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# dvbbs:
			elif ret['plugins'].has_key('dvbbs'):
				#print services
				services['cms'] = 'dvbbs'
				output += 'cms: dvbbs' + os.linesep
				if ret['plugins']['dvbbs'].has_key('version'):
					services['cmsversion'] = ret['plugins']['dvbbs']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# Ecshop:
			elif ret['plugins'].has_key('Ecshop'):
				#print services
				services['cms'] = 'Ecshop'
				output += 'cms: Ecshop' + os.linesep
				if ret['plugins']['Ecshop'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Ecshop']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# Emlog:
			elif ret['plugins'].has_key('Emlog'):
				#print services
				services['cms'] = 'Emlog'
				output += 'cms: Emlog' + os.linesep
				if ret['plugins']['Emlog'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Emlog']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# EmpireCMS:
			elif ret['plugins'].has_key('EmpireCMS'):
				#print services
				services['cms'] = 'EmpireCMS'
				output += 'cms: EmpireCMS' + os.linesep
				if ret['plugins']['EmpireCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['EmpireCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# EspCMS:
			elif ret['plugins'].has_key('EspCMS'):
				#print services
				services['cms'] = 'EspCMS'
				output += 'cms: EspCMS' + os.linesep
				if ret['plugins']['EspCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['EspCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# FoosunCMS:
			elif ret['plugins'].has_key('FoosunCMS'):
				#print services
				services['cms'] = 'FoosunCMS'
				output += 'cms: FoosunCMS' + os.linesep
				if ret['plugins']['FoosunCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['FoosunCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# HdWiki:
			elif ret['plugins'].has_key('HdWiki'):
				#print services
				services['cms'] = 'HdWiki'
				output += 'cms: HdWiki' + os.linesep
				if ret['plugins']['HdWiki'].has_key('version'):
					services['cmsversion'] = ret['plugins']['HdWiki']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# Hikvision:
			elif ret['plugins'].has_key('Hikvision'):
				#print services
				services['cms'] = 'Hikvision'
				output += 'cms: Hikvision' + os.linesep
				if ret['plugins']['Hikvision'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Hikvision']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# KesionCMS:
			elif ret['plugins'].has_key('KesionCMS'):
				#print services
				services['cms'] = 'KesionCMS'
				output += 'cms: KesionCMS' + os.linesep
				if ret['plugins']['KesionCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['KesionCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# KingCMS:
			elif ret['plugins'].has_key('KingCMS'):
				#print services
				services['cms'] = 'KingCMS'
				output += 'cms: KingCMS' + os.linesep
				if ret['plugins']['KingCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['KingCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# LjCMS:
			elif ret['plugins'].has_key('LjCMS'):
				#print services
				services['cms'] = 'LjCMS'
				output += 'cms: LjCMS' + os.linesep
				if ret['plugins']['LjCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['LjCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# PHP168:
			elif ret['plugins'].has_key('PHP168'):
				#print services
				services['cms'] = 'PHP168'
				output += 'cms: PHP168' + os.linesep
				if ret['plugins']['PHP168'].has_key('version'):
					services['cmsversion'] = ret['plugins']['PHP168']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# phpCMS:
			elif ret['plugins'].has_key('phpCMS'):
				#print services
				services['cms'] = 'phpCMS'
				output += 'cms: phpCMS' + os.linesep
				if ret['plugins']['phpCMS'].has_key('version'):
					services['cmsversion'] = ret['plugins']['phpCMS']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# PHPWind:
			elif ret['plugins'].has_key('PHPWind'):
				#print services
				services['cms'] = 'PHPWind'
				output += 'cms: PHPWind' + os.linesep
				if ret['plugins']['PHPWind'].has_key('version'):
					services['cmsversion'] = ret['plugins']['PHPWind']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# PowerEasy:
			elif ret['plugins'].has_key('PowerEasy'):
				#print services
				services['cms'] = 'PowerEasy'
				output += 'cms: PowerEasy' + os.linesep
				if ret['plugins']['PowerEasy'].has_key('version'):
					services['cmsversion'] = ret['plugins']['PowerEasy']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# qiboSoft:
			elif ret['plugins'].has_key('qiboSoft'):
				#print services
				services['cms'] = 'qiboSoft'
				output += 'cms: qiboSoft' + os.linesep
				if ret['plugins']['qiboSoft'].has_key('version'):
					services['cmsversion'] = ret['plugins']['qiboSoft']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# SiteServer:
			elif ret['plugins'].has_key('SiteServer'):
				#print services
				services['cms'] = 'SiteServer'
				output += 'cms: SiteServer' + os.linesep
				if ret['plugins']['SiteServer'].has_key('version'):
					services['cmsversion'] = ret['plugins']['SiteServer']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# southidc:
			elif ret['plugins'].has_key('southidc'):
				#print services
				services['cms'] = 'southidc'
				output += 'cms: southidc' + os.linesep
				if ret['plugins']['southidc'].has_key('version'):
					services['cmsversion'] = ret['plugins']['southidc']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep
			# Zoomla:
			elif ret['plugins'].has_key('Zoomla'):
				#print services
				services['cms'] = 'Zoomla'
				output += 'cms: Zoomla' + os.linesep
				if ret['plugins']['Zoomla'].has_key('version'):
					services['cmsversion'] = ret['plugins']['Zoomla']['version'][0]
					output += 'cmsversion: ' + services['cmsversion'] + os.linesep

			# HTTPServer
			if ret['plugins'].has_key('HTTPServer'):
				if ret['plugins']['HTTPServer'].has_key('string'):
					# string key is a list, so use [0]
					services['HTTPServer'] = ret['plugins']['HTTPServer']['string'][0]
					output += 'HTTPServer: ' + services['HTTPServer'] + os.linesep

			# X-Powered-By
			if ret['plugins'].has_key('X-Powered-By'):
				if ret['plugins']['X-Powered-By'].has_key('string'):
					# string key is a list, so use [0]
					services['X-Powered-By'] = ret['plugins']['X-Powered-By']['string'][0]
					output += 'X-Powered-By: ' + services['X-Powered-By'] + os.linesep

		elif False:
			pass
		
		return (retinfo,output)

	except urllib2.URLError,e:
		#print 'urllib2.URLError: ',e
		output += 'urllib2.URLError: ' + str(e) + os.linesep
	except urllib2.HTTPError,e:
		#print 'urllib2.HTTPError: ',e
		output += 'urllib2.HTTPError: ' + str(e) + os.linesep
	except TypeError, e:
		#print 'TypeError: ',e
		output += 'TypeError: ' + str(e) + os.linesep
	except Exception,e:
		output += 'Exception: ' + str(e) + os.linesep
		
	return (retinfo,output)
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