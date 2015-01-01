<?php
require_once('common.php');

//  check login first
if (!already_login()) {
	error_jump();
}
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
		<div class="container">

			<div class="container-fluid">
				<div class="row">
					<div class="col-sm-3 col-md-3">
					<h1>
						<a href='index.php'><span class="glyphicon glyphicon-circle-arrow-left"></span></a>&nbsp;User Info
					</h1>
					</div>
				</div>
				<div class="row">
					<div class="col-sm-3 col-md-2 sidebar">
						<ul class="nav nav-sidebar">
							<li ><a href="#">Overview</a></li>
							<li><a href="#token">Token</a></li>
							<li><a href="#">Settings</a></li>
							<li><a href="#">About</a></li>
						</ul>
					</div>
					<div class="col-sm-9 col-md-10  main">
						<div class="panel panel-default">
							<div class="panel-heading">
								User
							</div>
							<div class="panel-body">
								<b><?php $a=get_userinfo();echo $a['Name'];?></b>
							</div>
						</div>
						<div class="panel panel-default" id="token">
							<div class="panel-heading">
								<a href="user_token_refresh.php"><span class="glyphicon glyphicon-refresh"></span></a>
								Token: <?php $a=get_userinfo();echo $a['Token'];?>
							</div>
							<div class="panel-body">
								<p>Run Hammer like this:</p>
								<code>python hammer.py -s www.hammer.org -t <?php $a=get_userinfo();echo $a['Token'];?> -T http://testphp.vulnweb.com</code>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		
		<!-- Bootstrap core JavaScript
		================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<script src="js/bootstrap.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script src="js/ie10-viewport-bug-workaround.js"></script>
	</body>
</html>
