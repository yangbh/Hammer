<?php
require_once('common.php');

//
function search_scan($level,$keyword='',$scanid=0){
	// $pKeyword = check_sql($keyword);
	$pLevel = $level;
	$pKeyword = $keyword;
	$pId = $scanid;
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
	if (is_int($pId) and $pId>0) {
		$query .= " AND Scan.ID=$pId";
	}

	// echo $query.'<br>';

	$ret = array('data' => array(), );
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
$data=search_scan($level,$keyword,$scanID);
echo json_encode($data);
?>