<?php
require_once('common.php');
?>
<?php
// check session first
if(already_login()){
	// print 'already login';
	header('Location: index.php');
	exit;
}
// print 'hehe';
$user = check_sql(trim($_POST['username']));
$pwd = check_sql(trim($_POST['password']));
// var_dump($_POST);
// print('$user='.$user.'<br>');
// print('$pwd='.$pwd.'<br>');

if (login_check($user,$pwd)) {
	// print 'login success';
	header('Location: index.php');
	exit;
}

?>
<!DOCTYPE html>
<html lang="zh-cn">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Login</title>

		<!-- Bootstrap -->
		<link href="css/bootstrap.min.css" rel="stylesheet">

		<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
		<!--[if lt IE 9]>
			<script src="http://cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
			<script src="http://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
		<![endif]-->
		<style type="text/css">
			/* Override some defaults */
			html, body {
				background-color: #eee;
			}
			body {
				padding-top: 150px; 
			}
			.container {
				width: 300px;
			}

			/* The white background content wrapper */
			.container > .content {
				background-color: #fff;
				padding: 20px;
				margin: 0 -20px; 
				-webkit-border-radius: 10px 10px 10px 10px;
					 -moz-border-radius: 10px 10px 10px 10px;
								border-radius: 10px 10px 10px 10px;
				-webkit-box-shadow: 0 1px 2px rgba(0,0,0,.15);
					 -moz-box-shadow: 0 1px 2px rgba(0,0,0,.15);
								box-shadow: 0 1px 2px rgba(0,0,0,.15);
			}

			.login-form {
				margin-left: 20px;
				margin-right: 20px;
			}

			#login-from-header{

			}

		</style>
	</head>
	<body>
		<div class="container">
			<div class="content">
				<div class="row">
					<div class="login-form">
						<div id="login-from-header">
							<div style="float:left;">
								<h2>Login</h2>
							</div>
							<div style="float:right;">
								<a href="about.html" tabindex="-1">
								<span class="glyphicon glyphicon-question-sign"></span></a>
							</div>
						</div>
						<div>
							<form id="login-form" action="login.php" method="post">
								<div class="form-group">
									<!-- <label for="username">Username</label> -->
									<input type="text" class="form-control" name="username" placeholder="Username">
									<div style="float:right;">
										<a href="signin.php" tabindex="-1">Sign?</a>
									</div>
									
								</div>
								<div class="form-group">
									<!-- <label for="password">Password</label> -->
									<input type="password" class="form-control" name="password" placeholder="Password">
									<div style="float:right;">
										<a href="findpwd.php" tabindex="-1">Forget password?</a>
									</div>
								</div>
								<div>
									<div style="float:left;">
										<button type="submit" class="btn btn-default">Submit</button>
									</div>
									<!-- <div style="float:right;">
										<a href="about.html">About Hammer</p>
									</div> -->
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div> <!-- /container -->
		<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
		<script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script>
		<!-- Include all compiled plugins (below), or include individual files as needed -->
		<script src="js/bootstrap.min.js"></script>
	</body>
</html>
