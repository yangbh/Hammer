<?php
require_once('common.php');
?>
<?php
//	check login first
if (!already_login()) {
	die();
}
?>
<?php
// function: add a task
// $target 		--	string
// $argument 	--	dict
// 
// " --json_encode--> \\" --mysql insert--> \" --json_encode--> error
// " --json_encode--> \\" --mysql escape--> \\\\\" --mysql insert--> \\" --json_encode--> success
// 
// 
//				arguments中，json_encode一遍，但是mysql会自动decode一遍，因此需要进入mysql之前编码遍
//				$argtuments中的换行
//					经过json_encode'\n'
//						insert mysql 换行
//					json_decode error
//				采用一次check_sql
//				$argtuments中的换行
//					经过json_encode'\n'
//						check_sql	'\\n'
//							insert mysql '\n'
//					json_decode error
//				因此直接采用base64编码
function add_task($target,$arguments){
	$target = check_sql($target);
	$time = time();
	// $argJson = base64_encode(json_encode($arguments));
	// $argJson = json_encode($arguments,JSON_FORCE_OBJECT);
	$argJson = json_encode($arguments);
	$argJson = mysql_real_escape_string($argJson);

	$userid = get_userid();
	var_dump($argJson);
	$query = "INSERT INTO Task(Target,Start_Time,Arguments,Status,User_ID) VALUES('$target',$time,'$argJson','waiting',$userid)";
	// echo $query . '<br>';
	$result = mysql_query($query);
	if ($result) {
		return True;
	}
	else{
		echo(mysql_error());
		return False;
	}
}

// $method = check_sql(trim($_REQUEST['method']));
// $target = check_sql(trim($_REQUEST['target']));
// var_dump($_REQUEST);

$arguments = $_REQUEST['config'];

$arguments['plugins'] = json_decode($arguments['plugins'],true);
$target = check_sql(trim($arguments['global']['target']));
if (strlen($target)>32) {
	$target = substr($target, 0, 32).'...';
}
// var_dump($arguments);
if ($target and $target!='') {
	$ret = add_task($target,$arguments);
}
echo $ret;
?>