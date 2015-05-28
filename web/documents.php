<?php
require_once('common.php');
?>

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="">
		<meta name="author" content="">
		<link rel="icon" href="images/favicon.ico">

		<title>Hammer</title>
		<!-- Bootstrap core CSS -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		
		<!-- Custom styles for this template -->
		<!-- <link href="css/dashboard.css" rel="stylesheet"> -->

		<!-- <link href="css/responsive-nav.css" rel="stylesheet"> -->
		
		<!-- JQuery -->
		<script src="js/jquery.min.js"></script>

		<script src="js/bootstrap.min.js"></script>

		<!-- a<script src="js/responsive-nav.js"></script> -->

		<!-- google code prettify -->
		<link href="js/prettify.css" type="text/css" rel="stylesheet" />
		<script type="text/javascript" src="js/prettify.js"></script>
		<style type="text/css">
			pre {
				display: block;
				padding: 9.5px;
				margin: 0 0 10px;
				font-size: 13px;
				line-height: 20px;
				word-break: break-all;
				word-wrap: break-word;
				white-space: pre;
				white-space: pre-wrap;
				background-color: #f5f5f5;
				border: 1px solid #ccc;
				border: 1px solid rgba(0, 0, 0, 0.15);
				-webkit-border-radius: 4px;
				   -moz-border-radius: 4px;
						border-radius: 4px;
			}
			li.L0, li.L1, li.L2, li.L3,li.L5, li.L6, li.L7, li.L8{
				list-style-type: decimal !important
			}
		</style>

		<script type="text/javascript">
		$(document).ready(function(){
			prettyPrint();
			$("#myNav").affix({
				offset: { 
					top: 100
				}
			});
		});
		</script>

	</head>

	<body>
		<div class="navbar navbar-inverse navbar-default" role="navigation" style="border-radius: 0px;">
			<div class="container">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar">1</span>
						<span class="icon-bar">2</span>
						<span class="icon-bar">3</span>
					</button>
					<a class="navbar-brand" href="#" style="padding: 5px;">
						<img src="images/logo.ico" class="" style="width: 40px;height: 40px;">
					</a>
					<a class="navbar-brand" href="#">
						<strong>Hammer</strong>
					</a>
				</div>
				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">
						<li><a href="index.php">Home</a></li>
						<?php if (already_login()) {echo '<li><a href="scans.php">Scans</a></li>';}?>
						<li><a href="plugins.php">Plugins</a></li>
						<?php if (already_login()) {echo '<li><a href="configs.php">Configs</a></li>';}?>
						<li class="active"><a href="documents.php">Documents</a></li>
						<li><a href="about.php">About</a></li>
					</ul>
<?php
if (already_login()) {
	$username = $_SESSION['user'];
echo <<<EOF
					<ul class ="nav navbar-nav navbar-right">
						<li class="dropdown">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown" onmouseover="$(this).dropdown('toggle');">
								<i class="glyphicon glyphicon-user"></i> $username<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li role="presentation">
									<a href="task.php"><i class="glyphicon glyphicon-tasks"></i> Tasks</a>
								</li>
								<li role="presentation">
									<a href="dist.php"><i class="glyphicon glyphicon-tower"></i> Workers</a>
								</li>
								<li role="presentation">
									<a href="user.php"><i class="glyphicon glyphicon-cog"></i> Setting</a>
								</li>
								<li role="presentation">
									<a href="logout.php"><i class="glyphicon glyphicon-off"></i> Logout</a>
								</li>
						</li>
					</ul>
EOF;
}
else{
echo <<<EOF
					<form class="navbar-form navbar-right" role="form" action="login.php" method="post">
						<div class="form-group">
							<input type="text" placeholder="Name" class="form-control" name="username" id="username">
						</div>
						<div class="form-group">
							<input type="password" placeholder="Password" class="form-control" name="password" id="password">
						</div>
						<button type="submit" class="btn btn-success">Sign in</button>
					</form>
EOF;
}
?>

				</div><!--/.navbar-collapse -->
			</div>
		</div>


		<!-- Main jumbotron for a primary marketing message or call to action -->
		<div class="container">

			<div class="row row-offcanvas row-offcanvas-right">

				<div class="col-xs-2 col-sm-2 col-md-2" id="myScrollspy">
					<ul class="nav nav-tabs nav-stacked" id="myNav" style="margin: 0px;width: 80px;">
						<li><a href="#">关于</a></li>
						<li><a href="#run">运行</a></li>
						<li><a href="#plugin">插件</a></li>
						<li><a href="#framework">框架</a></li>
						<li><a href="#questions">问题</a></li>
						<li><a href="#contact">联系</a></li>
					</ul>
				</div>

				<div class="col-xs-10 col-sm-10 col-md-10" role="main" class="main">

					<h2 id="about">关于</h2>
						<p>Hammer 不只是一款网络扫描器，更是一个扫描框架，Hammer类似开源的yascanner（当然，目前功能还远不如yascanner，yascanner是我的偶像），与yascanner类似，它偏向于WEB漏洞的收集与检测，不太具有攻击性.</p>
						<p>开源不易，希望大家也能够开源出自己的插件，一起打造自己的锤子！！！</p>
					<hr>
					<h2 id="run">运行</h2>
						<p></p>
						<pre class="prettyprint linenums Lang-python">
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
	-s --server: your hammer web server host address, like www.hammer.org
	-t --token: token, find it in http://www.hammer.org/user.php
[Options]
	-u --update-plugins: update new added plugins to web
	-v --verbose: increase verbosity level
	   --threads: max number of process, default cpu number
	-h: help
[Targets]
	-T --target: target, can be an ip address, an url or an iprange
	   --no-gather: do not use information gather module
	   --gather-depth: information gather depth, default 1
	-p --plugin: run a plugin type scan
	   --plugin-arg: plugin argus
	-l --listen: listen mode
	   --max-size: scan pool max size, default 50
	-c --console: console mode
[Examples]
	hammer.py -s www.hammer.org -t 3r75... -u plugins/Info_Collect/
	hammer.py -s www.hammer.org -t 3r75... -T 192.168.1.1/24
	hammer.py -s www.hammer.org -t 3r75... -p plugins/System/iisshort.py -T target</pre>
						<h3>1. 四种运行模式————自收集扫描模式、批量扫描模式、listen模式、console模式</h3>
						<pre>
1. 常规的类似yascanner自收集扫描模式，扫描目标为一个ip、host、url，系统会自动搜集该target相关目标
hammer.py -s www.hammer.org -t 3r75... -T www.leesec.com
例如：	python hammer.py -s www.hammer.org -t 4aSJWhngmZdhAvkCGt6ODVhHTQ1R4Jzz -T 73.50.49.151

2. 批量扫描模式，可以是ip范围，也可以－T 从本地文件载入目标host、url等
hammer.py -s www.hammer.org -t 3r75... -p plugins/System/iisshort.py -T 192.168.1.0/24
例如：	python hammer.py -s www.hammer.org -t 4aSJWhngmZdhAvkCGt6ODVhHTQ1R4Jzz -p plugins/Info_Collect/portscan.py -T 73.50.49.151
	python hammer.py -s www.hammer.org -t 4aSJWhngmZdhAvkCGt6ODVhHTQ1R4Jzz -p plugins/System/mongodb_unauth_access.py --plugin-arg "ports=[27017]" -T 73.50.49.151／30

3. listen模式，在此模式下可以通过WEB实现简单的分布式管理
hammer.py -hammer.py -s www.hammer.org -t 3r75... -l [-v]

4. console模式，类似mst，扫描结果存入WEB服务器中
hammer.py -hammer.py -s www.hammer.org -t 3r75... -c
此模式下可以在本地缓存server和token等信息，因此第二次使用不需要再带上server和token参数，直接可以：
hammer.py -c
hammer.py -l
hammer.py -T http://testphp.vulnweb.com</pre>
						<h3>2. 详细参数解释</h3>
						<pre class="prettyprint linenums Lang-python">
[Auth]
	-s --server: web server地址，为域名或ip
	-t --token: token，在用户－设置界面可用找到并更新
[Options]
	-u --update-plugins: 更新本地插件至web，可用指定本地插件目录
	-v --verbose: 输出内容更加详细，默认输出内容为info，－v则为debug
	   --threads: 进程数量，默认为cpu核数
[Targets]
	-T --target: 目标，可以为ip、host、url或ip范围,当使用－p模式时还可以是文件
	   --no-gather: 不使用信息收集模块，也可以用下面的--gather-depth=0实现
	   --gather-depth: 信息收集深度，默认为1
	-p --plugin: 单独跑一个插件
	   --plugin-arg: 插件参数，格式为"port=20;name='hammer';"
	-l --listen: 监听模式，在WEB上进行任务分配
	-c --console: 控制台模式</pre>
						<h3>3. listen模式详解</h3>
						<p>listen模式下每个运行hammer.py -l 终端都会被充当成工作worker，并进行持续查询服务器是否存在扫描任务</p>
						<p>web服务器也充当任务分发的角色</p>
						
						<hr>
						<h3>4. console模式详解</h3>
						<p>console模式下的命令有</p>
						<pre class="prettyprint linenums Lang-bash">
HAMMER COSOLE COMMAND HELP MENU
=============
        COMMAND         DESCRIPTION                       EXAMPLE
        -------         -----------                       -----------
	help		Displays the help menu            help
	exit		Exit the Hammer console mode      exit
	cls 		Clear the screen                  cls
	set 		Set server and token              set PARAM VALUE
	connect 	Connect to server                 connect
	show 		List the plugins                  show info|com|sens|sys|pwd|web|all|user
	search 		Search plugins                    search plugin
	use 		Use the plugin                    use plugin|pluginID
PLUGIN HELP MENU
================
        COMMAND         DESCRIPTION                       EXAMPLE
        -------         -----------                       -----------
	help            Displays the plugin menu          help
	back            Back to Mst Main                  back
	cls             Clear the screen                  cls
	info            Displays the plugin info          info
	opts            Displays the mst options          opts
	set             Configure the plugin parameters   set PARAM VALUE
	run             Start plugin to run               run</pre>
						<p>首次使用需要登录</p>
						<pre class="prettyprint linenums Lang-bash">
Hammer$ python hammer.py -c
Seems user info not inited File not open for reading
Seems user info not inited 'NoneType' object has no attribute '__getitem__'
[!] Err:has not logged in, please log in first!
[!] Err:cannot concatenate 'str' and 'NoneType' objects
[*] Start hammer console ..

	   ██░ ██  ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
	  ▓██░ ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
	  ▒██▀▀██░▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
	  ░▓█ ░██ ░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
	  ░▓█▒░██▓ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
	   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
	   ▒ ░▒░ ░  ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
	   ░  ░░ ░  ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
	   ░  ░  ░      ░  ░       ░          ░      ░  ░   ░     

          =[ HAMMER::My Sec Tools
    + -- +=[ PLU::info::5 com::2 sens::5 sys::10 pwd::2 web::13
anonymous@local >set server 0xff.sinaapp.com
anonymous@local >set token XiUfga4xlS4ajBWnlUyBph9wGRxlFHF3
anonymous@local >connect
admin@0xff.sinaapp.com >show user
SHOW USER INFORMATION
=====================
	server:		0xff.sinaapp.com
	token:		XiUfga4xlS4ajBWnlUyBph9wGRxlFHF3
	user id:	1
	user name:	admin
	scan id:	247
==========================================================================</pre>
					<p>接下来就可以使用插件了</p>
					<pre class="prettyprint linenums Lang-bash">
admin@0xff.sinaapp.com >search iis
SEARCH 'iis'
============
   ID PATH                                                         TYPE   
----- ------------------------------------------------------------ -------
   15 System/iismethod                                             System 
   16 System/iisshort                                              System 
==========================================================================
COUNT [2] RESULTS (*^_^*)
admin@0xff.sinaapp.com >use 15
hammer System[ iismethod ] >info
PLUGIN INFOS
============
PARAMETER       VALUE
--------------- --------------------
WEB             
DESCRIPTION     When iis enable PUT or MOVE method, attacker can upload a webshell
TIME            20140731
NAME            IIS Method Scanner
AUTHOR          yangbh
hammer System[ iismethod ] >opts
PLUGIN OPTS
===========
PARAMETER       VALUE                DESCRIPTION                             
--------------- -------------------- ----------------------------------------
url             http://testasp.vulnweb.com target url                              
hammer System[ iismethod ] >run
[*] Start run..
[2015-01-22 13:53:14,431] - [WARNING] - 247 0xff.sinaapp.com XiUfga4xlS4ajBWnlUyBph9wGRxlFHF3 http://testasp.vulnweb.com IIS Method Scanner OPTIONS, TRACE, GET, HEAD
hammer System[ iismethod ] ></pre>
					<p>登录状态下会将结果保存至web server中</p>					
					<hr>
					<h2 id="plugin">插件</h2>
					<p>下面是一个典型的Hammer插件，功能为扫描robots.txt文件存在与否:</p>
					<pre class="prettyprint linenums Lang-python">
#!/usr/bin/python2.7
#coding:utf-8

import requests
# 导入hammer模块各种库
from dummy import *

# 插件信息
info = {
	'NAME':'Robots.txt Sensitive Information',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':'',
	'DESCRIPTION':'robots.txt文件扫描',
}
# 插件所需参数，格式类似msf/mst
opts = [
	['url','http://www.leesec.com','target url'],
]
# 任务分配函数Assign
def Assign(services):
	if services.has_key('url'):
		return True
	return False

# 漏洞检测函数Audit
def Audit(services):
	url = services['url']+ '/robots.txt'
	rq = requests.get(url,allow_redirects=False,timeout=30)
	if rq.status_code == 200 and 'Disallow: ' in rq.text:
		# 漏洞反馈函数security
		security_note(url) 
		# 调试输出函数logger,默认等级为debug
		logger('Find %srobots.txt' % url)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.leesec.com'}
	pprint(services)</pre>
					<h3>1. 插件的命名</h3>
					<pre class="prettyprint linenums Lang-python">
正确命名方式如下，第一个字母不能为数字，且文件名内不能有空格，可以以_下划线代替
├── CMS53KF_file_download.py
├── Comsenz_uctools.py
├── DeDecms5_7_plus_recommend_php_injection.py
├── DeDecms5_7minggan_info.py
例如下方式都为错误
53KF_file_download.py
Comsenz uctools.py
错误命名时，将导致插件不能被调用与导入
</pre>	
					<p>一个标准的插件信息info变量，如下：</p>
					<h3>2. 插件信息info和插件参数opts</h3>
					<p>一个标准的插件信息info变量，如下：</p>
					<pre class="prettyprint linenums Lang-python">
info = {
	'NAME':'Robots.txt Sensitive Information',	# 插件名称，必须唯一，建议命名方式一致，首写字母大写
	'AUTHOR':'yangbh',		# 插件作者，不能为空
	'TIME':'20140707',		# 插件编写时间，不能为空，格式要保持一致：yyyymmdd
	'WEB':'http://',		# 漏洞参考，以逗号分开
	'DESCRIPTION':'robots.txt文件扫描',		# 插件简要描述
	'Version':'0.1'			# 插件版本号
}</pre>
<p>一个标准的插件参数opts变量，如下：</p>
					<pre class="prettyprint linenums Lang-python">
opts是一个python list 类型，其中每个变量参数由变量名、变量默认值以及变量含有组成
opts = [
	['url','http://www.leesec.com','target url'],
]
注意：在hammer中opts变量的值不仅可以为python的string类型，而且可以是dict、list类型，例如mongodb_unauth_access插件
opts = [
	['ip','221.123.140.66','target ip'],
	['ports',[27017],'target ip\'s ports']
]
其中ports参数的值就是list类型
在console模式下可以使用 set ports [27017,28017]重新赋值</pre>
					<h3>3. 插件类型</h3>
					<p>Hammer的插件总共分为以下七种类型，请将相应的插件放在对应的目录下。</p>
					<pre class="prettyprint linenums Lang-python">
Info Collect	# 信息收集类插件，目录：plugins/Info_Collect, 注意这类的插件最先运行!

Common		# 普通类插件，目录：plugins/Common
Sensitive Info	# 敏感信息类插件，目录：plugins/Sensitive_Info
System		# 系统类插件，目录：plugins/System
Web Applications	# WEB应用类插件，目录：plugins/Web_Applications
Weak Password	# 弱口令类插件，目录：plugins/Weak_Password
Others		# 其它类型插件，目录：plugins/Others</pre>
					<p>请一定注意Info_Collect类插件，这类插件最先运行，将一些信息收集类的插件放在这个目录（如会改动services全局变量的插件），其它的插件的运行顺序未知，这点会在以后优化。</p>
					<h3>4. 全局变量&插件参数services</h3>
					<p>services是一个全局变量，插件的参数，dict类型，内含信息收集阶段运行的信息.</p>
					<p>键以及其含义：</p>
					<pre class="prettyprint linenums Lang-python">
services = {
	# 常用的
	'ip':'127.0.0.1',	# 被扫描的ip地址
	'host':'www.hammer.org',	#被扫描的host域名
	'url':'http://www.hammer.org',	#被扫描的url
	'cms':'Wordpress',	# cms类型，基于whatweb扫描结果分析，详情请参考whatweb插件
	'cmsversion':'3.9.1',	# cms版本，同上 
	'ports': [22,80],	# 端口号
	'port_detail':{22:{}},	# 端口详情，具体参考portscan插件
	'webserver',		# web server 类型，为Tomcat、Apache、IIS或者其他
	'webserverversion',	# web server 版本
	
	# 不常用		
	'alreadyrun'		# 是否已经作为信息收集模块运行过
	'nogather'			# 是否需要收集，例如－p模式默认为True，不需要收集信息

	# 弃用
	'noSubprocess': True,	# 是否是子进程
	'issubdomain': True,	# 是否是子域名
}</pre>
					<p>services变量很开放，是全局变量，意味着你可以在你的插件中修改它的值，或者增加你所需要的键，但是修改的时候请慎重！插件的调用的实现方式请参考pluginLoader_class.py</p>
					<p>注：services自从插件单独以进程方式运行时有个坑，请参考portscan.py插件。</p>
					<h3>5. 插件接口函数Assign/Audit</h3>
					<p></p>
					<pre class="prettyprint linenums Lang-python">
# 任务分配函数Assign
# 	函数功能：进行任务分配，决定是满足进入Audit条件
# 	参数：	为前面讲一节的service变量，和yascanner略有区别
# 	返回值：	为True or False
def Assign(services):
	if services.has_key('url'):
		return True
	return False

# 漏洞检测函数Audit
# 	函数功能：进行漏洞检测，判断是否存在漏洞
# 	参数：	同上，前面讲一节的service变量，和yascanner有区别
# 	返回值：	已取消(之前版本有return (ret,output)，其中ret为扫描返回结果，output为调试输出内容，引入web接口和调试接口logger之后废除)
def Audit(services):
	url = services['url']+ '/robots.txt'
	rq = requests.get(url,allow_redirects=False,timeout=30)
	if rq.status_code == 200 and 'Disallow: ' in rq.text:
		# 漏洞反馈函数security
		security_note(url) 
		# 调试输出函数logger,默认等级为
		logger('Find %srobots.txt' % url)</pre>
					<h3>6. 漏洞反馈接口security_info等</h3>
					<p>漏洞反馈可以通过以下四个函数实现，参数都是字符串型</p>
					<pre class="prettyprint linenums Lang-python">
security_note(vulninfo) 	# information level
security_info(vulninfo) 	# low level 
security_warning(vulninfo) 	# mideum level
security_hole(vulninfo) 	# high level</pre>
					<p>请自己参考漏洞危害酌情选择对应的接口函数。</p>
					<h3>7. 调试输出接口logger</h3>
					<pre class="prettyprint linenums Lang-python">
logger(debuginfo) # debuginfo为string类型，输出插件运行信息，单独运行参见时为print函数，整体运行时为logging.debug函数</pre>
					<h3>8. 添加子扫描任务接口add_target</h3>
					<p>除此之外还有一个添加子扫描任务模块</p>
					<pre class="prettyprint linenums Lang-python">
add_target(target) 		# target可以为url\ip\host之一</pre>
					<p>注意：这个函数只能作为信息收集模块内使用，即放在Infor_Collect目录下，可以参考subdomain.py插件。</p>
					<h3>9. Hammer框架之dummy.py</h3>
					<p>dummy.py是仿照yascanner的，是统一导入hammer框架的一些类库，结构有些牛头马面不成样子，在每个目录都得放一个，目前暂未有好的方法解决，留待后期吧</p>
					<pre class="prettyprint linenums Lang-python">
#!/usr/bin/python2.7
#coding:utf-8

import os
import sys

# BASEDIR 为hammer的工作目录
BASEDIR = os.path.realpath(__file__).replace('/plugins/Sensitive_Info/dummy.pyc','')
BASEDIR = BASEDIR.replace('/plugins/Sensitive_Info/dummy.py','')

from pprint import pprint
# 在 common 模块导入漏洞反馈函数、调试输出接口等函数
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# very important
# here it is common, not lib.common, because of python import strategies
from common import genFilename,security_note,security_info,security_warning,security_hole,add_target
from common import logger
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 其它的一些类及函数
from lib.ruleFile_class import RuleFile
# from lib.nmap_class import NmapScanner
# from lib.neighborHost_class import NeighborHost
# from lib.knock_class import SubDomain
# from lib.theHarvester_class import TheHarvester
# from lib.whatWeb_class import WhatWeb
from lib.spider.domain import GetFirstLevelDomain
from lib.crawler.crawlerFile import CrawlerFile</pre>
					<hr>
					<h2 id="framework">框架</h2>
					<h3>1. 插件调用的实现</h3>
					<p>插件调用类在lib/pluginLoader_class.py，实现步骤为：</p>
					<p>1).导入插件的Assign函数，若存在，则运行并判断返回值，Ture则继续运行，否则退出</p>
					<p>2).导入插件的Audit函数，运行，反馈扫描结果，输出调试信息</p>
					<p></p>
					<pre class="prettyprint linenums Lang-python">
# 尝试导入Assign函数
try:
	importcmd = 'global services' + os.linesep
	importcmd += 'from ' + modulepath + ' import Assign'
	# globalVar.mainlogger.debug('importcmd='+importcmd)
	exec(importcmd)
	globalVar.mainlogger.debug('load Assign success')
	self._saveRunningInfo('load Assign success'+os.linesep)
except Exception,e:
	globalVar.mainlogger.debug('Exception: Import Assign Failed\t:'+str(e))
# 尝试导入Audit函数 以及 info变量
try:
	importcmd = 'global services' + os.linesep
	importcmd += 'from ' + modulepath + ' import info,Audit'
	exec(importcmd)
	globalVar.mainlogger.debug('load info and Audit success')
	self._saveRunningInfo('load info and Audit success'+os.linesep)
except Exception,e:
	globalVar.mainlogger.debug('Exception: Import info and Audit Failed\t:'+str(e))

# 获得Assign函数结果
retflag = True
if locals().has_key('Assign'):
	retflag = False
	retflag = Assign(services)

if retflag and locals().has_key('Audit'):
	# 运行Audit扫描函数
	try:
		Audit(services)
		# ret,output = Audit(services)
	except Exception,e:
		globalVar.mainlogger.error('Audit Function Exception:\t'+str(e))

	# services info
	if self.services != services:
		self.services = services
		globalVar.mainlogger.warning('services changed to:\t' + str(services))
		self._saveRunningInfo('services changed to:\t' + str(services) + os.linesep)</pre>
					<p>services前文提到过，修改的原理就再此，修改时请慎重！</p>
					<h3>2. whatweb识别cms</h3>
					<p>本工具中的cms识别采用的是whatweb，有一个whatweb类，在lib/whatWeb_class.py。</p>
					<p>考虑到原生的whatweb的插件众多，影响扫描效率，所以在lib/whatweb目录下是一个经过插件简化的whatweb。PS：注意kali下whatweb会自动包含/usr/local/share/whatweb目录下的插件，所以也注释了下whatweb的几行代码，有空再找出来细说。</p>
					<p>Hammer的whatweb插件位于Info_Collect目录下，仍需补充完善，结构如下：</p>
					<pre class="prettyprint linenums Lang-python">
def Audit(services):
	if services.has_key('url'):
		try:
			url = services['url']
			wb = WhatWeb(url)
			wb.scan()
			ret = wb.getResult()
			#print ret
			retinfo = {'level':'info','content':''}
			
			if ret.has_key('plugins'):
				retinfo = {'level':'info','content':ret['plugins']}
				security_info(str(ret['plugins']))
				
				# wordpress
				if ret['plugins'].has_key('WordPress'):
					#print services
					services['cms'] = 'WordPress'
					if ret['plugins']['WordPress'].has_key('version'):
						services['cmsversion'] = ret['plugins']['WordPress']['version'][0]

				# Discuz
				elif ret['plugins'].has_key('Discuz'):
					#print services
					services['cms'] = 'Discuz'
					if ret['plugins']['Discuz'].has_key('version'):
						services['cmsversion'] = ret['plugins']['Discuz']['version'][0]</pre>
					<p>修改时一定要参考原生whatweb的插件的返回结果！</p>
					<h3>3. ruleFile类</h3>
					<p>ruleFile类是一个通用密码生成类，根据一些密码规则，生成对应的密码或路径。该类在lib/ruleFile_class.py中。暴力破解和路径猜解都会用到该类，这里提出来。</p>
					<p>生成规则如下（参考lib/db/passwd_gen.rule）：</p>
					<pre class="prettyprint linenums Lang-python">
# password 	# '#'号是注释符

%username%		# %username%是待替换的，可以自定义该字段，%com%是通用的，具体参考ruleFile类，有空细讲
%username%1
%username%12
%username%123
%username%1234
%username%12345
%username%123456
%username%@123</pre>
					<hr>
					<h2 id="questions">问题</h2>
					<h4>1. Windows, Linux or Mac?</h4>
					<p>目前建议在Kali Linux 或者Mac 上运行</p>
					<h4>2. 中文版什么时候出？</h4>
					<p>这不就是么。。。</p>
					<h4>3. 自己写的插件怎么提交？</h4>
					<p>建议在github加入这个项目，如何加入，提交代码请参考，不想这么麻烦发我邮件给我整理也行</p>
					<h4>4. 如何测试自己的插件？</h4>
					<p>每个插件都是可以自己单独运行的，所以单独测试就ok，也请大家测试完成后再提交</p>	
					<hr>
					<h2 id="contact">联系</h2>
						<p>github: <a target="_blank" href="https://github.com/yangbh/Hammer">https://github.com/yangbh/Hammer</a></p>
						<p>QQ群: 397554752</p>
						<p>感谢：Yascanner、MST、MultiProxies等众多开源及半开源程序</p>
						<p>感谢：c4bbage、kenan@为Hammer编写插件</p>
					<hr>	
				</div><!--/span-->

			</div><!--/row-->

<!-- 			<script>
				var navigation = responsiveNav("#nav", {customToggle: "#toggle"});
			</script>
 -->
			<hr>

			<footer>
				<p>© Company 2014</p>
			</footer>

		</div>

		<!-- Bootstrap core JavaScript
		================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->		
		<script src="js/jquery.pin.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script src="js/ie10-viewport-bug-workaround.js"></script>


	</body>
</html>
