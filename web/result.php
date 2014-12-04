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
		<!-- <link href="css/bootstrap.min.css" rel="stylesheet"> -->
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
			//  hide plugin_code div
			$('#code').show('fast');
			//  snippet
			$("pre.python").snippet("python",{style:"vim",menu:false,showNum:true});

			// datatime
			$('#datetimepicker').datetimepicker();


			//  <a> links in tables

			var scanID= document.location.hash.substr(1);
			console.log('scanID='+scanID)
			// alert(scanID);
			$.get("scans_search.php",{scanid: scanID},function(data){
				$('#plugins').hide('slow');
				$('#code').show('slow');
				// $('#plugin_code').html(data);
				$('#scan_results').empty();
				$('#scan_title').empty();
				//
				var json = jQuery.parseJSON(data);
				$.each(json,function(i,n){
					var ipurl = i;
					var html="<div><blockquote><h3>"+ipurl+"</h3></blockquote></div>"
					var extflag = true;
					$('#scan_results h3').each(function(){
						if ($(this).text()==i) {
							extflag = false;
						}
					});

					if (extflag) {
						$('#scan_results').append(html);
					};

					$.each(n,function(i2,n2){
						$('#scan_results h3').each(function(){
							if ($(this).text()==i) {
								var plugin = n2[0];
								var content = n2[1];
								var level = n2[2];
								var extflag = true;
								// console.log($(this));
								$(this).parent().parent().find('h4').each(function(){
									//console.log('$(this).text()='+$(this).text());
									//console.log('plugin='+plugin);
									if ($(this).text()==plugin) {
										extflag = false;
										html = "<li>";
										html+= content;
										html += "</li>";
										$(this).parent().children('ul').append(html);
									}
								});
								if (extflag) {
									html = "<ul><li>";
									var color = "text-muted";
									switch(level){
										case '1':
											color = "text-success";
											break
										case '2':
											color = "text-info";
											break;
										case '3':
											color = "text-warning";
											break;
										case '4':
											color = "text-danger";
											break;
										default:
											color = "text-muted";
									}
									html += "<h4 class=\""+color+"\">"+plugin+"</h4>";
									html += "<ul><li>";
									html += content;
									html += "</li></ul>";
									$(this).parent().after(html);
								}
							}
						});
					});
				});
			});
		});
		</script>
	</head>

	<body>

		<!-- Main jumbotron for a primary marketing message or call to action -->
		<div class="container">
			<div class="row" id="code" hidden="true">
			<div class="container" >
				<h1>
					<a class="glyphicon glyphicon-circle-arrow-left" id="plugin_goback" href="javascript:history.back()"></a>&nbsp;
					<small>Scan Results</small>
				</h1>
				<!-- <pre class="python" id="plugin_code"></pre> -->
				<div class="panel" id="scan_title">
				</div>
				<div class="panel" id="scan_results">
				</div>
			</div>
			</div>
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