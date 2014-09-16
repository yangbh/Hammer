#!/usr/bin/python2.7
#coding:utf-8
   
import json
import requests
import time
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
		self.startTime = 0
		self.endTime = 0

	def send(self,data):
		pass

	def task_start(self,taskurl,args=''):
		try:
			serverurl = 'http://' + self.server +'/scans_add.php'
			cookies = {'PHPSESSID':self.phpsession}
			postdata = {'type':'start','url':taskurl,'args':args}

			r = requests.post(serverurl,cookies=cookies,data=postdata)
			if r.status_code == 200 and r.text != '':
			# print r.request.headers
			# print r.request.body
			# print r.text
				self.startTime = json.loads(r.text)['startTime']

		except requests.HTTPError,e:
			print 'requests.HTTPError', e

	def task_end(self,taskurl,retinfo):
		try:
			serverurl = 'http://' + self.server +'/scans_add.php'
			cookies = {'PHPSESSID':self.phpsession}
			retinfo = json.dumps(retinfo)
			# print retinfo
			postdata = {'type':'end','url':taskurl,'startTime':self.startTime,'retinfo':retinfo}

			r = requests.post(serverurl,cookies=cookies,data=postdata)
			# print r.request.headers
			print r.request.body
			print r.text
			if r.status_code == 200:
				# print r.text
				pass
		except requests.HTTPError,e:
			print 'requests.HTTPError', e
		
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	server = 'www.hammer.org'
	phpsession = 'nu6er57bbrjg9digacphs7tl60'
	taskurl = 'http_www.hengtiansoft.com'
	wi = WebInterface(server,phpsession)
	wi.task_start(taskurl)
	print wi.startTime
	time.sleep(2)
	retinfo=[{'content': {u'HTTPServer': {u'string': [u'Microsoft-IIS/6.0']}, u'X-Powered-By': {u'string': [u'ASP.NET']}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://www.hengtiansoft.com/aspnet_client/\tcode:403\nhttp://www.hengtiansoft.com/images/\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/system_web/2_0_50727/\tcode:403\nhttp://www.hengtiansoft.com/images\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/FreeTextBox/\tcode:403\nhttp://www.hengtiansoft.com/upload\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/system_web/2_0_50727\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/system_web/\tcode:403\n', 'type': 'Sensitive File/Directory Discover', 'level': 'low'}, {'content': 'OPTIONS, TRACE, GET, HEAD', 'type': 'IIS PUT Vulnerability', 'level': 'info'}]
	wi.task_end(taskurl,retinfo)