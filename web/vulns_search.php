<?php
require_once('common.php');
//
function search_vuln($scanID){
	$pScanID = $scanID;
	// echo $pScanID.'<br>';
	if ($userid = get_userid()) {
		// echo $userid . '<br>';
	}
	else{
		die();
	}
	$query = "SELECT Vuln.IP_URL,Plugin.Name,Vuln.Vuln_Info,Vuln.Level FROM Plugin,Scan,Vuln WHERE Vuln.Scan_ID=Scan.ID AND Vuln.Plugin_ID=Plugin.ID AND Scan.ID=$scanID AND Scan.User_ID='$userid' ORDER BY Vuln.IP_URL,Vuln.Level,Vuln.ID";
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
if (!already_login()){
	die();
}
$level = (int)($_REQUEST['level']);
$scanID = (int)($_REQUEST['scanid']);
// echo $scanID.'<br>';
$data = search_vuln($scanID);
echo json_encode($data);
?>