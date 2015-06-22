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
				color: #030303;
				text-decoration: none;
			}
		</style>
		<!-- jquery -->
		<!-- <script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
		<script src="js/jquery.min.js"></script>

		<script>
		// 对Date的扩展，将 Date 转化为指定格式的String
		// 月(M)、日(d)、小时(h)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符， 
		// 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字) 
		// 例子： 
		// (new Date()).Format("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423 
		// (new Date()).Format("yyyy-M-d h:m:s.S")      ==> 2006-7-2 8:9:4.18 
		Date.prototype.Format = function (fmt) { //author: meizz 
			var o = {
				"M+": this.getMonth() + 1, //月份 
				"d+": this.getDate(), //日 
				"h+": this.getHours(), //小时 
				"m+": this.getMinutes(), //分 
				"s+": this.getSeconds(), //秒 
				"q+": Math.floor((this.getMonth() + 3) / 3), //季度 
				"S": this.getMilliseconds() //毫秒 
			};
			if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
			for (var k in o)
			if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
			return fmt;
		}

		$(document).ready(function () {
			//  plugin table
			$('#config_table').DataTable({
				// "ajax": "./datatable.json",
				"ajax": "./configs_search.php",
				// "paging":   false,
				"lengthChange": false, //改变每页显示数据数量
				"pageLength": 15,
				// "info":     false,
				"filter":   false,
				// "ordering": false,
				"order":    [6, "desc" ],
				"columnDefs": [
					{
						"targets": [0,3],
						"visible": false,
						"searchable": false
					},
					{
						"targets": [1],
						"render": function ( data, type, full, meta ) {
							return "<a class=\"plugin\" href=\""+"configs_edit.php#"+full[1]+"\">"+data+"</a>";
						}
					},
					{
						"targets":[6],
						 "render": function ( data, type, full, meta ) {
							return data == 1?'默认':'';
						}
					},
				 ]
			});

			//  search button click
			$('#search').click(function() {
				/* Act on the event */
				var ajax_url = "./configs_search.php?name="+$('#name').val();
				$('#config_table').DataTable().ajax.url(ajax_url).load();
			});

		});
		</script>
	</head>

	<body>
		<div class="navbar navbar-inverse navbar-default" role="navigation" style="border-radius: 0px;margin: 0px;">
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
						<?php if (already_login()) {echo '<li class="active"><a href="configs.php">Configs</a></li>';}?>
						<li><a href="documents.php">Documents</a></li>
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
			<div class="row" id="plugins">
				<div class="container" >
						<h2 class="page-header">
							<!-- <span class="glyphicon glyphicon-th"></span> -->
							Config&nbsp;
							<a href="task_create.php"><span class="glyphicon glyphicon-plus"></span></a>
							<a href="#"><span class="glyphicon glyphicon-search"></span></a>
						</h2>
						<div class="form-inline">
							<div class="form-group">
								<input type="text" class="form-control" id="keyword" placeholder="Keyword" name="keyword">
							</div>
							<button id="search" class="btn btn-default">Search</button>
						</div>
					<div class="table-responsive">
						<table id="config_table" class="table table-striped">
							<thead>
								<tr>
									<th>ID</th>
									<th style="width: 10%">Name</th>
									<th style="width: 15%">Time</th>
									<th style="width: 60%">Config</th>
									<th style="width: 5%">Auto Increament</th>
									<th style="width: 10%">Description</th>
									<th style="width: 10%">Is Default</th>
								</tr>
							</thead>
						</table>
					</div>
				</div>
			</div>
			<div class="row" id="code" hidden="true">
			<div class="container" >
				<h1>
					<a class="glyphicon glyphicon-circle-arrow-left" id="plugin_goback"></a>&nbsp;
					<small>Scan Results</small>
				</h1>
				<!-- <pre class="python" id="plugin_code"></pre> -->
				<div class="panel" id="scan_title">
				</div>
				<div class="panel" id="scan_results">
				</div>
			</div>
			</div>
			<hr>
			<footer>
				<p>© Company 2014</p>
			</footer>
		</div>

		<!-- ================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<!-- Bootstrap core JavaScript -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->

		<!-- DataTables -->
		<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
		<script type="text/javascript" charset="utf8" src="js/jquery.dataTables.js"></script>

		<!-- datatimepicker -->
		<link rel="stylesheet" type="text/css" href="css/bootstrap-datetimepicker.min.css">
		<script type="text/javascript" charset="utf8" src="js/bootstrap-datetimepicker.min.js"></script>

		<!-- snippet -->
		<link rel="stylesheet" type="text/css" href="css/jquery.snippet.min.css">
		<script type="text/javascript" charset="utf8" src="js/jquery.snippet.min.js"></script>

	</body>
</html>
