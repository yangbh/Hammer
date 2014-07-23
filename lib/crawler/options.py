#!/usr/bin/python2.7
#coding:utf-8

# ----------------------------------------------------------------------------------------------------
# filename: options.py
# func: 该模块定义了程序接收的命令行参数，提供参数的默认值与格式。
# author: lvyaojia
# web: https://github.com/lvyaojia/crawler
# modifed by mody at 2014-07-23
# ----------------------------------------------------------------------------------------------------

import argparse 

_default = dict(
	logfile = 'spider.log',
	dbFile = 'data.sql',
	loglevel = 3,
	threadNum = 10,
	keyword = '',
	)

def positiveInt(rawValue):
	errorInfo = "Must be a positive integer."
	try:
		value = int(rawValue)
	except ValueError:
		raise argparse.ArgumentTypeError(errorInfo)
	if value < 1:
		raise argparse.ArgumentTypeError(errorInfo)
	else:
		return value

def url(rawValue):
	value =  None
	if not rawValue.startswith('http'):
		value = 'http://' + rawValue
	return value

parser = argparse.ArgumentParser(description='A Web crawler for Knownsec') 

parser.add_argument('-u', type=str, required=True, metavar='URL', dest='url',
				   help='Specify the begin url')

parser.add_argument('-d', type=positiveInt, required=True, metavar='DEPTH', dest='depth',
				   help='Specify the crawling depth')

parser.add_argument('--logfile', type=str, metavar='FILE', default=_default['logfile'], dest='logFile',
				   help='The log file path, Default: %s' % _default['logfile'])

parser.add_argument('--loglevel', type=int, choices=[1, 2, 3, 4, 5], default=_default['loglevel'], dest='logLevel',
				   help='The level of logging details. Larger number record more details. Default:%d' % _default['loglevel'])

parser.add_argument('--thread', type=positiveInt, metavar='NUM', default=_default['threadNum'], dest='threadNum',
				   help='The amount of threads. Default:%d' % _default['threadNum'])

parser.add_argument('--dbfile', type=str, metavar='FILE', default=_default['dbFile'], dest='dbFile',
				   help='The SQLite file path. Default:%s' % _default['dbFile'])

parser.add_argument('--key', type=str, metavar='KEYWORD', default=_default['keyword'], dest='keyword',
				   help='The keyword for crawling. Default: None. For more then one word, quote them. example: --key \'Hello world\'')

parser.add_argument('--testself',action='store_true',dest='testSelf',
				   help='Crawler self test')

#spider.py -u url -d deep -f logfile -l loglevel(1-5)  --testself -thread number --dbfile  filepath  --key=”HTML5”
#Namespace(dbFile='data.sql', depth=3, keyword=None, logFile='spider.log', logLevel=3, testSelf=False, threadNum=10, url='baidu.com')
def main():
	args = parser.parse_args()
	print args
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()