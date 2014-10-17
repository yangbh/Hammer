What's Hammer?
===================================  
A web vulnnerability scanner

Install
=================================== 

		目前建议在kali上运行：
		1. 数据库导入sql文件，地址在temp/hammer.sql
		2. 配置web，修改web目录下config配置文件
		3. 将plugins目录下所有插件内容导入web数据库
      1)修改lib/plugin2sql.py 内的server 和 token（token在user.php中获取）
      2)hammer#python lib/plugin2sql.py plugins/
		4. 运行python hammer.py 进行扫描

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
   ██░ ██  ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
  ▓██░ ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
  ▒██▀▀██░▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
  ░▓█ ░██ ░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
  ░▓█▒░██▓ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ▒ ░▒░ ░  ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
   ░  ░░ ░  ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
   ░  ░  ░      ░  ░       ░          ░      ░  ░   ░     
  
	
Usage: hammer.py [options] -u url

[options]
	-s --server: your hammer web server host address, like www.hammer.org
	-t --token: token, find it in http://www.hammer.org/user.php
	-h: help
[Examples]
	hammer.py --s www.hammer.org --t MLDl15DwC6vqGrBoRto32hEnVjMxoCoB -u http://www.leesec.com
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