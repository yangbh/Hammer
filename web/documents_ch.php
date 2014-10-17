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

		<link href="css/responsive-nav.css" rel="stylesheet">
		
		<!-- JQuery -->
		<script src="js/jquery.min.js"></script>

		<!-- a<script src="js/responsive-nav.js"></script> -->
		
		<script type="text/javascript">
		$(document).ready(function(){
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
<!-- 					<img src="images/favicon.ico" class="img-circle"> -->
					<a class="navbar-brand" href="#"><strong>Hammer</strong></a>
				</div>
				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">
						<li><a href="index.php">Home</a></li>
						<?php if (already_login()) {echo '<li><a href="scans.php">Scans</a></li>';}?>
						<li><a href="plugins.php">Plugins</a></li>
						<li class="active"><a href="documents.php">Documents</a></li>
						<li><a href="about.php">About</a></li>
					</ul>
<?php
if (already_login()) {
	$username = $_SESSION['user'];
echo <<<EOF
					<ul class ="nav navbar-nav navbar-right">
						<li class="dropdown">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
								<i class="glyphicon glyphicon-user"></i> $username<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li>
									<a href="user.php"><i class="glyphicon glyphicon-cog"></i> 设置</a>
								</li>
								<li>
								</li>
								<li>
									<a href="logout.php"><i class="glyphicon glyphicon-off"></i> 退出</a>
								</li>
								</ul>
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

				<div class="col-sm-3 col-md-2" id="myScrollspy">
					<ul class="nav nav-tabs nav-stacked" id="myNav">
						<li><a href="#about">关于</a></li>
						<li><a href="#plugin">插件</a></li>
						<li><a href="#framework">框架</a></li>
						<li><a href="#questions">问题</a></li>
						<li><a href="#contact">联系</a></li>
					</ul>
				</div>

				<div class="col-xs-12 col-sm-9 col-md-10" role="main" class="main">

					<h2 id="about">关于</h2>
						<p>Hammer 不只是一款网络扫描器，更是一个扫描框架，一句话比喻，Hammer是开源的yascanner（当然，目前功能还远不如yascanner，yascanner是我的偶像），与yascanner类似，它偏向于WEB漏洞的收集与检测，不太具有攻击性，有喜欢这种类型的妹子否？</p>
						<p>开源不易，希望大家也能够开源出自己的插件。</p>
					<hr>					
					<h2 id="plugin">插件</h2>
					<p>下面是一个典型的Hammer插件，功能为扫描robots.txt文件存在与否:</p>
					<pre>
#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
from dummy import *

# info是插件信息
info = {
	'NAME':'Robots.txt Sensitive Information',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':''
}

def Audit(services):
	# services是一个全局变量，dict类型，详见下文
	if services.has_key('url'):
		url = services['url']
		if url[-1]!='/':
			url += '/'
		url = url + 'robots.txt'
		
		respone = urllib2.urlopen(url)
		redirected = respone.geturl()
		if redirected == url:
			ret = respone.read()
			if 'Disallow: ' in ret:
				security_note(url)	# 漏洞提交接口
# ----------------------------------------------------------------------------------------------------
#	插件也可以单独运行调试，如下
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
					</pre>
					<h3>1. 变量info</h3>
					<p>一个标准的info变量，如下：</p>
					<pre>
info = {
	'NAME':'Robots.txt Sensitive Information',	# 插件名称，必须唯一
	'AUTHOR':'yangbh',		# 插件作者，不能为空
	'TIME':'20140707',		# 插件编写时间，不能为空
	'WEB':'http://',		# 漏洞参考
	'Description':'',		# 漏洞描述
	'Version':'0.1'			# 插件版本号
}
					</pre>
					<h3>2. 全局变量services</h3>
					<p>services是一个全局变量，dict类型，内含信息收集阶段运行的信息.</p>
					<p>键以及其含义：</p>
					<pre>
services = {
	# 常用的
	'ip':'127.0.0.1',	#被扫描的ip地址
	'host':'www.hammer.org',	#被扫描的host域名
	'url':'http://www.hammer.org',	#被扫描的url
	'cms':'Wordpress',	# cms类型，基于whatweb扫描结果分析，详情请参考whatweb插件
	'cmsversion':'3.9.1',	# cms版本，同上 
	'ports': [22,80],	# 端口号
	'port_detail':{22:{}},	# 端口详情，具体参考portscan插件

	# 不常用
	'noSubprocess': True,	# 是否是子进程
	'issubdomain': True,	# 是否是子域名
}
					</pre>
					<p>services变量很开放，是全局变量，意味着你可以在你的插件中修改它的值，或者增加你所需要的键，但是修改的时候请慎重！插件的调用的实现方式请参考pluginLoader_class.py</p>
					
					<h3>3. 漏洞反馈接口</h3>
					<p>漏洞反馈可以通过以下四个函数实现，参数都是字符串型</p>
					<pre>
security_note(vulninfo) 	# information level
security_info(vulninfo) 	# low level 
security_warning(vulninfo) 	# mideum level
security_hole(vulninfo) 	# high level
					</pre>
					<p>请自己参考漏洞危害酌情选择对应的接口函数。</p>
					<h3>4. 插件类型</h3>
					<p>插件总共唯一以下七种类型，请将相应的插件放在对应的目录下。</p>
					<pre>
Info Collect	# 信息收集类插件，目录：plugins/Info_Collect, 注意这类的插件最先运行!
Common		# 普通类插件，目录：plugins/Common
Sensitive Info	# 敏感信息类插件，目录：plugins/Sensitive_Info
System		# 系统类插件，目录：plugins/System
Web Applications	# WEB应用类插件，目录：plugins/Web_Applications
Weak Password	# 弱口令类插件，目录：plugins/Weak_Password
Others		# 其它类型插件，目录：plugins/Others
					</pre>
					<p>请一定注意Info_Collect类插件，这类插件最先运行，将一些信息手机类的插件放在这个目录（如会改动services全局变量的插件），其它的插件的运行顺序未知，这点会在以后优化。</p>
					<hr>
					<h2 id="framework">框架</h2>
					<h3>1. 插件调用的实现</h3>
					<p>插件调用类在lib/pluginLoader_class.py，实现步骤为：</p>
					<p>1).导入插件的Audit函数</p>
					<p>2).运行Audit函数</p>
					<p>3).保存Audit返回结果，包括</p>
					<p></p>
					<pre>
importcmd = 'global services' + os.linesep
importcmd += 'from ' + modulepath + ' import Audit,info'

exec(importcmd)

if locals().has_key('Audit'):
	ret, output = ({},'')
	try:
		ret,output = Audit(services)
	except:
		pass
	# outputinfo
	if output != '' and output != None:
		self.output += output
	# services info
	if self.services != services:
		self.services = services
		#print 'services changed:\t', services
		self.output += 'services changed to:\t' + str(services) + os.linesep
	# return info
	if ret and ret != {}:
		ret['type'] = info['NAME']
		print 'ret=\t',ret
		self.retinfo.append(ret)
					</pre>
					<p>其中的output是plugin中的输出结果，仅作显示；ret是反馈结果，现在已经弃用，可以忽略；services前文提到过，修改的原理就再此，修改时请慎重！</p>
					<h3>2. whatweb识别cms</h3>
					<p>本工具中的cms识别采用的是whatweb，有一个whatweb类，在lib/whatWeb_class.py。</p>
					<p>考虑到原生的whatweb的插件众多，影响扫描效率，所以在lib/whatweb目录下是一个经过插件简化的whatweb。PS：注意kali下whatweb会自动包含/usr/local/share/whatweb目录下的插件，所以也注释了下whatweb的几行代码，有空再找出来细说。</p>
					<p>Hammer的whatweb插件位于Info_Collect目录下，仍需补充完善，结构如下：</p>
					<pre>
def Audit(services):
	retinfo = {}
	output = ''
	if services.has_key('url'):
		output += 'plugin run' + os.linesep
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
					output += 'cms: WordPress' + os.linesep
					if ret['plugins']['WordPress'].has_key('version'):
						services['cmsversion'] = ret['plugins']['WordPress']['version'][0]
						output += 'cmsversion: ' + services['cmsversion'] + os.linesep

				# Discuz
				elif ret['plugins'].has_key('Discuz'):
					#print services
					services['cms'] = 'Discuz'
					output += 'cms: Discuz' + os.linesep
					if ret['plugins']['Discuz'].has_key('version'):
						services['cmsversion'] = ret['plugins']['Discuz']['version'][0]
						output += 'cmsversion: ' + services['cmsversion'] + os.linesep					
					</pre>
					<p>修改时一定要参考原生whatweb的插件的返回结果！</p>
					<h3>3. ruleFile类</h3>
					<p>ruleFile类是一个通用密码生成类，根据一些密码规则，生成对应的密码或路径。该类在lib/ruleFile_class.py中。暴力破解和路径猜解都会用到该类，这里提出来。</p>
					<p>生成规则如下（参考lib/db/passwd_gen.rule）：</p>
					<pre>
# password 	# '#'号是注视符

%username%		# %username%是待替换的，可以自定义该字段，%com%是通用的，具体参考ruleFile类，有空细讲
%username%1
%username%12
%username%123
%username%1234
%username%12345
%username%123456
%username%@123
					</pre>
					<hr>
					<h2 id="questions">问题</h2>
					<h4>1. Windows, Linux or Mac?</h4>
					<p>For now, suggest run hammer on linux.</p>
					<h4>2. 中文版什么时候出？</h4>
					<p>这不就是么。。。</p>
					<h4>3. 自己写的插件怎么提交？</h4>
					<p>建议在github加入这个项目，如何加入，提交代码请参考，不想这么麻烦发我邮件给我整理也行</p>
					<h4>4. 如何测试自己的插件？</h4>
					<p>每个插件都是可以自己单独运行的，所以单独测试就ok，也请大家测试完成后再提交</p>	
					<hr>	
					<h2 id="contact">联系</h2>
						<p>若有问题，github或者QQ:2452355068联系我都行</p>
						<p></p>
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
		<script src="js/bootstrap.min.js"></script>
		
		<script src="js/jquery.pin.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script src="js/ie10-viewport-bug-workaround.js"></script>


	</body>
</html>
