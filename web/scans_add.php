<?php
require_once('common.php');
?>

<?php
//	
function task_start(){

}

//
function task_end(){

}

function task_add($Url,$Time,$Arguments,$Level,$User_ID){

}

if (!already_login()) {
	die();
}

$type = check_sql(trim($_REQUEST['type']));
if ($type == 'start') {
	
}

?>