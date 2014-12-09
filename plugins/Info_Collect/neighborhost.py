#!/usr/bin/python2.7
#coding:utf-8

import os
import socket
from dummy import *

info = {
	'NAME':'Neighborhood-Host Scanning',
	'AUTHOR':'yangbh',
	'TIME':'20140709',
	'WEB':'',
	'DESCRIPTION':'旁站扫描',
	'VERSION':'1.0',
	'RUNLEVEL':0
}

def Assign(services):
	if services.has_key('ip'):
		return True
	return False

def Audit(services):
	retinfo = {}
	output = ''
	# print 'logger=',logger
	logger('plugin run')
	neighborhosts = []
	nbh = NeighborHost(services['ip'])
	neighborhosts = nbh.getFromChinaZ()
	# print 'neighborhosts=\t',neighborhosts
	logger('neighborhosts=\t'+str(neighborhosts))
	if neighborhosts and len(neighborhosts) != 0:
		services['neighborhosts'] = neighborhosts
		ret = neighborhosts
		retinfo = {'level':'info','content':ret}
		for each_neighbor in neighborhosts:
			security_note(each_neighbor)
			add_scan_task(each_neighbor)

	return (retinfo,output)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	# www.leesec.com
	services = {'ip':'61.164.42.190'}
	print Audit(services)
	pprint(services)