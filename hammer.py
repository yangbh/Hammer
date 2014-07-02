#!/usr/bin/python2.7
#coding:utf-8
import sys
import getopt
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def usage():
	print "Usage: hammer.py [options] -h host\n"
	print "       -h: host"
	print "       -p: port, default 80"
	print "\nExamples:"
	print "         ./hammer.py -h www.sohu.com\n"

def main():
	try :
		opts, args = getopt.getopt(sys.argv[1:], "h:p:")
	except getopt.GetoptError:
		usage()

	_host = None
	_port = 80

	for opt, arg in opts:
		if opt == '-h':
			_host = arg
		elif opt == '-p':
			_port = arg
		else:
			pass
	#bScanAllDomains = False

	if _host == None:
		usage()
		sys.exit()

	services = {'http':{'host':_host,
					'port':_port,
					'cms':{'name':'WordPress',
						'version':'3.9.3'}}}
	print services
	

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()