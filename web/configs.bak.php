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
		<!-- Documentation extras -->
		<link href="css/docs.min.css" rel="stylesheet">
		<!-- jquery -->
		<!-- <script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
		<script src="js/jquery.min.js"></script>

		<!-- Bootstrap core JavaScript -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript" src="js/bootstrap.min.js"></script>

		<script type="text/javascript" src="js/searchbox.js"></script>
		<style type="text/css">
		a span{
			color: #555;
			text-decoration: none;
		}
		body{
			/*font-size: 16px;*/
		}
		.mcheck {
			width: 150px;
		}
		blockquote {
			margin: 0px;
			margin-bottom: 0px;
		}
		.panel {
			margin-top: 5px;
			margin-bottom: 5px;
		}
		blockquote {
			margin:5px;
			padding: 5px;
			font-size: 15px;
		}
		</style>

	</head>

	<body>

		<!-- Main jumbotron for a primary marketing message or call to action -->
		<div class="container">
			<h1>
				<a href="index.php">
					<!-- <small><span class="glyphicon glyphicon-home"></span></small> -->
					<span class="glyphicon glyphicon-home"></span>
				</a>
				<a href="javascript:history.back()">
					<span class="glyphicon glyphicon-circle-arrow-left"></span>
				</a>
				Config
			</h1>
			<div class="form" id="dlg_form">

				<div class="panel panel-default form-group">
					<div class="panel-heading"><strong>Configs</strong></div>
					<div class="panel-body collapse in" id="modules">
						<div class="content">
							<div style="margin-top:5px">
								<p><div id="dists">
									No dispatchers created yet !<a target="_blank" href="http://www.python.org/">Depends on Python 2.7.*</a><br>
								</div></p>
								<p>Just paste following command at terminal prompt. <i>-m</i> options specifies maximum number of concurrent tasks.<br></p>
								<code>python hammer.py -s <?php echo $_SERVER['HTTP_HOST'].str_replace('/task_create.php','',$_SERVER['PHP_SELF']);?> -t <?php $a=get_userinfo();echo $a['Token'];?> -l</code>
							</div>
						</div>
					</div>
				</div>
				<div class="panel panel-default form-group">
					<div class="panel-heading" data-toggle="collapse" data-target="#options" aria-expanded="true" aria-controls="options"><strong>Global Options</strong></div>
					<div class="panel-body collapse in" id="options">
						<div class="content" style="overflow: hidden; display: block;">
							<div class="row">
								<div class="col-md-2">
									<blockquote>Global</blockquote>
								</div>
								<div class="col-md-10 form-inline">
									<div>
										Threads
										<input type="text" class="form-control" name="config[global][threads]" size="4" value=4>
										Timeout
										<input type="text" class="form-control" name="config[global][timeout]" size="4" value=10>
										Loglevel
										<div class="btn-group">
											<select class="form-control" name="config[global][timeout]">
												<option value="INFO">INFO</option>
												<option value="DEBUG">DEBUG</option>
											</select>
										</div>
										<!-- <input type="text" class="form-control" name="config[global][loglevel]" size="4" value="INFO"> -->
										GatherDepth
										<input type="text" class="form-control" name="config[global][gatherdepth]" size="4" value=1>
									</div>
								</div>
							</div>
							<div class="row">
								<div class="col-md-2">
									<blockquote>Proxies</blockquote>
								</div>
								<div class="col-md-8">
									<div class="checkbox">
										<label class="mcheck">
											<input type="checkbox" name="config[global][autoproxy]" checked ="checked">
											AutoProxies
										</label>
									</div>
								</div>
							</div>
							<div class="row form-line">
								<div class="col-md-2">
									<blockquote>User Agent</blockquote>
								</div>
								<div class="col-md-2">
									<div class="checkbox">
										<label class="mcheck">
											<input type="checkbox" name="config[global][autoagent]" checked ="checked">
											AutoAgents
										</label>
									</div>
								</div>
								<div class="col-md-6">
									<div class="input-group">
										<input type="text" class="form-control" name="config[global][useragent]" placeholder="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; .NET CLR 2.0.50727)" >
										<span class="input-group-addon glyphicon glyphicon-search"></span>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="panel panel-default form-group">
					<div class="panel-heading">
						<strong>Plugins Config Options:</strong>
						<input type="text" id="searchbox"/>
					</div>
					<div class="panel-body collapse in" id="modules">
						<div class="checkbox">
							<label class="mcheck">
								<input type="checkbox" id="test" name="config[plugins][Info_Collect][run]" checked ="checked"> Info Collect
							</label>
							<label class="mcheck">
								<input type="checkbox" name="config[plugins][Common][run]" checked ="checked"> Common
							</label>
							<label class="mcheck">
								<input type="checkbox" name="config[plugins][Sensitive_Info][run]" checked ="checked"> Sensitive Info
							</label>
							<label class="mcheck">
								<input type="checkbox" name="config[plugins][System][run]" checked ="checked"> System
							</label>
							<label class="mcheck">
								<input type="checkbox" name="config[plugins][Web_Applications][run]" checked ="checked"> Web Applications
							</label>
							<label class="mcheck">
								<input type="checkbox" name="config[plugins][Weak_Password][run]"> Weak Password
							</label>
							<label class="mcheck">
								<input type="checkbox" name="config[plugins][Others][run]"> Others
							</label>
						 </div>
					</div>
				</div>
				<!-- <div class="panel panel-default">
					<div class="panel-heading " ><button type="button" class="btn btn-danger" data-toggle="collapse" data-target="#demo" aria-expanded="true" aria-controls="demo">
				  simple collapsible
				</button></div>
					<div class="panel-body collapse in" id="demo" >

					</div>
				</div> -->
				<div>
					<button class="btn btn-warning btn-lg disabled" id="submit" onclick="task_create()">
						<span class="glyphicon glyphicon-flash"></span>
						Scan it!
					</button>
				</div>
			</form>
			<hr>
			<footer>
				<p>© Company 2014</p>
			</footer>
		</div>
		<!-- ================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script>
			$('input.search').searchbox({
				url: 'configs_search.php',
				param: 'name',
				dom_id: '#thumbnails',
				delay: 250,
				loading_css: '#spinner'
			})
		</script>
		<script>
			$(document).bind('after.searchbox', function() {alert('after.searchbox')});
		</script>
	</body>
</html>