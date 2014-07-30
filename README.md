What's Hammer?
===================================  
A web vulnnerability scanner

Installing
=================================== 

 Require
----------------------------------- 
Required software:
```
dig
whatweb
```
Required python plugins:
```
nmap
httplib
urllib
urllib2
sqlite3
argparse 
json
paramiko
requests
gevent
MySQLdb
pyquery
beautifulsoup4
```

Quick help
===================================  
Basic usage
----------------------------------- 


Available plugins
----------------------------------- 
```
plugins/
├── Info_Collect
│   ├── crawler.py
│   ├── dummy.py
│   ├── __init__.py
│   ├── neighborhost.py
│   ├── portscan.py
│   ├── robots.py
│   ├── subdomain.py
│   └── whatweb.py
├── __init__.py
├── Sensitive_Info
│   ├── backupfile.py
│   ├── compressedfile.py
│   ├── dummy.py
│   ├── __init__.py
│   ├── probefile.py
│   └── senpath.py
├── System
│   ├── dnszone.py
│   ├── dummy.py
│   └── openssl.py
├── Weak_Password
│   ├── dummy.py
│   ├── __init__.py
│   └── sshcrack.py
└── Web_Applications
    ├── discuz7_2fap_php_sqlinject.py
    └── dummy.py
```