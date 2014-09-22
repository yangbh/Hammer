<?php
require_once('common.php');

//
function search_scan($level,$keyword=''){
	// $pKeyword = check_sql($keyword);
	$pLevel = $level;
	$pKeyword = $keyword;
	if ($userid = get_userid()) {
		// echo $userid . '<br>';
	}
	else{
		die();
	}
	// echo $userid . '<br>';
	// print $pLevel.$pKeyword;
	$query = "SELECT Scan.ID,Scan.Url,Scan.Start_Time,Scan.End_Time,Scan.Level,Scan.Arguments,User.Name FROM Scan,User WHERE Scan.User_ID=User.ID AND Scan.User_ID='$userid'";
	if (is_int($pLevel) and $pLevel>0 and $pLevel<5) {
		$query .= " AND Scan.Level=$pLevel";
	}

	if ($pKeyword !='') {
		$query .= " AND Scan.Url LIKE '%$pKeyword%'";
	}
	// echo $query.'<br>';

	$ret = array('data' => [], );
	$result = mysql_query($query);
	while ($row = mysql_fetch_row($result)){
		// var_dump($row);
		foreach ($row as $key => $value){
			// echo $key.' => '.$value;
			$row[$key] = check_xss($value);
		}
		$ret['data'][] = $row;
		// var_dump($row);
	}
	return $ret;
}
//
function search_vuln($scanID){
	$pScanID = $scanID;
	if ($userid = get_userid()) {
		// echo $userid . '<br>';
	}
	else{
		die();
	}
	$query = "SELECT Vuln.IP_URL,Plugin.Name,Vuln.Vuln_Info,Vuln.Level FROM Plugin,Scan,Vuln WHERE Vuln.Scan_ID=Scan.ID AND Vuln.Plugin_ID=Plugin.ID AND Scan.ID=$scanID AND Scan.User_ID='$userid' ORDER BY Vuln.IP_URL,Vuln.Level";
	// echo $query.'<br>';

	$ret = array();
	$result = mysql_query($query);
	while ($row = mysql_fetch_row($result)){
		// var_dump($row);
		foreach ($row as $key => $value){
			// echo $key.' => '.$value;
			$row[$key] = check_xss($value);
		}
		$ipurl = $row[0];
		$ret[$ipurl][]=array_slice($row,1);
	}
	// var_dump($ret);
	return $ret;
}
?>
<?php
//	check login first
if (!already_login()) {
	die();
}

$keyword = check_sql(trim($_REQUEST['keyword']));
// echo $keyword . '<br>';
$level = (int)($_REQUEST['level']);
$scanID = (int)($_REQUEST['scanid']);
if ($scanID and $scanID!='') {
	$data = search_vuln($scanID);
	echo json_encode($data);
}
else{
	$data=search_scan($level,$keyword);
	echo json_encode($data);
}

?>