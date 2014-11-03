What's Hammer?
===================================  
A web vulnerability scanner framework

Basic usage
===================================  

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
	hammer.py -s www.hammer.org -t 3r75... -u http://www.leesec.com/
```

Install
=================================== 

```
目前建议在kali上运行：
```
```
1. 数据库导入sql文件，地址在temp/hammer.sql
2. 配置web，修改web目录下config配置文件
3. 将plugins目录下所有插件内容导入web数据库
	1)修改lib/plugin2sql.py 内的server 和 token（token在user.php中获取）
	2)hammer#python lib/plugin2sql.py plugins/
4. 运行python hammer.py 进行扫描
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
# framework basic
futures		# for Parallel Processing
argparse 	# for input handling
sqlite3		# for local database
MySQLdb
beautifulsoup4	# for crawler
＃ used in plugins
python-nmap	# for nmap scanning
httplib		# for http request
urllib
urllib2
requests
paramiko	# for ssh cracker
easywebdav	# for webdav
json		# others
pyquery
```