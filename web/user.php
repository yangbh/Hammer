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
			a span{
				color: #555;
				text-decoration: none;
			}
		</style>

		
		<script src="js/jquery.min.js"></script>
		<!-- <script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script> -->

		<script type="text/javascript">
			// $("#username").change(function(){
			// 	alert($("#username").value);
			// });
			function changepassword(){
				var oldpwd = $('#oldpassword').val();
				var newpwd = $('#newpassword').val();
				var newpwd2 = $('#newpassword2').val();
				if (newpwd == newpwd2) {
					$.post("user_setting.php", {type: "changepwd",oldpwd: oldpwd,newpwd: newpwd},
						function(data){
							if (data.code) {
								alert('change password success');
							}
							else{
								alert(data.info);
							}
						},"json");
				}
				else{
					alert('new passwords not the same');
				}
			}
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
							<li ><a href="#overview">Overview</a></li>
							<li><a href="#token">Token</a></li>
							<li><a href="#changepwd">Change password</a></li>
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
								<code>python hammer.py -s <?php echo $_SERVER['HTTP_HOST'].str_replace('/user.php','',$_SERVER['PHP_SELF']);?> -t <?php $a=get_userinfo();echo $a['Token'];?> -T http://testphp.vulnweb.com</code>
							</div>
						</div>
						<div class="panel panel-default" id="token">
							<div class="panel-heading">
								Change password
							</div>
							<div class="panel-body">
								<div class="form-inline">
									<div class="form-inline">
										<div class="form-inline">
											&nbsp;Old Password: &nbsp;&nbsp;&nbsp;
											<input class="form-control" id="oldpassword" placeholder="Old Password" type="password" />
										</div>
									</div>
									<div class="form-inline">
										<div class="form-inline">
											New Password: &nbsp;&nbsp;
											<input class="form-control" id="newpassword" placeholder="New Password" type="password" />
										</div>
									</div>
									<div class="form-inline">
										<div class="form-inline">
											New Password: &nbsp;&nbsp;
											<input class="form-control" id="newpassword2" placeholder="New Password" type="password" />
										</div>
									</div>
									<div class="form-inline">
										<div class="form-inline">
											<div class="controls">
												<button type="submit" class="btn" onclick="changepassword()">更改</button>
											</div>
										</div>
									 </div>
								</div>

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
