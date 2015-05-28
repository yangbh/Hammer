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
			/*.navbar-inverse .navbar-nav>li>a{
				font-size: 15px;
				color: #ffffff;
			}
			.navbar-inverse .navbar-nav > .active > a, .navbar-inverse .navbar-nav > .active > a:hover, .navbar-inverse .navbar-nav > .active > a:focus{
				background-color: #D6572A;
			}*/
			a span{
				color: #030303;
				text-decoration: none;
			}
		</style>
		<!-- jquery -->
		<!-- <script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
		<script src="js/jquery.min.js"></script>

		<script>
		$(document).ready(function () {
			//  hide plugin_code div
			$('#code').hide('fast');
			//  snippet
			$("pre#python").snippet("python",{style:"vim",menu:false,showNum:true});

			//  plugin table
			$('#plugins_table').DataTable({
				// "ajax": "./datatable.json",
				"ajax": "./plugins_search.php",
				// "paging":   false,
				"lengthChange": false, //改变每页显示数据数量
				"pageLength": 15,
				// "info":     false,
				"filter":   false,
				// "ordering": false,
				"order":    [[ 3, "desc" ]],
				"columnDefs": [ 
					{
						"targets": 0,
						"visible": false,
						"searchable": false
					},{
					"targets": 1,
					"render": function ( data, type, full, meta ) {
						// return "<a class=\"plugin\" href='search.php?name="+encodeURI(data)+"'>"+data+"</a>";
						// $(this:parent).parent.text();
						// console.log(full);
						return "<a class=\"plugin\" href=\"code.php#"+full[0]+"\">"+data+"</a>";
					}
				} ]
			});

			//  <a> links in tables
			// $('#plugins_table').DataTable().on('draw.dt', function () {
			// 	$('.plugin').bind("click",function() {
			// 		var name= $(this).text();
			// 		$.get("plugins_search.php",{name: name},function(data){
			// 			$('#plugins').hide('slow');
			// 			$('#code').show('slow');
			// 			$('#plugin_name').html(name);
			// 			$('#plugin_code').html(data);
			// 		});
			// 	});
			// });

			// $('#plugin_goback').click(function(){
			// 	$('#plugins').show('slow');
			// 	$('#code').hide('slow');
			// });

			//  search button click
			$('#search').click(function() {
				/* Act on the event */
				var ajax_url = "./plugins_search.php?type="+$('#type').val()+"&keyword="+$('#keyword').val();
				$('#plugins_table').DataTable().ajax.url(ajax_url).load();
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
						<li class="active"><a href="plugins.php">Plugins</a></li>
						<?php if (already_login()) {echo '<li><a href="configs.php">Configs</a></li>';}?>
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
						Plugins&nbsp;
						<!-- <a href="#"><span class="glyphicon glyphicon-plus"></span></a> -->
						<!-- <a href="#"><span class="glyphicon glyphicon-search"></span></a> -->
						<a href="plugins_config.php"><span class="glyphicon glyphicon-cog"></span></a>
					</h2>
					<div class="form-inline">
						<div class="btn-group">
							<select class="form-control" name="type" id="type">
								<option value="0">All Category</option>
								<option value="4">Info Collect</option>
								<option value="1">Common</option>
								<option value="2">Sensitive Info</option>
								<option value="3">System</option>
								<option value="5">Web Applications</option>
								<option value="6">Weak Password</option>
								<option value="7">Others</option>
							</select>
						</div>
						<div class="form-group">
							<input type="text" class="form-control" id="keyword" placeholder="Keyword" name="keyword">
						</div>
						<button id="search" class="btn btn-default">Search</button>
					</div>
					<div class="table-responsive">
						<table id="plugins_table" class="table table-striped">
							<thead>
								<tr>
									<th>ID</th>
									<th style="width: 30%">Name</th>
									<th style="width: 10%">Author</th>
									<th style="width: 10%">Time</th>
									<th style="width: 50%;overflow:hidden;">Description</th>
								</tr>
							</thead>
						</table>
					</div>
				</div>
			</div>
			<!-- <div class="row" id="code" hidden="true">
			<div class="container" >
				<h1><a class="glyphicon glyphicon-circle-arrow-left" id="plugin_goback"></a>&nbsp;<small id="plugin_name"></small></h1>
				<pre class="python" id="plugin_code"></pre>
			</div>
			</div> -->
			<hr>
			<footer>
				<p>© Company 2014</p>
			</footer>
		</div>

		<!-- ================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<!-- snippet -->
		<link rel="stylesheet" type="text/css" href="css/jquery.snippet.min.css">
		<script type="text/javascript" charset="utf8" src="js/jquery.snippet.min.js"></script>

		<!-- Bootstrap core JavaScript -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->


		<!-- DataTables -->
		<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
		<script type="text/javascript" charset="utf8" src="js/jquery.dataTables.js"></script>

	</body>
</html>
