<?php
require_once('common.php');

//	check login first
if (!already_login()) {
	die();
}
//
function search_config($name){
	$name = check_sql($name);
	$userId = $_SESSION['userID'];

	$query = "SELECT Config.ID,Config.Name,Config.Time,Config.Config,Config.AutoI,Config.Description,Config.IsDefault FROM Config,User WHERE Config.User_ID=User.ID AND Config.Name LIKE '%$name%'";
	// echo $query.'<br>';

	$ret = array('data' => array(), );
	$result = mysql_query($query);
	while ($row = mysql_fetch_row($result)){
		// foreach ($row as $key => $value){
		// 	$row[$key] = check_xss($value);
		// }
		$ret['data'][] = $row;
		// var_dump($row);
	}
	return $ret;
}
?>
<?php

$name = check_sql(trim($_REQUEST['name']));
$data=search_config($name);
echo json_encode($data);
?>