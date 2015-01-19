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
		<!-- jquery -->
		<!-- <script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
		<script src="js/jquery.min.js"></script>
		
		<!-- Bootstrap core CSS -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<!-- Bootstrap core JavaScript -->
		<script type="text/javascript" src="js/bootstrap.min.js"></script>

		<style type="text/css">
			a span{
				color: #555;
				text-decoration: none;
			}
			.tooltip-inner {
				max-width: 768px;
				/* If max-width does not work, try using width instead */
				width: 768px; 
			}

		</style>


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
			//	tooltip	
			var options={
				animation:true,
				trigger:'hover' //触发tooltip的事件
			}
			$('.atip').tooltip(options);

			// DataTable
			$('#scans_table').DataTable({
				// "ajax": "./datatable.json",
				"ajax": "./task_search.php",
				// "paging":   false,
				"lengthChange": false, //改变每页显示数据数量
				"pageLength": 15,
				// "info":     false,
				"filter":   false,
				// "ordering": false,
				"order":    [2, "desc" ],
				"columnDefs": [
					{
						"targets": [ 0,6 ],
						"visible": false,
						"searchable": false
					},
					{
						"targets": [1],
						"render": function ( data, type, full, meta ) {
								// return "<a class=\"plugin\" href='search.php?name="+encodeURI(data)+"'>"+data+"</a>";
								return "<a class=\"plugin\" href=\""+"vulns.php#"+full[0]+"\">"+data+"</a>";
						}
					},
					{
						"targets":[2],
						"render": function ( data, type, full, meta ) {
								var d = new Date();
								d.setTime(parseInt(data)*1000);
								// alert(d.toString());
								return d.Format("yyyy-MM-dd hh:mm:ss");
						}
					},
					{
						"targets": [3],
						"visible": false,
						"searchable": false
					},
					{
						"targets":[4],
						"render": function ( data, type, full, meta ) {
							if (data.length>32) {
								var showdata=data.substring(0,128);
								// console.log(data);
								var ret = '<a href="#" class="atip" data-toggle="tooltip" data-container="body" data-original-title="'+data+'">'+showdata+'</a>';
								$('.atip').tooltip({
										trigger:'hover focus'
									});
								return ret;
							};
						}
					},
					{
						"targets": [8],
						"render": function ( data, type, full, meta ) {
							return '<span class="glyphicon glyphicon-edit"></span>	\
									<span class="glyphicon glyphicon-remove"></span>';
						}
					},
				 ]
			});

			$('#plugin_goback').click(function(){
				$('#plugins').show('slow');
			});

			//  search button click
			$('#search').click(function() {
				/* Act on the event */
				var ajax_url = "./task_search.php?level="+$('#level').val()+"&keyword="+$('#keyword').val();
				$('#scans_table').DataTable().ajax.url(ajax_url).load();
			});


		});
		</script>
	</head>

	<body>
		<!-- Main jumbotron for a primary marketing message or call to action -->
		<div class="container">
			<div class="row" id="plugins">
				<div class="container" >
					<h1>
						<a href="index.php">
							<!-- <small><span class="glyphicon glyphicon-home"></span></small> -->
							<span class="glyphicon glyphicon-home"></span>
						</a>
						<a href="javascript:history.back()">
							<span class="glyphicon glyphicon-circle-arrow-left"></span>
						</a>
						&nbsp;Tasks
						<!-- <a class="glyphicon glyphicon-circle-arrow-left" id="plugin_goback" href="javascript:history.back()"></a>&nbsp; -->
					</h1>
						<div class="form-inline">
<!-- 							<div class="form-group">
								<input type="text" class="form-control" value="2012-05-15" id="datetimepicker" data-date-format="yyyy-mm-dd">
							</div> -->
							<div class="btn-group">
								<select class="form-control" name="level" id="level">
									<option value="0">All Status</option>
									<option value="1">Done</option>
									<option value="2">Running</option>
									<option value="3">Waiting</option>
									<option value="3">Others</option>
								</select>
							</div>
							<div class="form-group">
								<input type="text" class="form-control" id="keyword" placeholder="Target Keyword" name="keyword">
							</div>
							<button id="search" class="btn btn-default">Search</button>
						</div>
					<div class="table-responsive">
						<table id="scans_table" class="table table-striped">
							<thead>
								<tr>
									<th>ID</th>
									<th>Target</th>
									<th>Start_Time</th>
									<th>End_Time</th>
									<th>Arguments</th>
									<th>Status</th>
									<th>User_Name</th>
									<th>Dispatcher</th>
									<th>Operation</th>
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
