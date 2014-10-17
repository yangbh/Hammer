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

		<style type="text/css">

		</style>

		
		<script src="js/jquery.min.js"></script>
		<!-- <script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script> -->

		<script type="text/javascript">
			// $("#username").change(function(){
			// 	alert($("#username").value);
			// });
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
<!-- 				<img src="images/favicon.ico" class="img-circle"> -->
					<a class="navbar-brand" href="#"><strong>Hammer</strong></a>
				</div>
				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">
						<li class="active"><a href="index.php">Home</a></li>
						<?php if (already_login()) {echo '<li><a href="scans.php">Scans</a></li>';}?>
						<li><a href="plugins.php">Plugins</a></li>
						<li><a href="documents.php">Documents</a></li>
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
							<ul class="dropdown-menu" role="meun">
								<li role="presentation">
									<a href="user.php"><i class="glyphicon glyphicon-cog"></i> 设置</a>
								</li>
								<li role="presentation">
								</li>
								<li role="presentation">
									<a href="logout.php"><i class="glyphicon glyphicon-off"></i> 退出</a>
								</li>
							</ul>
						</li>
					</ul>
EOF;
}
else{
echo <<<EOF
					<div class="navbar-form navbar-right">
						<button class="btn btn-success" data-toggle="modal" data-target="#myModal">
							Sign in
						</button>
					</div>
EOF;
}
?>
				</div><!--/.navbar-collapse -->
			</div>
		</div>


		<!-- Main jumbotron for a primary marketing message or call to action -->
		<div class="jumbotron">
			<div class="container">
				<h1>What's Hammer?</h1>
				<p>Hammer is a web vulnnerability scanner, but more of a vulnerability scan framework. It supports plug-in extensions, you can design your own hammer, that is your hacking tool. Hammer is open source, and i hope you can share yours! </p>
				<p><a class="btn btn-primary btn-lg" role="button" href="https://www.github.com/yangbh/Hammer">Design Your Hammer &raquo;</a></p>
			</div>
		</div>

		<div class="container">
			<!-- Example row of columns -->
			<div class="row">
				<div class="col-md-4">
					<h2>Framework</h2>
					<p>Hammer is coded in Python, so it can cross platform, you can use hammer in windows, linux and mac... </p>
					<p><a class="btn btn-default" href="plugins.php" role="button">View details &raquo;</a></p>
				</div>
				<div class="col-md-4">
					<h2>API Docs</h2>
					<p>In hammer, almost everything is plugin. If you want design you own plugins, you must know how to. API documents just tells you that. </p>
					<p><a class="btn btn-default" href="documents.php" role="button">View details &raquo;</a></p>
			 </div>
				<div class="col-md-4">
					<h2>About</h2>
					<p>Hammer is coded by yangbh, that's me of course. I design Hammer because i want a hacking tool of my own, like yascanner, mst, blackspider, multiproxies... I share Hammer because i hope everyone in hacking group can share their own good ideas and tools... </p>
					<p><a class="btn btn-default" href="about.php" role="button">View details &raquo;</a></p>
				</div>
			</div>

			<hr>

			<footer>
				<p>&copy; Company 2014</p>
			</footer>
		</div> <!-- /container -->

<?php
if (!already_login()) {
echo <<<EOF
		<!-- 模态框（Modal） -->
		<div class="modal fade" id="myModal" tabindex="-1" role="dialog" 
		   aria-labelledby="myModalLabel" aria-hidden="true">
		   <div class="modal-dialog" style="width:400px">
			  <div class="modal-content">
				 <div class="modal-header">
					<button type="button" class="close" 
					   data-dismiss="modal" aria-hidden="true">
						  &times;
					</button>
					<h4 class="modal-title" id="myModalLabel">
					   Sign In
					</h4>
				 </div>
				 <div class="modal-body">
					<form role="form" action="login.php" method="post">
						<div class="form-group">
							<input type="text" placeholder="Name" class="form-control" name="username" id="username">
						</div>
						<div class="form-group">
							<input type="password" placeholder="Password" class="form-control" name="password" id="password">
						</div>
						<button type="submit" class="btn btn-success">Sign in</button>
					</form>
				 </div>
			  </div><!-- /.modal-content -->
		</div><!-- /.modal -->
EOF;
}
?>

		<!-- Bootstrap core JavaScript
		================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<script src="js/bootstrap.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script src="js/ie10-viewport-bug-workaround.js"></script>
	</body>
</html>
