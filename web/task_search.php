<?php
require_once('common.php');

//
function search_task($level,$keyword='',$taskid=0){
	// $pKeyword = check_sql($keyword);
	$pLevel = $level;
	// echo $pLevel.'<br>';
	$pKeyword = $keyword;
	$pId = $taskid;
	if ($userid = get_userid()) {
		// echo $userid . '<br>';
	}
	else{
		die();
	}
	// echo $userid . '<br>';
	// print $pLevel.$pKeyword;
	$query = "SELECT Task.ID,Task.Target,Task.Start_Time,Task.End_Time,Task.Arguments,Task.Status,User.Name,CONCAT(Dispatcher.ID,':',Dispatcher.MAC,':',Dispatcher.OS,':',Dispatcher.IP) 
			FROM Task
			INNER JOIN User ON Task.User_ID=User.ID
			LEFT JOIN Dispatcher ON Dispatcher.ID=Task.Dispatcher_ID 
			WHERE Task.User_ID='$userid'";
	if (is_int($pLevel) and $pLevel>0 and $pLevel<4) {
		$pLevel = ($pLevel==1)?'done':($pLevel==2?'running':($pLevel==3?'waiting':'others'));
		$query .= " AND Task.Status='$pLevel'";
	}
	if ($pKeyword !='') {
		$query .= " AND Task.Target LIKE '%$pKeyword%'";
	}
	if (is_int($pId) and $pId>0) {
		$query .= " AND Task.ID=$pId";
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
$level = (int)($_REQUEST['level']);
$taskID = (int)($_REQUEST['taskid']);
$data=search_task($level,$keyword,$taskID);
echo json_encode($data);
?>