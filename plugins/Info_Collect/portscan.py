#!/usr/bin/python2.7
#coding:utf-8

import os
from lib.nmap_class import NmapScanner

info = {
	'NAME':'Port and Service Discover',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
}

def Audit(services):
	if services.has_key('ip') and 'isneighborhost' not in services.keys():
		ip = services['ip']
		np = NmapScanner(ip)
		sc = np.scanPorts()
		#print sc
		try:
			services['ip'] = sc.keys()[0]
			services['ports'] = []
			services['detail'] = {}
			if sc[sc.keys()[0]].has_key('tcp'):
				services['detail'].update(sc[sc.keys()[0]]['tcp'])
				for eachport in sc[sc.keys()[0]]['tcp']:
					services['ports'].append(eachport)
			if sc[sc.keys()[0]].has_key('udp'):
				services['detail'].update(sc[sc.keys()[0]]['udp'])
				for eachport in sc[sc.keys()[0]]['udp']:
					services['ports'].append(eachport)

			#print 'services:\t',services

			retinfo = {'level':'info','content':str(services['ports'])}

		except IndexError,e:
			print 'IndexError:',e
			output += 'IndexError: ' + str(e) + os.linesep
		except KeyError,e:
			print 'KeyError:',e
			output += 'KeyError: ' + str(e) + os.linesep
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services={'ip':'124.160.91.86'}
	Audit(services)