import string
import httplib, sys
import myparser
import re
import time

class search_baidu:
	def __init__(self,word,limit,start):
		self.word=word.replace(' ', '%20')
		self.results=""
		self.totalresults=""
		self.server="www.baidu.com"
		#self.apiserver="api.search.live.net"
		self.hostname="www.baidu.com"
		self.userAgent="(Mozilla/5.0 (Windows; U; Windows NT 6.0;zh-cn; rv:1.9.2) Gecko/20100115 Firefox/3.6"
		self.quantity="50"
		self.limit=int(limit)
		self.bingApi=""
		self.counter=start
		
	def do_search(self):
		h = httplib.HTTP(self.server)
		h.putrequest('GET', "/s?wd=%40" + self.word + "&rn=100&pn="+ str(self.counter))
		h.putheader('Host', self.hostname)
		h.putheader('Cookie: H_PS_PSSID=4454_1421_4414_4261_4202_4587; BAIDUID=ABE16F3C528AB718BFDBAAAA76626AC3:SL=0:NR=100:FG=1; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; sug=3; bdime=0; BD_TMP_CK=true')
		h.putheader('Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
		h.putheader('User-agent', self.userAgent)	
		h.endheaders()
		returncode, returnmsg, headers = h.getreply()
		self.results = h.getfile().read()
		self.totalresults+= self.results
	def process(self):
		while self.counter <= self.limit:
			self.do_search()
			# print "\tSearching "+ str(self.counter) + " results..."
			self.counter+=100		
	def get_emails(self):
		rawres=myparser.parser(self.totalresults,self.word)
		return rawres.emails()
	
	def get_hostnames(self):
		rawres=myparser.parser(self.totalresults,self.word)
		return rawres.hostnames()
	
	def get_allhostnames(self):
		rawres=myparser.parser(self.totalresults,self.word)
		return rawres.hostnames_all()