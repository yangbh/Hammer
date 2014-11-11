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
	
Usage: hammer.py [Options] [Targets]

[Options]
	-s --server: your hammer web server host address, like www.hammer.org
	-t --token: token, find it in http://www.hammer.org/user.php
	-U --update-plugins: update new added plugins to web
	-h: help
[Targets]
	-T --target: target, can be an ip address, an url or an iprange
[Examples]
	hammer.py -s www.hammer.org -t 3r75... -U plugins/Info_Collect/
	hammer.py -s www.hammer.org -t 3r75... -T http://www.leesec.com
	hammer.py -s www.hammer.org -t 3r75... -T 192.168.1.0/24
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
	1)登录web，在user.php中获取token，执行更新插件:
	python hammer.py -s www.hammer.org -t yourtokenhere -U plugins/
	2) 以后若添加插件，可以-U指定单独.py插件，也可以指定目录
	python hammer.py -s www.hammer.org -t yourtokenhere -U yourpluginfilepath
4. 运行hammer.py进行扫描
	python hammer.py -s www.hammer.org -t yourtokenhere -T yourtargethere
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
ipaddress	# for handling input ip
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