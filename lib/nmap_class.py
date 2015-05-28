#!/usr/bin/python2.7
#coding:utf-8
'''

'''
import sys
import nmap
from pprint import pprint

# refer to http://zone.wooyun.org/content/18959

commonports = '21,22,23,25,110,53,67,80,1521,1526,3306,3389,4899,8580'
commonports += ',137'			# netbios
commonports += ',161'			# snmp
commonports += ',873'			# rsync default port
commonports += ',443,465,993,995'	# ssl services port
	# https tcp-443
	# imaps tcp-993
	# pop3s tcp-995
	# smtps tcp-465
commonports += ',1900'			# SSDP Discovery Service，xp可能沦为DDOS源
commonports += ',2082,2083' 	# cpanel主机管理系统登陆 （国外用较多）​
commonports += ',2222'  		# DA虚拟主机管理系统登陆 （国外用较多）​
commonports += ',2601,2604'		# zebra路由，默认密码zebra 
commonports += ',3128'			# squid代理默认端口，如果没设置口令很可能就直接漫游内网了 
commonports += ',3312,3311'  	# kangle主机管理系统登陆
commonports += ',4440'			# rundeck  参考WooYun: 借用新浪某服务成功漫游新浪内网 
commonports += ',6082'			# varnish  参考WooYun: Varnish HTTP accelerator CLI 未授权访问易导致网站被直接篡改或者作为代理进入内网 
commonports += ',6379'			# redis 一般无认证，可直接访问
commonports += ',7001'			# weblogic，默认弱口令
commonports += ',7778' 			# Kloxo主机控制面板登录​
commonports += ',8000-9090'	# 都是一些常见的web端口，有些运维喜欢把管理后台开在这些非80的端口上 
commonports += ',8080'			# tomcat/WDCP主机管理系统 默认端口
commonports += ',8888'  		# amh/LuManager 主机管理系统默认端口
commonports += ',8083' 			# Vestacp主机管理系统​​ （国外用较多）
commonports += ',8089' 			# jboss端口 历史曾经爆漏洞/可弱口令
commonports += ',9200'			# elasticsearch port
commonports += ',10000' 		# Virtualmin/Webmin 服务器虚拟主机管理系统
commonports += ',11211'			# memcache  未授权访问 
commonports += ',11211'			# memcache  未授权访问 
commonports += ',28017,27017'	# mongodb default port
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
class NmapScanner(object):
	"""docstring for nmapScanner_class"""


	# def __init__(self, hosts,ports=commonports,arguments='-sV '):
	def __init__(self, hosts,ports=commonports,arguments=' '):
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
		self.nm.scan(hosts=hosts,ports=commonports,arguments=arguments)
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
	ip='172.16.3.5'
	if len(sys.argv) ==  2:
		ip = sys.argv[1]
	np = NmapScanner(ip)
	pprint(np.scanPorts())

