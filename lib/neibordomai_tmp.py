#!/usr/bin/env python

from sys import argv,exit
import urllib2
import urllib
import json

print '\033[1;32m[+]\033[0m Reverse ip lookup by MMxM'

if(len(argv) != 2):
    print '\033[1;36m[*]\033[0m How to use: %s <ip|hostname>'%argv[0]
    exit(1)
try:
    url = 'http://www.yougetsignal.com/tools/web-sites-on-web-server/php/get-web-sites-on-web-server-json-data.php'
    req = urllib2.Request(url)
    req.add_header('Referer', 'http://www.yougetsignal.com/tools/web-sites-on-web-server/')
    params = {"remoteAddress": argv[1]}
    query = urllib.urlencode(params)
    r = urllib2.urlopen(req, query)
    data = json.loads(r.read())
    domain = (data['domainArray'])
    
    print "\n[+] Domains Found:\n"
    
    for s in domain:
        for d in s:
            if d != '':
                print d
except:
    print "[-] Unexpected error"