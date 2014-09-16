<?php
require_once('common.php');

//
function search_vuln($level,$keyword=''){
	// $pKeyword = check_sql($keyword);
	$pLevel = $level;
	$pKeyword = $keyword;
	// print $pLevel.$pKeyword;
	$query = "SELECT Scan.ID,Scan.Url,Scan.Start_Time,Scan.End_Time,Scan.Level,Scan.Arguments,User.Name FROM Scan,User WHERE Scan.User_ID=User.ID";
	if (is_int($pLevel) and $pLevel>=0 and $pLevel<=3) {
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
?>
<?php
//	check login first
if (!already_login()) {
	die();
}

$keyword = check_sql(trim($_REQUEST['keyword']));
$level = (int)($_REQUEST['level']);
$scanID = (int)($_REQUEST['scanid']);
// echo $keyword . '<br>';
$data=search_vuln($level,$keyword);
echo json_encode($data);
?>