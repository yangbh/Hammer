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
<!--          <img src="images/favicon.ico" class="img-circle"> -->
					<a class="navbar-brand" href="#"><strong>Hammer</strong></a>
				</div>
				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">
						<li><a href="index.php">Home</a></li>
						<?php if (already_login()) {echo '<li><a href="scans.php">Scans</a></li>';}?>
						<li><a href="plugins.php">Plugins</a></li>
						<li><a href="documents.php">Documents</a></li>
						<li class="active"><a href="about.php">About</a></li>
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
									<a href="user_setting"><i class="glyphicon glyphicon-cog"></i> 设置</a>
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

				<div class="col-xs-2 col-sm-2 col-md-2" id="myScrollspy">
					<ul class="nav nav-tabs nav-stacked" id="myNav">
						<li><a href="#1.2">1.2</a></li>
						<li><a href="#1.1">1.1</a></li>
						<li><a href="#1.0">1.0</a></li>
					</ul>
				</div>

				<div class="col-xs-10 col-sm-10 col-md-10" role="main" class="main">
					<h2 id="1.2">1.2</h2>
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
					<h3>1.1.0.140918_lpha</h3>
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
