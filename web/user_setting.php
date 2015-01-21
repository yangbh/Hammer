<?php
require_once('common.php');

//  check login first
if (!already_login()) {
	error_jump();
}
?>
<?php
$type = trim($_REQUEST['type']);
$username = $_SESSION['user'];
$ret = array('code' => 0, );
switch ($type) {
	case 'changepwd':
		$oldpwd = trim($_REQUEST['oldpwd']);
		$newpwd = trim($_REQUEST['newpwd']);

		$oldpwdhash = pwd_encode($username,$oldpwd);

		$query = "SELECT ID FROM User WHERE Name='$username' AND Password='$oldpwdhash'";
		$result = mysql_query($query);
		$row = mysql_fetch_row($result);
		// var_dump($row);
		if (count($row) && $id=intval($row[0])) {
			// echo '$id='.$id.'<br>';
			$newpwdhash = pwd_encode($username,$newpwd);
			$query = "UPDATE User SET Password= '$newpwdhash' WHERE ID = '$id'";
			$result = mysql_query($query);
			// var_dump($result);
			if ($result) {
				$ret['code'] = 1;
				$ret['info'] = 'change password success';
			}
			else{
				$ret['info'] = 'something wrong';
			}
		}
		else{
			$ret['info'] = 'password wrong';
		}
		break;
	
	case 'getinfo':
		$query = "SELECT ID FROM User WHERE Name='$username'";
		$result = mysql_query($query);
		$row = mysql_fetch_row($result);
		// var_dump($row);
		if (count($row) && $id=intval($row[0])) {
			$ret['code'] = 1;
			$ret['info'] = 'get user info success';
			$ret['data'] = array('name' => $username, 'id' => $id);
		}
		else{
			$ret['info'] = 'something wrong';
		}
		break;

	default:
		# code...
		break;
}
echo json_encode($ret);
?>