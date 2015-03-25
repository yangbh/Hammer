<?php
require_once('common.php');

//  check login first
if (!already_login()) {
	error_jump();
}
?>
<?php
// var_dump($_POST);
$userid = get_userid();
$num = intval($_POST['num'])?$_POST['num']:1000;
$proxies = [];

$query = "SELECT IP_Addr,Port,Type,Address,Latency,Reliability FROM Proxy Limit $num";
// echo $query . '<br>';
$result = mysql_query($query);

while ($row = mysql_fetch_row($result)){
	$proxies[] = $row;
}
echo json_encode($proxies);
?>