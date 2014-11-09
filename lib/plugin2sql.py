#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import MySQLdb
import requests
from dummy import BASEDIR
from mysql_class import MySQLHelper
from common import addslashes
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
def write2sql(filepath=None):
	try:
		filepath = os.path.realpath(filepath)
		print 'loading', filepath
		info = runEachPlugin(filepath)
		fp = open(filepath,'r')
		code = fp.read()
		fp.close()

		sql = MySQLHelper('localhost','ham_usr','ham_pwd')
		sql.selectDb('Hammer')

		pName = addslashes(info['NAME'])
		pType = os.path.basename(os.path.dirname(filepath))
		pAuthor = ''
		if info.has_key('AUTHOR'):
			pAuthor = addslashes(info['AUTHOR'])
		pTime = ''
		if info.has_key('TIME'):
			pTime = addslashes(info['TIME'])
		pVersion = ''
		if info.has_key('VERSION'):
			pVersion = addslashes(info['VERSION'])
		pWeb = ''
		if info.has_key('WEB'):
			pWeb = addslashes(info['WEB'])
		pDescription = ''
		if info.has_key('DESCRIPTION'):
			pDescription = addslashes(info['DESCRIPTION'])
		pCode = addslashes(code)

		# sql.cur.execute("INSERT INTO Plugin(Name,Type,Author,Time,Version,Web,Description,Code) VALUES(?,?,?,?,?,?,?,?)" % (pName,pType,pAuthor,pTime,pVersion,pWeb,pDescription,pCode))
		sqlcmd = "INSERT INTO Plugin(Name,Type,Author,Time,Version,Web,Description,Code) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (pName,pType,pAuthor,pTime,pVersion,pWeb,pDescription,pCode)
		# print sqlcmd
		sql.cur.execute(sqlcmd)
		sql.commit()
		sql.close()

	except TypeError,e:
		print e
	except MySQLdb.Error,e:
		print e

def write2web(filepath=None,server='localhost',token=''):
	try:
		filepath = os.path.realpath(filepath)
		print 'loading', filepath
		info = runEachPlugin(filepath)
		fp = open(filepath,'r')
		code = fp.read()
		fp.close()

		pName = info['NAME']
		pType = os.path.basename(os.path.dirname(filepath))
		pAuthor = ''
		if info.has_key('AUTHOR'):
			pAuthor = info['AUTHOR']
		pTime = ''
		if info.has_key('TIME'):
			pTime = info['TIME']
		pVersion = ''
		if info.has_key('VERSION'):
			pVersion = info['VERSION']
		pWeb = ''
		if info.has_key('WEB'):
			pWeb = info['WEB']
		pDescription = ''
		if info.has_key('DESCRIPTION'):
			pDescription = info['DESCRIPTION']
		pCode = code

		# send to  web server
		serverurl = 'http://' + server +'/plugins_add.php'
		# cookies = {'PHPSESSID':token}
		postdata = {'name':pName,'type':pType,'token':token,'author':pAuthor,'time':pTime,'version':pVersion,'web':pWeb,'description':pDescription,'code':pCode}
		print postdata
		r = requests.post(serverurl,data=postdata)
		print r.status_code,r.text
		if r.status_code == 200:
		# print r.request.headers
			# print r.text
			pass
		else:
			print 'return error, please check token and server'
		pass

	except TypeError,e:
		print e
	except MySQLdb.Error,e:
		print e


def runEachPlugin(pluginfilepath):
	# print '>>>running plugin:',pluginfilepath
	modulepath = pluginfilepath.replace(BASEDIR+'/plugins/','')
	
	modulepath = modulepath.replace('.py','')
	modulepath = modulepath.replace('.','')
	modulepath = modulepath.replace('/','.')
	print 'modulepath',modulepath

	importcmd = 'from ' + modulepath + ' import info'
	exec(importcmd)

	# print importcmd
	# print sys.path
	print info
	return info

def loadPlugins(path=None,server='localhost',token=''):
	print '>>>loading plugins'
	if path == None:
		return None
	if os.path.isdir(path) == True:	
		ret = {}
		for root, dis, files in os.walk(path):  
			ret[root] =[]
			for eachfile in files:
				if eachfile != '__init__.py' and '.pyc' not in eachfile and eachfile != 'dummy.py' and eachfile.endswith('.py'):
					ret[root].append(root + '/' + eachfile)
					# write2sql(root + '/' + eachfile)
					write2web(root + '/' + eachfile,server,token)
		# print ret
	elif os.path.isfile(path) == True:
		basename = os.path.basename(path)
		if basename != '__init__.py' and '.pyc' not in basename and basename != 'dummy.py':
			# write2sql(path)
			write2web(path,server,token)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	server = 'www.hammer.org'
	# server = '0xff.sinaapp.com'
	token = 'PNykhMYzMSOMevsNU9SZzmdUgi6t85Cn'
	if len(sys.argv) ==  2:
		filepath = sys.argv[1]
		loadPlugins(filepath,server,token)