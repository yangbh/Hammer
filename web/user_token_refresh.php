<?php
require_once('common.php');

//  check login first
if (!already_login()) {
	error_jump();
}
?>
<?
$username = $_SESSION['user'];
$token = getRandChar(32);
// echo '$token='.$token.'<br>';
$query = "UPDATE User SET Token = '$token'  WHERE Name='$username'";
// echo '$query='.$query.'<br>';
$result = mysql_query($query);
if ($row = mysql_fetch_array($result)) {
	// echo 'True';
}
?>
<script>document.location.href='user.php';</script>