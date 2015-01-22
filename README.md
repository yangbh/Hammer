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
	
Usage: hammer.py [Auth] [Options] [Targets]

[Auth]
	-s --server: web server地址，为域名或ip
	-t --token: token，在用户－设置界面可用找到并更新
[Options]
	-u --update-plugins: 更新本地插件至web，可用指定本地插件目录
	-v --verbose: 输出内容更加详细，默认输出内容为info，－v则为debug
	   --threads: 进程数量，默认为cpu核数
	-h : 输出帮助信息
[Targets]
	-T --target: 目标，可以为ip、host、url或ip范围,当使用－p模式时还可以是文件
	   --no-gather: 不使用信息收集模块，也可以用下面的--gather-depth=0实现
	   --gather-depth: 信息收集深度，默认为1
	-p --plugin: 单独跑一个插件
	   --plugin-arg: 插件参数，格式为"port=20;name='hammer';"
	-l --listen: 监听模式，在WEB上进行任务分配
	-c --console: 控制台模式
[Examples]
	hammer.py -s www.hammer.org -t 3r75... -u plugins/Info_Collect/
	hammer.py -s www.hammer.org -t 3r75... -T http://testphp.vulnweb.com
	hammer.py -s www.hammer.org -t 3r75... -p plugins/System/iisshort.py -T target
	hammer.py -s www.hammer.org -t 3r75... -l
```

Install
=================================== 

```
目前建议在kali上运行：
```
```
1. 安装python依赖库
	sudo apt-get install python-pip python-dev build-essential
	sudo pip install -r requirement.txt
2. 数据库导入sql文件，地址在bin/hammer.sql
3. 配置web，修改web目录下config配置文件
4. 将plugins目录下所有插件内容导入web数据库
	1) 登录web，默认账号密码为admin/123456,在user.php中获取token
	2) 将本地插件信息更新至WEB:
	python hammer.py -s www.hammer.org -t yourtokenhere -u plugins/
	3) 以后若添加插件，可以-u指定单独.py插件，也可以指定目录
	python hammer.py -s www.hammer.org -t yourtokenhere -u yourpluginfilepath
5. 运行hammer.py进行扫描
	python hammer.py -s www.hammer.org -t yourtokenhere -T yourtargethere
```
 Require
----------------------------------- 
Required software:
```
python2.7
ruby
# dig
# whatweb
```

Required python plugins:
```
# framework basic
futures		# for Parallel Processing
argparse 	# for input handling
#sqlite3		# for local database
#MySQL-python
beautifulsoup4	# for crawler
#ipaddress	# for handling input ip
netaddr		# for handling input ip range
# used in plugins
python-nmap	# for nmap scanning
dnspython	# for dns zone transfer
#httplib		# for http request
#urllib
#urllib2
requests
paramiko	# for ssh cracker
pymongo		# for mongodb
easywebdav	# for webdav
#json		# others
pyquery
```