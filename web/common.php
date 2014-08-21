<?php
require_once('config.php');
//	init mysql db
# start session
session_set_cookie_params(2*3600);
session_start();

$con = mysql_connect($DB_HOST,$DB_USER,$DB_PWD,$DB_NAME);

if (!$con) {
	die('Could not connect: ' . mysql_error());
}
mysql_select_db($DB_NAME,$con)

?>
<?php
function check_input($value){
	// 去除斜杠
	if (get_magic_quotes_gpc()){
		$value = stripslashes($value);
	}
	// 如果不是数字则加引号
	if (!is_numeric($value)){
		$value = mysql_real_escape_string($value);
	}
	return $value;
}

function already_login(){
	if ($_SESSION['user']) {
		// header('Location: index.php');
		// exit;
		return True;
	}
	// header('Location: login.php');
	// exit;
	return False;
}

function pwd_encode($username,$password){
	global $DB_SALT;
	$Pwd = strrev($username).'#'. $DB_SALT .'#'.strrev($password);
	$Pwd = md5($Pwd);
	return $Pwd;
}
?>