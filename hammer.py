#!/usr/bin/python2.7
#coding:utf-8
import sys
import getopt
sys.path.append(sys.path[0]+'/lib')
#print sys.path
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def usage():
	print "Usage: hammer.py [options] -h host\n"
	print "       -h: host"
	print "\nExamples:"
	print "         ./hammer.py -h www.sohu.com\n"

def main():
	# step1: get arguments
	try :
		opts, args = getopt.getopt(sys.argv[1:], "h:")
	except getopt.GetoptError:
		usage()

	_host = None

	for opt, arg in opts:
		if opt == '-h':
			_host = arg
		else:
			pass
	#bScanAllDomains = False

	if _host == None:
		usage()
		sys.exit()

	# step2: get global services
	import lib.dummy
	from lib.nmap_class import NmapScanner
	np = NmapScanner(_host)
		
	lib.dummy.services = np.scanPorts()
	print lib.dummy.services

	# step3: load plugins
	from lib.pluginLoader_class import PluginLoader
	pl = PluginLoader('plugins')
	pl.loadPlugins()
	print pl.plugindict

	# step4: run plugins
	pl.runPlugins()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()