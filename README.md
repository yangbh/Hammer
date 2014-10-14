What's Hammer?
===================================  
A web vulnnerability scanner

Install
=================================== 

目前建议在kali上运行：
1. 数据库导入sql文件，地址在temp/hammer.sql
2. 将plugins目录下所有插件内容导入数据库
```
1)修改lib/plugin2sql.py 内的数据库地址、账户、密码
2)hammer#python lib/plugin2sql.py plugins/
```
可以先导入本地，导出Plugins表，再导入到Hammer数据库（关键是没写添加plugin的web接口，这个有点很蛋疼，待改）
3. 配置web，修改web目录下config配置文件
4. 修改lib/scanner_class_mp.py中的web服务器server和session
5. 运行python lib/scanner_class_mp.py 进行扫描

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