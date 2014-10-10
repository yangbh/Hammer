What's Hammer?
===================================  
A web vulnnerability scanner

Install
=================================== 
```
目前建议再kali上运行：
1. 数据库导入sql文件，地址再temp/hammer.sql
2. 配置web，修改config文件
3. 修改lib/scanner_class_mp.py中的session，并运行python lib/scanner_class_mp.py http://www.leesec.com
```
 Require
----------------------------------- 
Required software:
```
python2.7
ruby
dig
whatweb
```

Required python plugins:
```
python-nmap
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
easywebdav
```

Quick help
===================================  
Basic usage
----------------------------------- 
```
	####################################################
	##
	##
	##
	##	
	##	author	:  yangbh
	##	email  	:  
	####################################################
	
Usage: hammer.py [options] -u url

	-u --url: url address, like http://www.leesec.com/
	-h: help

Examples:
	hammer.py -u http://www.leesec.com/
```

Available plugins
----------------------------------- 
```
plugins/
├── Common
│   └── fileinclusion.py
├── Info_Collect
│   ├── crawler.py
│   ├── neighborhost.py
│   ├── portscan.py
│   ├── robots.py
│   ├── subdomain.py
│   └── whatweb.py
├── Sensitive_Info
│   ├── backupfile.py
│   ├── compressedfile.py
│   ├── probefile.py
│   └── senpath.py
├── System
│   ├── iismethod.py
│   ├── iisshort.py
│   ├── openssl.py
│   ├── phpmyadmin_null_password.py
│   └── webdav.py
├── Weak_Password
│   └── sshcrack.py
└── Web_Applications
    ├── bo_blog_tag_php_xss.py
    ├── espcms_search_inject.py
    ├── espcms_sql_inject.py
    ├── shopex_phpinfo_disclosure.py
    └── wordpress_reflect_xss.py
```