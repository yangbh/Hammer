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
opts = [
	['ip','61.164.42.190','target ip'],
]
def Assign(services):
	if services.has_key('ip'):
		return True
	return False

def Audit(services):
	# print 'logger=',logger
	# logger('plugin run')
	neighborhosts = []
	nbh = NeighborHost(services['ip'])
	neighborhosts = nbh.getFromChinaZ()
	# print 'neighborhosts=\t',neighborhosts
	logger('neighborhosts=\t'+str(neighborhosts))
	if neighborhosts and len(neighborhosts) != 0:
		services['neighborhosts'] = neighborhosts
		for each_neighbor in neighborhosts:
			security_note(each_neighbor)
			if services.has_key('nogather') and services['nogather'] == True:
				pass
			else:
				add_scan_task(each_neighbor)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	ip = '222.84.126.197'
	if len(sys.argv) ==  2:
		ip = sys.argv[1]
	services = {'ip':ip}
	print Audit(services)
	pprint(services)