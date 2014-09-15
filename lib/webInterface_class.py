#!/usr/bin/python2.7
#coding:utf-8

import requests

# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
class WebInterface(object):
	"""docstring for webInterface"""
	def __init__(self,server,phpsession):
		super(WebInterface, self).__init__()
		self.server = server
		if phpsession  and type(phpsession) == str and len(phpsession) == 26:
			self.phpsession = phpsession
		else:
			raise SystemExit,  "invalid phpsession for class WebInterface"

	def send(self,data):
		pass

	def task_start(self):
		url = 'http://' + self.server +'scans_add.php'
		cookies = {'PHPSESSID':self.phpsession}
		postdata = {type:'start'}
		r = requests.post(url,cookies=cookies,data=postdata)
		# print r.status_code

	def task_end(self):
		pass
		
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	server = 'www.hammer.org'
	phpsession = 'gnfbujhdggue8bbd489l5hfg44'
	wi = WebInterface(server,phpsession)
	wi.task_start()