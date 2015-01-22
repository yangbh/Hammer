<?php
require_once('common.php');

//
function search_dist($status,$os,$mac,$distid=0){
	// $pKeyword = check_sql($keyword);
	$pStatus = $status;
	$pOS = $os;
	$pMAC = $mac;
	$pId = $distid;
	$time = time();
	$ip = $_SERVER["REMOTE_ADDR"];
	if ($userid = get_userid()) {
		// echo $userid . '<br>';
	}
	else{
		die();
	}
	// echo $userid . '<br>';
	// echo $time . '<br>';
	// if Last_Time bigger than now time too much, such as 1 min, then set online status off
	$query = "UPDATE Dispatcher SET Status=0 WHERE $time-Last_Time>60";
	$result = mysql_query($query);

	// then select information
	$query = "SELECT Dispatcher.ID,Dispatcher.OS,Dispatcher.MAC,Dispatcher.IP,Dispatcher.Last_Time,Dispatcher.Status,User.Name FROM Dispatcher,User WHERE Dispatcher.User_ID=User.ID AND Dispatcher.User_ID='$userid'";
	if (is_int($pStatus) and $pStatus>=0 and $pStatus<2) {
		$query .= " AND Dispatcher.Status='$pStatus'";
	}
	if ($pOS) {
		$query .= " AND Dispatcher.OS like'%$pOS%'";
	}
	if ($pMAC) {
		$query .= " AND Dispatcher.MAC='$pMAC'";
	}
	if (is_int($pId) and $pId>0) {
		$query .= " AND Dispatcher.ID=$pId";
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

$os = check_sql(trim($_REQUEST['os']));
$mac = check_sql(trim($_REQUEST['mac']));
$status = None;
if ($_REQUEST['status']) {
	$status = (int)($_REQUEST['status']);
}
$distID = None;
if ($_REQUEST['distid']) {
	$distID = (int)($_REQUEST['distid']);
}
$data=search_dist($status,$os,$mac,$distID);
echo json_encode($data);
?>