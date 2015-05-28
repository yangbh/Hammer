<?php
require_once('config.php');
//	init mysql db
# start session
session_set_cookie_params(2*3600);
session_start();

ini_set('display_errors','off');
// error_reporting(E_ALL);
// error_reporting(E_ERROR);
$con = mysql_connect($DB_HOST.':'.$DB_PORT,$DB_USER,$DB_PWD,$DB_NAME);

// $con = mysql_connect($DB_HOST,$DB_USER,$DB_PWD,$DB_NAME);

if (!$con) {
	die('Could not connect: ' . mysql_error());
}
mysql_select_db($DB_NAME,$con);
mysql_query('set names utf8');

?>
<?php
function check_sql($value){
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

function check_xss($value){
	return htmlspecialchars($value,ENT_QUOTES,'UTF-8');
}

function pwd_encode($username,$password){
	global $DB_SALT;
	$Pwd = strrev($username).'#'. $DB_SALT .'#'.strrev($password);
	$Pwd = md5($Pwd);
	return $Pwd;
}

function error_jump(){
	echo "<script>window.location='index.php';</script>";
}

function login_check($username,$password){
	global $con,$DB_SALT;
	// print $username.$password.$DB_SALT;
	// $Pwd = strrev($username).'#'. $DB_SALT .'#'.strrev($password);	
	// $Pwd = md5($Pwd);
	if ($username && $password) {
		$Pwd = pwd_encode($username,$password);
		$query = "SELECT * FROM User WHERE NAME='" . $username . "' AND Password='". $Pwd . "'";
		// print '$query= '. $query . '<br>';
		$result = mysql_query($query);
		if ($row = mysql_fetch_array($result)) {
			$_SESSION['user'] = $row['Name'];
			$_SESSION['userID'] = $row['ID'];
			$_SESSION['isadmin'] = $row['Is_Admin'];
			return True;
		}
	}

	// check token
	$token = check_sql(trim($_REQUEST['token']));
	if ($token and $token != '') {
		$query = "SELECT * From User WHERE Token='$token'";
		// print '$query= '. $query . '<br>';
		$result = mysql_query($query);
		if ($row = mysql_fetch_array($result)) {
			$_SESSION['user'] = $row['Name'];
			$_SESSION['userID'] = $row['ID'];
			$_SESSION['isadmin'] = $row['Is_Admin'];
			return True;
		}
	}

	return False;
}

function already_login(){
	if ($_SESSION['user']) {
		// print $_SESSION['user'];
		// header('Location: index.php');
		// exit;
		return True;
	}
	return login_check();
	// header('Location: login.php');
	// exit;
	// return False;
}

function get_userid(){
	global $con;
	if (already_login()) {
		$username = $_SESSION['user'];
		$query = "SELECT ID FROM User WHERE Name='$username'";
		// echo '$query='.$query.'<br>';
		$result = mysql_query($query);
		if ($row = mysql_fetch_array($result)) {
			return $row[0];
		}
	}
	else{
		return False;
	}
}

function get_userinfo(){
	global $con;
	if (already_login()) {
		$username = $_SESSION['user'];
		$query = "SELECT * FROM User WHERE Name='$username'";
		// echo '$query='.$query.'<br>';
		$result = mysql_query($query);
		if ($row = mysql_fetch_array($result)) {
			return $row;
		}
	}
	else{
		return False;
	}
}

function getRandChar($length){
	$str = null;
	$strPol = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz";
	$max = strlen($strPol)-1;
	for($i=0;$i<$length;$i++){
		$str.=$strPol[rand(0,$max)];//rand($min,$max)生成介于min和max两个数之间的一个随机整数
	}
	return $str;
}

?>