<?php
require_once('common.php');
?>
<?php
//	check login first
if (!already_login()) {
	die();
}

$pluginName = check_sql(trim($_REQUEST['name']));
$pluginAuthor = check_sql(trim($_REQUEST['author']));
$pluginType = check_sql(trim($_REQUEST['type']));
$pluginTime = check_sql(trim($_REQUEST['time']));
$pluginVersion = check_sql(trim($_REQUEST['version']));
$pluginWeb = check_sql(trim($_REQUEST['web']));
$pluginDescription = check_sql(trim($_REQUEST['description']));
$pluginCode = check_sql(trim($_REQUEST['code']));

$query = "INSERT INTO Plugin(Name,Type,Author,Time,Version,Web,Description,Code) VALUES('$pluginName','$pluginType','$pluginAuthor','$pluginTime','$pluginVersion','$pluginWeb','$pluginDescription','$pluginCode')";
print '$query='.$query.'<br>';
$result = mysql_query($query);
if ($row = mysql_fetch_array($result)) {
	// echo $row;
}

?>