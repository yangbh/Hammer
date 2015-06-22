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

		<link href="css/skins/line/blue.css" rel="stylesheet">
		<script src="js/jquery.icheck.min.js"></script>

		<!-- Bootstrap core JavaScript -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript" src="js/bootstrap.min.js"></script>

		<link href="css/live-search.css" rel="stylesheet">
		<script type="text/javascript" src="js/foot-2-live-search.js"></script>

		<link href="css/jsoneditor.css" rel="stylesheet">
		<script src="js/jquery.jsoneditor.js"></script>

		<!-- <script type="text/javascript" src="js/bootstrap-collapse.js"></script> -->
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
			.panel {
				margin-top: 5px;
				margin-bottom: 5px;
			}
			blockquote {
				margin:0px;
				padding: 1px;
				font-size: 15px;
			}
			#legend {
				display: inline;
				margin-left: 30px;
			}
			#legend h2 {
				 display: inline;
				 font-size: 18px;
				 margin-right: 20px;
			}
			#legend a {
				color: white;
				margin-right: 20px;
			}
			#legend span {
				padding: 2px 4px;
				-webkit-border-radius: 5px;
				-moz-border-radius: 5px;
				border-radius: 5px;
				color: white;
				font-weight: bold;
				text-shadow: 1px 1px 1px black;
				background-color: black;
			}
			#legend .string  { background-color: #009408; }
			#legend .array   { background-color: #2D5B89; }
			#legend .object  { background-color: #E17000; }
			#legend .number  { background-color: #497B8D; }
			#legend .boolean { background-color: #B1C639; }
			#legend .null    { background-color: #B1C639; }

			#expander {
				cursor: pointer;
				margin-right: 20px;
			}
		</style>
		<script>
		function task_create(){
			// check target
			if ($("#target").val() == '') {alert("target cannot be empty");return;};
			
			//	
			var str_data='';
			$("#dlg_form input,textarea,select").each(function(){
				if($(this).attr("name") != undefined){
					if ($(this).attr("type")=="checkbox") {
						str_data += $(this).attr("name") + "=" + ($(this).attr("checked")=="checked"?1:0) + "&";
					}
					else{
						str_data += $(this).attr("name") + "=" + $(this).val() + "&";
					}
				}
			});
			// console.log(str_data);

			//	ajax post data
			$.ajax({
				type: "POST",
				url: "task_add.php",
				data: str_data,
				success: function(msg){
					if (msg == true) {alert('Add Task Success');}
					else {alert('Add Task Faild' + msg);}
					location.href = 'scans.php';
				}
			});
		}
		function show_config(span){
			// this.text = 'hehe';
			console.log(span);
			// span.text('test');
			console.log(span.id);
			var id = span.id;
			$('span[id="'+id+'"]').removeClass('label-info');
			$('span[id="'+id+'"]').addClass('label-info');

			// console.log(this.class);
			// console.log($(this).html());
		}
		$(document).ready(function () {

			// $('.input').iCheck({
			// 	checkboxClass: 'icheckbox_minimal-blue',
			// 	radioClass: 'iradio_minimal-blue',
			// 	increaseArea: '20%' // optional
			// });

			$.ajax({
				type: "POST",
				url: "dist_search.php",
				data: "status=0",
				dataType: "json",
				success: function(data){
					console.log(data.data);
					dists = data.data;
					if (dists.length) {
						var html = '';
						console.log('yes');
						for (var i = dists.length - 1; i >= 0; i--) {
							dist = dists[i];
							if (dist[5]=='1') {
								html += '<span class="label label-info">'+dist[1]+'@'+dist[3]+'</span>&nbsp;';
							}
						};
						$('#dists').html(html);
						$('#submit').removeClass('disabled');
					}
				}
			});


			$.ajax({
				type: "GET",
				url: 'configs_search.php',
				data: "name=",
				dataType: "json",
				success: function(data){
					console.log(data.data);
					configs = data.data;
					var spans = '<ul class="list-inline">';
					for(var i =0;i < configs.length; i++){
						config = configs[i];
						if(config[6] == '1'){
							spans += '<li>\
								<input tabindex="15" type="radio" id="flat-radio-1" name="flat-radio" checked>\
								<label for="flat-radio-1">'+ config[1] +'</label></li>';
							// spans += '<button type="button" class="btn btn-primary btn-sm" onclick="javascript:show_config(this.id)" id="'+config[1]+'">'+config[1]+'</button>';
						}
						else{
							spans += '<li>\
								<input tabindex="15" type="radio" id="flat-radio-1" name="flat-radio">\
								<label for="flat-radio-1">'+ config[1] +'</label></li>';
							}
					}
					spans += '</ul>';
					$('#configs').html(spans);
					
					$('li > input').click(function(){
						// $(this).parent().attr("");
						var name = $(this).parent().children("label").text();
						// alert(name);
						$.ajax({
							url:'configs_search.php',
							data: {name: name},
							type: "GET",
							dataType: 'json',
							success: function(json){
								jsondata = json.data[0];
								// alert('json:'+json.data);
								// alert(jsondata);
								var id = jsondata[0];
								var name = jsondata[1];
								var time = jsondata[2];
								var json = JSON.parse(jsondata[3]);
								var autoi = jsondata[4];
								// alert(json);
							
								function printJSON() {
									$('#json').val(JSON.stringify(json));
								}

								function updateJSON(data) {
									json = data;
									printJSON();
								}

								function showPath(path) {
									$('#path').text(path);
								}

								$(document).ready(function() {

									$('#rest > button').click(function() {
										var url = $('#rest-url').val();
										$.ajax({
											url: url,
											dataType: 'jsonp',
											jsonp: $('#rest-callback').val(),
											success: function(data) {
												json = data;
												$('#editor').jsonEditor(json, { change: updateJSON, propertyclick: showPath });
												printJSON();
											},
											error: function() {
												alert('Something went wrong, double-check the URL and callback parameter.');
											}
										});
									});

									$('#json').change(function() {
										var val = $('#json').val();

										if (val) {
											try { json = JSON.parse(val); }
											catch (e) { alert('Error in parsing json. ' + e); }
										} else {
											json = {};
										}
										
										$('#editor').jsonEditor(json, { change: updateJSON, propertyclick: showPath });
									});

									$('#expander').click(function() {
										var editor = $('#editor');
										editor.toggleClass('expanded');
										$(this).text(editor.hasClass('expanded') ? 'Collapse' : 'Expand all');
									});
									
									printJSON();
									$('#editor').jsonEditor(json, { change: updateJSON, propertyclick: showPath });

								});
							}
						});
					});

					// 默认
					$('li > input')[0].click();
				}
			});
		});

		</script>
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
				Task Add
				<!-- &nbsp;Plugin Code -->
				<!-- <a class="glyphicon glyphicon-circle-arrow-left" id="plugin_goback" href="javascript:history.back()"></a>&nbsp; -->
			</h1>
			<div class="form" id="dlg_form">
<!-- 				<div class="form-inline">
					<div class="btn-group">
						<select class="form-control" name="config[global][mode]" id="mode">
							<option value="1">Signal Target</option>
							<option value="2">Multi Targets</option>
							<option value="3">Others</option>
						</select>
					</div>
					<div class="form-group">
						<input type="text" class="form-control" id="target" name="config[global][target]" size="30" placeholder="testphp.vulnweb.com">
						<label class="control-label" for="target">(Exp: http://testphp.vulnweb.com/)</label>
					</div>
				</div> -->
			<!-- 	<div class="btn-group">
						<select class="form-control" name="config[global][mode]" id="mode">
							<option value="1">Signal Target</option>
							<option value="2">Multi Targets</option>
						</select>
					</div> -->
				<div class="panel panel-default form-group">
					<div class="panel-heading"><strong>Targets</strong></div>
					<div class="panel-body collapse in" id="modules" style="padding:5px">
						<div class="content">
							<div class="row">
								<div class="col-md-6" style="margin:0px">
									<textarea class="form-control" id="target" name="config[global][target]" size="50" rows="3" placeholder="http://testphp.vulnweb.com"></textarea>
								</div>
								<div class="col-md-6">
									<div class="list-group" style="margin:0px">
										<h4 class="list-group-item-heading">Notice: One Target Per Line</h4>
										<p class="list-group-item-text">Targets can be: http://testphp.vulnweb.com -- url
											<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;www.vulnweb.com -- host
											<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;192.168.0.1/24 -- ip or ip range</p>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="panel panel-default form-group">
					<div class="panel-heading"><strong>Dispachers</strong></div>
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
						<div class="row">
							<div class="col-md-3">
								<strong>Plugins Config Options</strong>
							</div>
						</div>
					</div>

					<div class="panel-body collapse in" id="modules">
						<div class="row form-line">
							<div class="col-md-2">
								<blockquote>Configs</blockquote>
							</div>
							<div class="col-md-10" id="configs">
							</div>
						</div>
						<div class="panel panel-default form-group">
							<div class="panel-body collapse in" id="modules">
								<div class="row">
									<div class="col-md-12">
										<textarea id="json" class="form-control" rows="3" name="config[plugins]"></textarea>
									</div>
								</div>
								<hr>
								<div class="row">
									<div class="col-md-12" id="legend">
										<span id="expander">Expand all</span>
										<span class="array">array</span>
										<span class="object">object</span>
										<span class="string">string</span>
										<span class="number">number</span>
										<span class="boolean">boolean</span>
										<span class="null">null</span>
										Notice: Remove item by deleting a property name.
									</div>
								</div>
								<!-- <pre id="path"></pre> -->
								<div id="editor" class="json-editor"></div>
							</div>
						</div>

					</div>
				</div>
				<div>
					<button class="btn btn-warning btn-default disabled" id="submit" onclick="task_create()">
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
	</body>
</html>