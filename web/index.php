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
		.navbar {
			margin-bottom: 0px;
		}
		.banner {
			position: relative;
			width: 100%;
			overflow: auto;

			font-size: 18px;
			line-height: 24px;
			text-align: center;

			color: rgba(255,255,255,.6);
			text-shadow: 0 0 1px rgba(0,0,0,.05), 0 1px 2px rgba(0,0,0,.3);

			background: #5b4d3d;
			box-shadow: 0 1px 2px rgba(0,0,0,.25);

		}
			.banner ul {
				list-style: none;
				width: 300%;
				padding-left: 0px;
			}
			.banner ul li {
				display: block;
				float: left;
				width: 33%;
				min-height: 350px;

				-o-background-size: 100% 100%;
				-ms-background-size: 100% 100%;
				-moz-background-size: 100% 100%;
				-webkit-background-size: 100% 100%;
				background-size: 100% 100%;

				box-shadow: inset 0 -3px 6px rgba(0,0,0,.1);
			}

			.banner .inner {
				padding: 80px 0 60px;
			}

			.banner h1, .banner h2 {
				font-size: 30px;
				line-height: 35px;

				color: #fff;
			}

			.banner .btn {
				display: inline-block;
				margin: 25px 0 0;
				padding: 9px 22px 7px;
				clear: both;

				color: #fff;
				font-size: 12px;
				font-weight: bold;
				text-transform: uppercase;
				text-decoration: none;

				border: 2px solid rgba(255,255,255,.4);
				border-radius: 5px;
			}
				.banner .btn:hover {
					background: rgba(255,255,255,.05);
				}
				.banner .btn:active {
					-webkit-filter: drop-shadow(0 -1px 2px rgba(0,0,0,.5));
					-moz-filter: drop-shadow(0 -1px 2px rgba(0,0,0,.5));
					-ms-filter: drop-shadow(0 -1px 2px rgba(0,0,0,.5));
					-o-filter: drop-shadow(0 -1px 2px rgba(0,0,0,.5));
					filter: drop-shadow(0 -1px 2px rgba(0,0,0,.5));
				}

			.banner .btn, .banner .dot {
				-webkit-filter: drop-shadow(0 1px 2px rgba(0,0,0,.3));
				-moz-filter: drop-shadow(0 1px 2px rgba(0,0,0,.3));
				-ms-filter: drop-shadow(0 1px 2px rgba(0,0,0,.3));
				-o-filter: drop-shadow(0 1px 2px rgba(0,0,0,.3));
				filter: drop-shadow(0 1px 2px rgba(0,0,0,.3));
			}

			.banner .dots {
				position: absolute;
				left: 0;
				right: 0;
				bottom: 20px;
				padding-left: 0px;
			}
				.banner .dots li {
					display: inline-block;
					width: 10px;
					height: 10px;
					margin: 0 4px;

					text-indent: -999em;

					border: 2px solid #fff;
					border-radius: 6px;

					cursor: pointer;
					opacity: .4;

					-webkit-transition: background .5s, opacity .5s;
					-moz-transition: background .5s, opacity .5s;
					transition: background .5s, opacity .5s;
				}
					.banner .dots li.active {
						background: #fff;
						opacity: 1;
					}

			.banner .arrows {
				position: absolute;
				bottom: 20px;
				right: 20px;
				color: #fff;
			}
				.banner .arrow {
					display: inline;
					padding-left: 10px;
					cursor: pointer;
				}
		</style>

		
		<script src="js/jquery.min.js"></script>
		<!-- <script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script> -->
		
		<script src="js/unslider.min.js"></script>

		<script type="text/javascript">
			$(document).ready(function(){
				$(function() {
					// $('.banner').unslider();
					if(window.chrome) {
						$('.banner li').css('background-size', '100% 100%');
					}
					$('.banner').unslider({
						speed: 500,               //  The speed to animate each slide (in milliseconds)
						delay: 3000,              //  The delay between slide animations (in milliseconds)
						complete: function() {},  //  A function that gets called after every slide animation
						keys: true,               //  Enable keyboard (left, right) arrow shortcuts
						dots: true,               //  Display dot navigation
						fluid: false              //  Support responsive design. May break non-responsive designs
					});
				})
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
<!-- 		<div class="jumbotron">
			<div class="container">
				<h1>What's Hammer?</h1>
				<p>Hammer is a web vulnnerability scanner, but more of a vulnerability scan framework. It supports plug-in extensions, you can design your own hammer, that is your hacking tool. Hammer is open source, and i hope you can share yours! </p>
				<p><a class="btn btn-primary btn-lg" role="button" href="https://www.github.com/yangbh/Hammer">Design Your Hammer &raquo;</a></p>
			</div>
		</div> -->

		<div class="banner">
			<ul>
				<li style="background-image: url('images/sunset.jpg');">
					<div class="inner">
						<h1>Hammer -- a web vulnnerability scanner.</h1>
						<p>Hammer漏洞扫描框架，你值得拥有。</p>
						<a class="btn" href="https://github.com/yangbh/Hammer">下载</a>
					</div>
				</li>

				<li style="background-image: url('images/wood.jpg');">
					<div class="inner">
						<h1>Hammer -- a web vulnnerability scanner.</h1>
						<p>Hammer漏洞扫描框架，你值得拥有。</p>
						<a class="btn" href="https://github.com/yangbh/Hammer">下载</a>
					</div>
				</li>

				<li style="background-image: url('images/subway.jpg');">
					<div class="inner">
						<h1>Hammer -- a web vulnnerability scanner.</h1>
						<p>Hammer漏洞扫描框架，你值得拥有。</p>
						<a class="btn" href="https://github.com/yangbh/Hammer">下载</a>
					</div>
				</li>

				<li style="background-image: url('images/shop.jpg');">
					<div class="inner">
						<h1>Hammer -- a web vulnnerability scanner.</h1>
						<p>Hammer漏洞扫描框架，你值得拥有。</p>
						<a class="btn" href="https://github.com/yangbh/Hammer">下载</a>
					</div>
				</li>
			</ul>
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
