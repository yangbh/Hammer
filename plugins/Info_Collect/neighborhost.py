#!/usr/bin/python2.7
#coding:utf-8

import os
import socket

info = {
	'NAME':'Neighborhood-Host Scanning',
	'AUTHOR':'yangbh',
	'TIME':'20140709',
	'WEB':''
}

def Audit(services):
	output = ''
	if services.has_key('ip'):
		output += 'plugin run' + os.linesep
		neighborhosts = []
		nbh = NeighborHost(services['ip'])
		neighborhosts = nbh.getFromChinaZ()

		services['neighborhosts'] = neighborhosts

	else:
		output += 'plugin does not run' + os.linesep

	return (None,output)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	from dummy import *
	# www.leesec.com
	services = {'ip':'106.187.37.47'}
	print Audit(services)
	pprint(services)