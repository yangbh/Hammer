<?php
require_once('common.php');

function get_code($id=0,$name=''){
	$pID = intval($id);
	$pName = check_sql($name);
	$query = "SELECT ID,Name,Type,Author,Time,Version,Web,Description,Code FROM Plugin";
	if (is_int($pID) and $pID>0) {
		$query .= " WHERE ID=$pID";
	}
	elseif($pName !='') {
		$query .= " WHERE Name=$pName";
	}

	// print($query.'<br>');
	// $ret = array('data' => array(), );
	$result = mysql_query($query);
	if ($row = mysql_fetch_row($result)) {
		foreach ($row as $key => $value){
			// echo $key.' => '.$value;
			$row[$key] = check_xss($value);
		}
		$ret['data'][] = $row;
		return $ret;
	}
}
$name = check_sql(trim($_REQUEST['name']));
$id = check_sql(trim($_REQUEST['id']));
// echo '$id='.$id.'<br>';
$data = get_code($id,$name);
echo json_encode($data);

?>