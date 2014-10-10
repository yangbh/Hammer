#!/usr/bin/python2.7
#coding:utf-8

import os
import socket
from dummy import *

info = {
	'NAME':'Neighborhood-Host Scanning',
	'AUTHOR':'yangbh',
	'TIME':'20140709',
	'WEB':''
}

def Audit(services):
	retinfo = {}
	output = ''
	if services.has_key('ip'):
		output += 'plugin run' + os.linesep
		neighborhosts = []
		nbh = NeighborHost(services['ip'])
		neighborhosts = nbh.getFromChinaZ()
		#print 'neighborhosts=\t',neighborhosts
		if neighborhosts and len(neighborhosts) != 0:
			services['neighborhosts'] = neighborhosts
			ret = neighborhosts
			retinfo = {'level':'info','content':ret}
			if services.has_key('noSubprocess') and services['noSubprocess'] == True:
				pass
			else:
				security_note(str(services['ports']))

	# else:
	# 	output += 'plugin does not run' + os.linesep

	return (retinfo,output)

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	# www.leesec.com
	services = {'ip':'106.187.37.47'}
	print Audit(services)
	pprint(services)