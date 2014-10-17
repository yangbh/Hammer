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
						<li><a href="#about">About</a></li>
						<li><a href="#plugin">Plugin Interfaces</a></li>
						<li><a href="#framework">Framework</a></li>
						<li><a href="#questions">Questions</a></li>
						<li><a href="#contact">ContactMe</a></li>
					</ul>
				</div>

				<div class="col-xs-12 col-sm-9 col-md-10" role="main" class="main">

					<h2 id="about">About</h2>
						<p>Hammer is a web vulnnerability scanner, but more of a vulnerability scan framework. It supports plug-in extensions, you can design your own hammer, that is your hacking tool. Hammer is open source, and i hope you can share yours!</p>
					<hr>					
					<h2 id="plugin">Plugin Interfaces</h2>
					<p>The following is a typical plugin with detailed comments, To detect the sensitive information in robots.txt:</p>
					<pre>
#!/usr/bin/python2.7
#coding:utf-8

import os
import urllib2
from dummy import *

info = {
	'NAME':'Robots.txt Sensitive Information',
	'AUTHOR':'yangbh',
	'TIME':'20140707',
	'WEB':''
}

def Audit(services):
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
				security_note(url)
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	services = {'url':'http://www.eguan.cn'}
	pprint(Audit(services))
					</pre>
					<h3>1. Plugin Information: info</h3>
					<p>A standard info:</p>
					<pre>
info = {
	'NAME':'Robots.txt Sensitive Information',	# the plugin name, must be unique
	'AUTHOR':'yangbh',		# the author, coludn't be none
	'TIME':'20140707',		# the plugin coded time, coludn't be none
	'WEB':'http://',		# any website to introduce this vulnerabilisty, maybe none
	'Description':'',		# your description about this plugin, maybe none
	'Version':'0.1'			# the plugin version, maybe none
}
					</pre>
					<h3>2. Global Variable: services</h3>
					<p>Variable services is a global dict, it contains informations that plugin need.</p>
					<p>Keys in services and its meaning:</p>
					<pre>
services = {
	# commonly used
	'ip':'127.0.0.1',
	'host':'www.hammer.org',
	'url':'http://www.hammer.org',
	'cms':'Wordpress',	# please refer whatweb plugin
	'cmsversion':'3.9.1',
	'ports': [22,80],	# a list port table, please refer portscan plugin
	'port_detail':{22:{}},	# a dict port table, contains detail port information, please refer portscan plugin

	# not commonly used
	'noSubprocess': True,
	'issubdomain': True,
}
					</pre>
					<p>At last, you can design you key in services dict whatever you want!</p>
					
					<h3>3. Result Interfaces</h3>
					<p>Function used to report vulnerability:</p>
					<pre>
security_note(vulninfo) 	# information level
security_info(vulninfo) 	# low level 
security_warning(vulninfo) 	# mideum level
security_hole(vulninfo) 	# high level
					</pre>
					<p>Choose the right one when your plugin find a vulnerability.</p>
					<h3>4. Plugin Type</h3>
					<p></p>
					<pre>
Info Collect 		# in directory plugins/Info_Collect, these plugins run first!
Common			# in directory plugins/Common
Sensitive Info		# in directory plugins/Sensitive_Info
System			# in directory plugins/System
Web Applications	# in directory plugins/Web_Applications
Weak Password		# in directory plugins/Weak_Password
Others			# in directory plugins/Others
					</pre>
					<p>Put your plugin into the right directory.</p>
					<hr>
					<h2 id="framework">Framework</h2>
					<hr>	
					<h2 id="questions">Questions</h2>
					<h4>1. Windows, Linux or Mac?</h4>
					<p>For now, suggest run hammer on linux.</p>
					<h4>2. 中文版什么时候出？</h4>
					<p>尽快，最近有点忙。。。</p>
					<h4>3. 自己写的插件怎么提交？</h4>
					<p>建议在github加入这个项目，发我邮件我整理也行～～Hammer只是一个框架，只有大家一起开发插件，Hammer才能变成一个扫描器</p>
					<h4>4. 如何测试自己的插件？</h4>
					<p>每个插件都是可以自己单独运行的，所以单独测试就ok，也请大家测试完成后再提交</p>	
					<hr>	
					<h2 id="contact">ContactMe</h2>
						<p>If you have any problem, please notice me at github.</p>
						<p>If necessary, please contact QQ:2452355068.</p>
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
