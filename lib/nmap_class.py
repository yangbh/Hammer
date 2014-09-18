#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import sys
import nmap
from pprint import pprint

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class NmapScanner(object):
	"""docstring for nmapScanner_class"""
	# https tcp-443
	# imaps tcp-993
	# pop3s tcp-995
	# smtps tcp-465
	commonports = '21,22,23,25,110,53,67,80,443,1521,1526,3306,3389,8080,8580'
	commonports += ',465,993,995'
	def __init__(self, hosts,ports=commonports,arguments='-sV '):
		super(NmapScanner, self).__init__()
		self.hosts = hosts
		self.ports = ports
		self.arguments = arguments
		try:	
			self.nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
		except nmap.PortScannerError:
			print('Nmap not found', sys.exc_info()[0])
			sys.exit(0)

	def scanPorts(self):
		''' '''
		hosts = self.hosts
		ports = self.ports
		arguments = self.arguments
		self.nm.scan(hosts=hosts,ports=ports,arguments=arguments)
		# clear state:down host
		# clear state:closed port
		ret = {}
		for host in self.nm.all_hosts():
			if self.nm[host].state() != 'up':
				continue
			else:
				ret[host] = self.nm[host]
				for port in ret[host]['tcp'].keys():
					if ret[host]['tcp'][port]['state'] != 'open':
						ret[host]['tcp'].pop(port)
		
		return ret
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	np = NmapScanner('www.eguan.cn')
	pprint(np.scanPorts())

