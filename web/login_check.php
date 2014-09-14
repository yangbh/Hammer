<?php
require_once('common.php');

function login_check($username,$password){
	global $con,$DB_SALT;
	$Pwd = strrev($username).'#'. $DB_SALT .'#'.strrev($password);	
	$Pwd = md5($Pwd);
	$query = "SELECT * FROM USER WHERE NAME='" . $username . "' AND Password='". $Pwd . "'";
	#print '$query= '. $query . '<br>';
	$result = mysql_query($query);
	if ($row = mysql_fetch_array($result)) {
		$_SESSION['user'] = $logininfo['Name'];
		$_SESSION['isadmin'] = $logininfo['Is_Admin'];
		$arr = array('result'=>'True','username'=>$_SESSION['user'],'is_admin'=>$_SESSION['isadmin']);
		return json_encode($arr);
	}
	$arr = array('result'=>'False','errorinfo'=>'UserName or Password Wrong!');
	return json_encode($arr);
}
?>
<?php
// check session first
if(already_login()){
	$arr = array('result'=>'True','username'=>$_SESSION['user'],'is_admin'=>$_SESSION['isadmin']);
	echo json_encode($arr);
}

$user = check_sql(trim($_POST['username']));
$pwd = check_sql(trim($_POST['password']));
echo login_check($user,$pwd);
?>