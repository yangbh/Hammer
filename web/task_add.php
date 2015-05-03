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
	$argJson = base64_encode(json_encode($arguments));
	// $argJson = check_sql($argJson);
	$userid = get_userid();
	// var_dump($argJson);
	$query = "INSERT INTO Task(Target,Start_Time,Arguments,Status,User_ID) VALUES('$target',$time,'$argJson','waiting',$userid)";
	// echo $query . '<br>';
	$result = mysql_query($query);
	if ($result) {
		return True;
	}
	else{
		return False;
	}
}

// $method = check_sql(trim($_REQUEST['method']));
// $target = check_sql(trim($_REQUEST['target']));
// var_dump($_REQUEST);

$arguments = $_REQUEST['config'];
$target = check_sql(trim($arguments['global']['target']));
// var_dump($arguments);
if ($target and $target!='') {
	$ret = add_task($target,$arguments);
}
echo $ret;
?>