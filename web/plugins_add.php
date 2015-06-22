<?php
require_once('common.php');
?>
<?php
//	check login first
if (!already_login()) {
	echo 'false';
	die();
}
//
//	josn 入库之前必须escape
//

// 第一步：更新plugin表
$pluginName = check_sql(trim($_REQUEST['name']));
$pluginFile = check_sql(trim($_REQUEST['file']));
$pluginAuthor = check_sql(trim($_REQUEST['author']));
$pluginType = check_sql(trim($_REQUEST['type']));
$pluginTime = check_sql(trim($_REQUEST['time']));
$pluginVersion = check_sql(trim($_REQUEST['version']));
$pluginWeb = check_sql(trim($_REQUEST['web']));
$pluginDescription = check_sql(trim($_REQUEST['description']));
$pluginCode = check_sql(trim($_REQUEST['code']));
$pluginOpts_unescape = trim($_REQUEST['opts']);
$pluginOpts = check_sql($pluginOpts_unescape);

$query = "SELECT ID FROM Plugin WHERE Name='$pluginName'";
// print '$query='.$query.'<br>';
$result = mysql_query($query);
if ($row = mysql_fetch_array($result)) {
	// echo $row;
	$pluginID = $row[0];
	$query = "UPDATE Plugin SET File='$pluginFile',Type='$pluginType',Author='$pluginAuthor',Time='$pluginTime',Version='$pluginVersion',Web='$pluginWeb',Description='$pluginDescription',Code='$pluginCode',Opts='$pluginOpts' WHERE ID='$pluginID'";
}
else{
	$query = "INSERT INTO Plugin(Name,File,Type,Author,Time,Version,Web,Description,Code,Opts) VALUES('$pluginName','$pluginFile','$pluginType','$pluginAuthor','$pluginTime','$pluginVersion','$pluginWeb','$pluginDescription','$pluginCode','$pluginOpts')";
}
// print '$query='.$query.'<br>';
$result = mysql_query($query);
if ($row = mysql_fetch_array($result)) {
	// echo $row;
	echo 'true';
}
else{
	echo 'false';
}

// 第二步：更新config表
// 
// 插件类型与序号对照表
//	json_encode 的一个坑
//	
//	http://stackoverflow.com/questions/8595627/best-way-to-create-an-empty-object-in-json-with-php
//	The documentation specifies that (object) null will result in an empty object, some might therefor say that your code is valid and that it's the method to use.
//	PHP: Objects - Manual
//	If a value of any other type is converted to an object, 
//	a new instance of the stdClass built-in class is created. 
//	if the value was NULL, the new instance will be empty.
$PLUGIN_ID = array();
$PLUGIN_ID['Common'] = 0;
$PLUGIN_ID['Info_Collect'] = 1;
$PLUGIN_ID['Sensitive_Info'] = 2;
$PLUGIN_ID['System'] = 3;
$PLUGIN_ID['Weak_Password'] = 4;
$PLUGIN_ID['Web_Applications'] = 5;
$PLUGIN_ID['Others'] = 6;
// var_dump($PLUGIN_ID);
$userid = get_userid();
$query = "SELECT ID,Config,AutoI FROM Config WHERE User_ID='$userid'";
// print '$query='.$query.'<br>';
$result = mysql_query($query);
while ($row = mysql_fetch_row($result)) {
	// var_dump($row);
	$id = $row[0];
	$autoi = explode('|', $row[2]);
	// var_dump($autoi);
	// print $pluginType;
	$i = $PLUGIN_ID[$pluginType];
	// print '$i='.$i;
	if($autoi[$i]){
		$config = json_decode($row[1],true);
		// $config = array($config);
		$opt = json_decode($pluginOpts_unescape,true);
		// var_dump($opt);
		$config[$pluginType][$pluginFile] = $opt;
		// var_dump($config);
		// $config_json = json_encode($config,JSON_FORCE_OBJECT);
		$config_json = json_encode($config);
		// print $config_json;
		$config_json = check_sql($config_json);
		# insert into config
		$query = "UPDATE Config SET Config='$config_json' WHERE ID='$id'";
		print '$query='.$query.'<br>';
		$result2 = mysql_query($query);
		if ($row2 = mysql_fetch_array($result2)) {
			// echo $row;
		}
	}
}

?>