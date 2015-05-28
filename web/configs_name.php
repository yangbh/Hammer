<?php
require_once('common.php');

//  check login first
if (!already_login()) {
	error_jump();
}
?>
<?php
function search_config($s){
	$name = check_sql($name);
	$userId = $_SESSION['userID'];

	$query = "SELECT Config.Name,Config.Description FROM Config,User WHERE Config.User_ID=User.ID AND Config.Name like '%$name%'";
	// echo $query.'<br>';

	$ret = array();
	$result = mysql_query($query);
	while ($row = mysql_fetch_row($result)){
		foreach ($row as $key => $value){
			$row[$key] = check_xss($value);
		}
		$ret[] = $row;
		// var_dump($row);
	}
	return $ret;
}
?>
<?php
if (isset($_SERVER['HTTP_X_REQUESTED_WITH']) and strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest'){
	$ret = search_config($_GET['s']);
	echo '<ul>';
	foreach ($ret as $row){
		echo '<li><a href="#">'.$row[0].'</a></li>';
		// var_dump($row);
	}
	echo '</ul>';
}
?>