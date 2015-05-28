#!/usr/bin/python2.7
#coding:utf-8
#	https://github.com/lijiejie/edu-dns-zone-transfer
#	
# import os
# import re

import dns.resolver
import dns.zone

from dummy import * 

info = {
	'NAME':'DNS zone transfer Vulnerability',
	'AUTHOR':'yangbh',
	'TIME':'20140729',
	'WEB':'https://github.com/znb/Scripts/blob/22fab25bd1f158a829f3d1cd471248c0d630fe5e/Networking/zonetransfer.py',
	'DESCRIPTION':' DNS AXFR zone transfer',
	'VERSION':'2',
}
opts = {
	'host':'cau.edu.cn',	#'target ip'
	'timeout':300,
}
# opts = [
# 	['host','cau.edu.cn','target host'],
# 	['timeout',300,'pulgin run max time'],
# ]

def get_ns_records(adomain, aserver=None):
	"""Pull NS records for our domain"""
	logger("Pulling NS records for: " + adomain)
	dresolver = dns.resolver.Resolver()
	if aserver:
		dresolver.nameservers = [aserver]
	ans = dresolver.query(adomain, 'ns')
	ns_list = []            
	try:
		for rdata in ans:
			ns_list.append(rdata)
			logger(rdata)
	except Exception as e:
		logger("Error: %s" % e)
	return ns_list

def zone_transfer(adomain, aserver=None):
	"""Perform zone transfers against our name servers"""
	ns_list = get_ns_records(adomain, aserver)
	dm_list = []
	for server in ns_list:
		logger("> Testing: " + str(server))
		try:
			z = dns.zone.from_xfr(dns.query.xfr(str(server), adomain))
			security_warning("%s %s" %(server,adomain))
			names = z.nodes.keys()
			names.sort()
			for n in names:
				# logger(z[n].to_text(n))
				# logger(n.to_text()+'.'+adomain)
				dm_list.append(n.to_text()+'.'+adomain)
			break

		except Exception as e:
			logger("Error: %s" % e)
	dm_list.sort()
	return dm_list

def Assign(services):
	if services.has_key('host'):
		return True
	return False

def Audit(services):
	try:
		host = services['host']
		dm = zone_transfer(host)
		pprint(dm)
		# if re.search('((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))',host):
		# 	return(None,output)
		# domain = GetFirstLevelDomain(host)
		# logger(domain)

		# cmd_res = os.popen('nslookup -type=ns ' + domain).read()	# fetch DNS Server List
		# # print cmd_res
		# dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
		# for server in dns_servers:
		# 	if len(server) < 5: 
		# 		server += domain
		# 	cmd_res = os.popen('dig @%s axfr %s' % (server, domain)).read()
		# 	# print cmd_res
		# 	if cmd_res.find('Transfer failed.') < 0 and \
		# 			cmd_res.find('connection timed out') < 0 and \
		# 			cmd_res.find('XFR size') > 0 :

		# 		output +=  'Vulnerable dns server found:' + server + os.linesep
		# 		retinfo = {'level':'medium','content':domain}
		# 		security_warning(domain)

		# 采用dnspython库，弃用dig与nslookup


	except Exception,e:
		logger('Exception:%s' % e)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	host = 'cau.edu.cn'
	if len(sys.argv) ==  2:
		host = sys.argv[1]
	services = {'host':host}
	Audit(services)
	pprint(services)