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
						<li><a href="documents.php">Documents</a></li>
						<li class="active"><a href="about.php">About</a></li>
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
					<ul class="nav nav-tabs nav-stacked" id="myNav" style="width: 50px;border:0 px;">
						<li><a href="#">1.4</a></li>
						<li><a href="#1.2">1.3</a></li>
						<li><a href="#1.2">1.2</a></li>
						<li><a href="#1.1">1.1</a></li>
						<li><a href="#1.0">1.0</a></li>
					</ul>
				</div>

				<div class="col-xs-10 col-sm-10 col-md-10" role="main" class="main">
					<h2 id="1.4">1.4</h2>
					<h3>1.4.5.150530_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).全面引入全局config变量，规范config接口</p>
						<p>b).web config管理以及更细粒度的创建任务、插件参数配置</p>
						<p>c).插件接口变量opts更改,以适应通过web可配置</p>
					<h3>1.4.4.150502_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).修复-l监听模式subTarget子进程共享变量紊乱</p>
						<p>b).初步引入全局config与插件config配置措施，方便用户配置</p>
					<h3>1.4.3.150421_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).增加插件超时机制</p>
						<p><strong>待完善：</strong></p>
						<p>a).代理接口自动化管理，参考multiproxies</p>
						<p>b).增加搜索引擎支持，类似multisearch</p>
						<p>c).搜索引擎自动代理攻击模块，类似golismero</p>
						<p>d).引入全局config与插件config</p>
						<p>e).重构pluginloader，一次加载所有插件，避免多次文件读取加载，类似msf</p>
						<p>f).设置http类型的target黑名单，比如默认建站可能一站多地址，对此进行target过滤</p>
					<h3>1.4.2.150322_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).-l监听模式修改成多线程模式修复</p>
						<p>b).autoproxy自动代理雏形</p>
					<hr>
					<h3>1.4.1.150122_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).参考mst，增加命令行模式</p>
					<hr>
					<h3>1.4.0.150118_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).初步尝试web管理模式</p>
						<p>b).优化安装，采用requirement.txt管理python依赖库</p>
						<p><strong>待完善：</strong></p>
						<p>a).更加细致web管理的参数，可指定插件参数</p>
						<p>b).更加细致的任务分配（现在以每个scan为单位，以后可以考虑以target或者plugin为单位）</p>
						<p>c).console控制，类似mst</p>
						<p>d).增加配置管理，例如全局参数与每个插件参数的统一管理</p>
					<hr>
					<h2 id="1.3">1.3</h2>
					<h3>1.3.2.141216_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).引入单个插件的批量模式，-p pluginpath</p>
						<p>b).引入logger接口，完善输出日志</p>
						<p>c).弃用本地结果保存与输出功能</p>
						<p>d).一些bug修复</p>
					<hr>
					<h3>1.3.1.141204_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).一些bug修复</p>
						<p>b).引入yascanner的assign接口</p>
						<p><strong>待完善：</strong></p>
						<p>a).采用log进行调试输出</p>
						<p>b).插件不应该每一个子进程（即pluginLoader_class.py）中加载，而应该在scanner_class.py中一次加载完成，避免加载多次</p>
						<p>c).futures模块主进程ctrl＋c捕获不到，必须要等所有子进程停止才能捕获</p>
					<hr>
					<h3>1.3.0.141109_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).对框架的调整，明确分为信息收集模块和漏洞扫描模块，信息收集模块支持动态添加</p>
						<p>b).添加ip段扫描</p>
						<p>c).一些关键插件性能优化</p>
					<hr>
					<h2 id="1.2">1.2</h2>
					<h3>1.2.2.141101_Beta</h3>
						<p><strong>改进：</strong></p>
						<p>a).弃用session，改用token</p>
						<p>b).ctrl+c子进程退出</p>
						<p>c).一些其他bug修复以及插件添加</p>
						<p><strong>待完善：</strong></p>
						<p>a).插件分配机制(终于体会yascanner的assign接口函数的用处了)</p>
						<p>b).分布式</p>
						<p>c).跨平台</p>
					<hr>
					<h3>1.2.1.141011_Beta</h3>
						<p><strong>修改：</strong></p>
						<p>a).统一漏洞提交接口，改用security_info等类似函数，与return retinfo返回结果并用</p>
					<hr>
					<h3>1.2.0.140928_Beta</h3>
						<p>第一个发布的测试版本</p>
						<p><strong>修复漏洞：</strong></p>
						<p>a).改用multiprocessing模块，修复了threading方式时多个子任务访问Plugin全局变量造成全局变量紊乱</p>
						<p>b).完善web功能</p>
						<p><strong>待完善：</strong></p>
						<p>a).改用multiprocessing模块之后，scanner_calsss_mp.py中调用crawler插件在Mac OS平台上会出现Python异常，Linux正常，原因未知，猜测为sqlite3.so在Mac上fork进程异常</p>
						<p>b).修改后台用户验证机制，不直接采用session，并启用一个专门的ttl进程</p>
						<p>c).程序退出时停止所有扫描子进程</p>
						<p>d).统一漏洞提交接口，改用securityInfo等类似函数，弃用return retinfo</p>
						<!-- <p>c).</p> -->
					<hr>  
					<h2 id="1.1">1.1</h2>
					<h3>1.1.0.140918_Alpha</h3>
						<p>
							第一个发布的功能版本
						</p>
					<hr> 
					<h2 id="1.0">1.0</h2>
					<h3>1.0.0</h3>
						<p>
							Just For Test!
						</p>
					<hr>
	 
				</div><!--/span-->

			</div><!--/row-->

<!--      <script>
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
