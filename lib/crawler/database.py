#coding:utf8

"""
database.py
~~~~~~~~~~~~~

该模块提供爬虫所需的sqlite数据库的创建、连接、断开，以及数据的存储功能。
"""

import sqlite3

class Database(object):
	def __init__(self, dbFile=':memory:'):
		super(Database, self).__init__()
		try:
			print 'dbFile:\t',dbFile
			self.conn = None
			# self.conn = sqlite3.connect(dbFile,isolation_level=None, check_same_thread = False) #让它自动commit，效率也有所提升. 多线程共用
			print id(self.conn)
			# self.conn.execute('''CREATE TABLE IF NOT EXISTS
			# 				Webpage (id INTEGER PRIMARY KEY AUTOINCREMENT, 
			# 				url TEXT, 
			# 				pageSource TEXT,
			# 				keyword TEXT)''')
		except Exception, e:
			print 'Exception',e
			self.conn = None

	def isConn(self):
		if self.conn:
			return True
		else:
			return False

	def saveData(self, url, pageSource, keyword=''):
		if self.conn:
			sql='''INSERT INTO Webpage (url, pageSource, keyword) VALUES (?, ?, ?);'''
			self.conn.execute(sql, (url, pageSource, keyword) )
		else :
			raise sqlite3.OperationalError,'Database is not connected. Can not save Data!'

	def close(self):
		if self.conn:
			self.conn.close()
		else :
			raise sqlite3.OperationalError, 'Database is not connected.'

def main():
	database = Database()
	print database.isConn()
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	import multiprocessing
	p = multiprocessing.Pool(8)
	p.apply_async(main)
	p.apply_async(main)
	p.close()
	p.join()
