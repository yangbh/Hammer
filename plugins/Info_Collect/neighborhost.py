#!/usr/bin/python2.7
#coding:utf-8

import socket
from lib.neighborHost_class import NeighborHost

info = {
	'NAME':'Neighborhood-Host Scanning',
	'AUTHOR':'yangbh',
	'TIME':'20140709',
	'WEB':'',
}

def Audit(services):
	if services.has_key('ip') and 'isneighborhost' not in services.keys():
		neighborhosts = []
		nbh = NeighborHost(services['ip'])
		neighborhosts = nbh.getFromChinaZ()

		services['neighborhosts'] = neighborhosts