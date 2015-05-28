<?php
require_once('common.php');
?>
<?php
//	check login first
if (!already_login()) {
	echo 'false';
	die();
}

$userId = $_SESSION['userID'];
$configName = check_sql(trim($_REQUEST['name']));
$configConfig = check_sql(trim($_REQUEST['config']));	# json type
$configAutoI = check_sql(trim($_REQUEST['autoi']));

$query = "SELECT ID FROM Config WHERE Name='$configName' AND User_ID = $userId";
// print '$query='.$query.'<br>';
$result = mysql_query($query);
if ($row = mysql_fetch_array($result)) {
	// echo $row;
	$configID = $row[0];
	$query = "UPDATE Config SET Config='$configConfig',name='$configName',autoi='$configAutoI' WHERE ID='$configID' AND User_ID = $userId";
}
// print '$query='.$query.'<br>';
$result = mysql_query($query);
if ($row = mysql_fetch_array($result)) {
	// echo $row;
}
echo 'true';
?>