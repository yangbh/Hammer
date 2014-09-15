<?php
require_once('common.php');
?>
<?php
//	
function task_start(){

}

//
function task_end(){

}
//
function task_add($Url,$Time,$Arguments,$Level,$User_ID){

}

//	check login first
if (!already_login()) {
	die();
}

$type = check_sql(trim($_REQUEST['type']));
//	start a scan task
if ($type == 'start') {

	$url = check_sql(trim($_REQUEST['url']));
	// echo $url . '<br>';
	$startTime = $_SERVER['REQUEST_TIME'];	//自 PHP 5.1 起在 $_SERVER['REQUEST_TIME'] 中保存了发起该请求时刻的时间戳。
	// echo $startTime . '<br>';
	$args = check_sql(trim($_REQUEST['args']));
	// echo $args . '<br>';
	$userid = get_userid();
	// echo $userid . '<br>';
	$query = "INSERT INTO Scan(Url,Start_Time,Arguments,User_ID) Values('$url',$startTime,'$args',$userid)";
	// echo $query . '<br>';

	$result = mysql_query($query);
	if ($row = mysql_fetch_array($result)) {
		// echo $row;
	}
	// return start time
	$ret = array('startTime' => $startTime);
	echo json_encode($ret);
}
//	end a scan task
elseif ($type == 'end') {
	$scanurl = check_sql(trim($_REQUEST['url']));
	// echo $scanurl . '<br>';
	$startTime = (int)($_REQUEST['startTime']);
	// echo $startTime . '<br>';
	$retinfo = json_decode(trim($_REQUEST['retinfo']));
	var_dump($retinfo);
	//
	$scanLevel = 'info';
	$endTime = $_SERVER['REQUEST_TIME'];

	//	get scan id
	$query = "SELECT ID FROM Scan WHERE Start_Time=$startTime AND Url='$scanurl' limit 1";
	echo $query . '<br>';
	$result = mysql_query($query);
	if ($row = mysql_fetch_array($result)) {
		$scanID = $row[0];
		echo $scanID . '<br>';
	}

	foreach ($retinfo as $key => $eachVuln) {
		print_r($eachVuln);
		$vulnType = $eachVuln['type'];
		$vulnLevel = $eachVuln['level'];
		$vulnContent = $eachVuln['content'];
		if(is_array($content)){
			$content = json_encode($content);
		}

		//	get plugin id
		$query = "SELECT ID FROM Plugin WHERE Name=$vulnType limit 1";
		echo $query . '<br>';
		$result = mysql_query($query);
		if ($row = mysql_fetch_array($result)) {
			$pluginID = $row[0];
			echo $pluginID . '<br>';
		}

		//
		$query = "INSERT INTO Vuln(IP_URL,Scan_ID,Plugin_ID,Vuln_Info,Level) VALUES('$scanurl',$scanID,$pluginID,'$vulnContent',$vulnLevel)";
		echo $query . '<br>';
	}
}

?>