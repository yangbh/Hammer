<?php
require_once('common.php');
?>
<?php
//	check login first
if (!already_login()) {
	echo 'false';
	die();
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
		
		<!-- <script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
				<script src="js/jquery.min.js"></script>
		<!-- ================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<!-- Bootstrap core JavaScript -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
	
		<link href="css/jsoneditor.css" rel="stylesheet">
		<script src="js/jquery.jsoneditor.js"></script>

		<!-- <script src="js/jsoneditor.js"></script> -->

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
			function update_config(){
				var str_data='';
				$("#dlg_form input#name,textarea#json").each(function(){
					str_data += $(this).attr("name") + "=" + $(this).val() + "&";
				});
				var autoi = new Array();
				$('#dlg_form input[type="checkbox"]').each(function(){
					var checked = this.checked?1:0;
					autoi.push(checked);
				});
				str_data += '&autoi=' + autoi.join('|');

				console.log(str_data);

				//	ajax post data
				$.ajax({
					type: "POST",
					url: "configs_update.php",
					data: str_data,
					success: function(msg){
						if (msg == 'true') {alert('Update Success');}
						else {alert('Update Faild' + msg);}
						location.href = 'configs.php';
					}
				});
			}
			$.ajax({
				url:'configs_search.php',
				data: {name: location.hash.substr(1)},
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
					var autoi = jsondata[4].split('|');
					// console.log(autoi);
			
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

						$('#name')[0].value = name;

						$('#Common_Check')[0].checked = parseInt(autoi[0]);
						$('#Info_Collect_Check')[0].checked = parseInt(autoi[1]);
						$('#Sensitive_Info_Check')[0].checked = parseInt(autoi[2]);
						$('#System_Check')[0].checked = parseInt(autoi[3]);
						$('#Weak_Password_Check')[0].checked = parseInt(autoi[4]);
						$('#Web_Applications_Check')[0].checked = parseInt(autoi[5]);
						$('#Others_Check')[0].checked = parseInt(autoi[6]);

					});
				}
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
				Plugins Configuration
			</h1>
			<div class="form" id="dlg_form">
				<div class="panel panel-default form-group">
					<div class="panel-heading"><strong>Settings</strong></div>

					<div class="panel-body collapse in" id="modules">
						<div class="content" style="overflow: hidden; display: block;">
							<div class="row">
								<div class="col-md-2">
									<blockquote>Name</blockquote>
								</div>
								<div class="col-md-10 form-inline">
									<input type="text" class="form-control" id="name" name="name" value=1>
								</div>
							</div>
							<div class="row">
								<div class="col-md-2">
									<blockquote>Auto Incresment</blockquote>
								</div>
								<div class="col-md-8">
									<ul class="list-inline">

										<li>
											<input type="checkbox" id="Common_Check" checked ="checked">			
											<label class="mcheck">Common</label>	
										</li>
										<li>
											<input type="checkbox" id="Info_Collect_Check" checked ="checked">			
											<label class="mcheck">Info_Collect</label>	
										</li>
										<li>
											<input type="checkbox" id="Sensitive_Info_Check"  checked ="checked">			
											<label class="mcheck">Sensitive_Info</label>	
										</li>
										<li>
											<input type="checkbox" id="System_Check"  checked ="checked" id="autoi">			
											<label class="mcheck">System</label>	
										</li>
										<li>
											<input type="checkbox" id="Weak_Password_Check"  checked ="checked" id="autoi">			
											<label class="mcheck">Weak_Password</label>	
										</li>
										<li>
											<input type="checkbox" id="Web_Applications_Check"  checked ="checked" id="autoi">			
											<label class="mcheck">Web_Applications</label>
										</li>
										<li>
											<input type="checkbox" id="Others_Check" id="autoi">			
											<label class="mcheck">Others</label>
										</li>										
									</ul>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="panel panel-default form-group">
					<div class="panel-heading"><strong>Value</strong></div>
					<div class="panel-body collapse in" id="modules">
						<div class="row">
							<div class="col-md-12">
								<textarea id="json" class="form-control" rows="3" name="config"></textarea>
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
				<div>
					<button class="btn btn-warning btn-default" id="submit" onclick="update_config()">
						<span class="glyphicon glyphicon-flash"></span>
						Update!
					</button>
				</div>

			</div>
	</body>
</html>
