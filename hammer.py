#!/usr/bin/python2.7
#coding:utf-8

import sys
import getopt

# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def show():
	print'''
	####################################################
	##
	##
	##
	##	
	##	author	:  yangbh
	##	email  	:  
	####################################################
	'''

def usage():
	print "Usage: hammer.py [options] -u url\n"
	print "\t-u --url: url address, like http://www.leesec.com/"
	print "\t-h: help"
	print "\nExamples:"
	print "\thammer.py -u http://www.leesec.com/\n"
	sys.exit(0)

def main():
	# step1: get arguments
	show()
	try :
		opts, args = getopt.getopt(sys.argv[1:], "hu:")
	except getopt.GetoptError:
		usage()

	_url = None

	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt == '-u':
			_url = arg
		else:
			pass
	if _url == None:
		usage()

	# step2: init syspath
	basepath = sys.path[0]
	sys.path.append(basepath +'/lib')
	sys.path.append(basepath +'/plugins')
	sys.path.append(basepath +'/bin')

	# step3: run scans
	from lib.scanner_class import Scanner
	
	sn =Scanner(_url)
	sn.getServices()
	print sn.startScan()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	main()