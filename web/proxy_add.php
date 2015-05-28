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
$proxies = $_POST['proxies'];
// var_dump($proxies);
$proxies = json_decode($proxies,true);
// var_dump($proxies);
$success = 0;
$fail = 0;

foreach ($proxies as $key => $proxy) {
	$port =intval($proxy[1]);	
	if ($proxy[3]) {
		$type = 'https';
	}
	else{
		$type = 'http';
	}
	$latency = intval($proxy[5]);
	$reliablity = intval($proxy[6]);

	$query = "INSERT INTO Proxy(IP_Addr,Port,Type,Address,Latency,Reliability) VALUES('$proxy[0]',$port,'$type','$proxy[4]',$latency,$reliablity)";
	// echo $query . '<br>';
	$result = mysql_query($query);
	if ($result) {
		// echo 'True<br>';
		$success +=1;
	}
	else{
		// echo 'False<br>';
		$fail +=1;
	}
}
echo "success insert $success pieces proxies";
echo "fail insert $fail pieces proxies";
?>