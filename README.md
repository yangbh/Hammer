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
	   --auto-proxy: 启用自动代理
	-h : 输出帮助信息
[Targets]
	-T --target: 目标，可以为ip、host、url或ip范围,当使用－p模式时还可以是文件
	   --no-gather: 不使用信息收集模块，也可以用下面的--gather-depth=0实现
	   --gather-depth: 信息收集深度，默认为1
	   --conf-file: 配置文件，默认为conf/basic.conf
	-p --plugin: 单独跑一个插件
	   --plugin-arg: 插件参数，格式为"port=20;name='hammer';"
	-l --listen: 监听模式，在WEB上进行任务分配
	   --max-size: listen模式的最大线程池
	--console: 控制台模式
[Examples]
	hammer.py -s www.hammer.org -t 3r75... --update-plugins plugins/Info_Collect/
	hammer.py -s www.hammer.org -t 3r75... --console
	hammer.py -T http://testphp.vulnweb.com
	hammer.py --conf-file conf/basic.conf
	hammer.py -T vulnweb.com --conf-file conf/basic.conf
	hammer.py -p plugins/System/dnszone.py -T vulnweb.com
	hammer.py -l
```

Install
=================================== 

```
目前建议在Linux/Mac上运行，Mac上请用brew安装pip：
```
```
1. 安装python依赖库
	sudo apt-get install python-pip python-dev
	sudo pip install -r requirement.txt
2. 下载项目
	~$>git clone https://github.com/yangbh/Hammer.git & cd Hammer
	Hammer$>git clone https://github.com/yangbh/Hammer.git
	以后更新就可以直接用git pull origin master解决了
3. 数据库
	1）mysql>create database Hammer;
	2) 并为Hammer数据库分配账户密码
	3）导入sql文件，地址在bin/hammer.sql
	source bin/hammer.sql
4. 配置web，修改web/config.php配置文件
	$DB_HOST = 'localhost';
	$DB_PORT = '3306';
	$DB_NAME = 'Hammer';	
	$DB_USER = 'user';
	$DB_PWD = 'password';	
	$DB_SALT = 'hammer';	# salt是盐，建议修改，改动后请手动修改数据库中web admin密码hash
5. 将plugins目录下所有插件内容导入web数据库
	1) 登录web，默认账号密码为admin/123456,在user.php中获取token
	2) 将本地插件信息更新至WEB:
	python hammer.py -s www.hammer.org -t yourtokenhere -u plugins/
	3) 以后若添加插件，可以-u指定单独.py插件，也可以指定目录
	python hammer.py -s www.hammer.org -t yourtokenhere -u yourpluginfilepath
6. 运行hammer.py进行扫描
	1) 第一次使用－c模式设置本地缓存server和token
	python hammer.py -c
	anonymous@local >set server 0xff.sinaapp.com
	anonymous@local >set token XiUfga4xlS4ajBWnlUyBph9wGRxlFHF3
	anonymous@local >connect
	admin@0xff.sinaapp.com >show user
	2) 若未设置token，则以后的扫描需要带上server和token，具体扫描命令参考web/documents.php,常用的命令：
	python hammer.py -l
	python hammer.py -T yourtargethere
7. 推荐使用web进行任务分发，在configs.php中设置插件参数
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