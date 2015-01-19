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
		<style type="text/css">
			a span{
				color: #555;
				text-decoration: none;
			}
			pre {
				display: block;
				padding: 9.5px;
				margin: 0 0 10px;
				font-size: 13px;
				line-height: 20px;
				word-break: break-all;
				word-wrap: break-word;
				white-space: pre;
				white-space: pre-wrap;
				background-color: #f5f5f5;
				border: 1px solid #ccc;
				border: 1px solid rgba(0, 0, 0, 0.15);
				-webkit-border-radius: 4px;
				   -moz-border-radius: 4px;
						border-radius: 4px;
			}
			li.L0, li.L1, li.L2, li.L3,li.L5, li.L6, li.L7, li.L8{
				list-style-type: decimal !important
			}
			.bs-callout{
				margin-top: 10px;
				margin-bottom: 0px;
				padding-top: 10px;
				padding-bottom: 10px;
			}
			blockquote {
				margin: 0px;
				margin-bottom: 0px;
			}
		</style>
		
		<!-- jquery -->
		<!-- <script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
		<script src="js/jquery.min.js"></script>

		<!-- Bootstrap core JavaScript -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		
		<!-- DataTables -->
		<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.css">
		<script type="text/javascript" charset="utf8" src="js/jquery.dataTables.js"></script>

		<!-- google code prettify -->
		<link href="js/prettify.css" type="text/css" rel="stylesheet" />
		<script type="text/javascript" src="js/prettify.js"></script>


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
		$(document).ready(function (){
			// prettyPrint();

			var pluginID= parseInt(document.location.hash.substr(1));
			// console.log(pluginID)
			$.get('code_search.php',{id: pluginID},function(data){
				var json = jQuery.parseJSON(data);
				var name = json.data[0][1];
				var type = json.data[0][2];
				var author = json.data[0][3];
				var time = parseInt(json.data[0][4]);
				// console.log(time);
				var version = json.data[0][5];
				var web = json.data[0][6];	
				var description = json.data[0][7];
				console.log(description);
				
				var code = json.data[0][8];
				$("#code h3 span:first").text(name);
				$('#plugin_code').html(code);
				prettyPrint();
				var webhtml = '';
				if(web!=''){
					webhtml = '';
					urls = web.split(',');
					for (var i = 0; i < urls.length; i++) {
					 	webhtml += "<a href=\""+urls[i]+"\">"+urls[i]+"</a><br>";
					}; 
				}
				$("#description").html(webhtml+description);
				// var d = new Date();
				// d.setTime(time*1000);
				// $("#author").text(d.Format("yyyy-MM-dd hh:mm:ss")+' by '+author);
				$("#author").text(time+' by '+author)
			});

		});
		</script>
	</head>

	<body>

		<!-- Main jumbotron for a primary marketing message or call to action -->
		<div class="container">
			<div class="row" id="code">
				<div class="container" >
					<h1>
						<a href="index.php">
							<!-- <small><span class="glyphicon glyphicon-home"></span></small> -->
							<span class="glyphicon glyphicon-home"></span>
						</a>
						<a href="javascript:history.back()">
							<span class="glyphicon glyphicon-circle-arrow-left"></span>
						</a>
						<!-- &nbsp;Plugin Code -->
						<!-- <a class="glyphicon glyphicon-circle-arrow-left" id="plugin_goback" href="javascript:history.back()"></a>&nbsp; -->
					</h1>
					<div id="code" style="margin-bottom: 0px;">
						<div>
							<h3>
								<span></span>
								<span class="label label-info"></span>
							</h3>
						</div>
						<div>
							<blockquote style="margin-bottom: 0px;"><strong>Description</strong></blockquote>
							<span class="text" id="description">https://www.yascanner.com/#!/n/65</span>
							<blockquote style="margin-bottom: 0px;"><strong>Source Code</strong></blockquote>
							<pre class="prettyprint linenums Lang-python" id="plugin_code"></pre>
							<blockquote style="margin-bottom: 0px;"><strong>Public Date</strong></blockquote>
							<span class="text" id="author"></span>
						</div>
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
		<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.css">
		<script type="text/javascript" charset="utf8" src="js/jquery.dataTables.js"></script>

		<!-- datatimepicker -->
		<link rel="stylesheet" type="text/css" href="css/bootstrap-datetimepicker.min.css">
		<script type="text/javascript" charset="utf8" src="js/bootstrap-datetimepicker.min.js"></script>

		<!-- snippet -->
		<link rel="stylesheet" type="text/css" href="css/jquery.snippet.min.css">
		<script type="text/javascript" charset="utf8" src="js/jquery.snippet.min.js"></script>
	</body>
</html>