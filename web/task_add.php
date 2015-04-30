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
function add_task($target,$arguments){
	$target = check_sql($target);
	$time = time();
	$argJson = json_encode($arguments);
	$userid = get_userid();
	// echo $argJson;
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