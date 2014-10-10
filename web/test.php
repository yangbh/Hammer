<?php
require_once('common.php');


$query = "SELECT Level FROM Vuln WHERE  Scan_ID=20007";
echo $query . '<br>';
$result = mysql_query($query);
if ($row = mysql_fetch_array($result)) {
	echo 'yes';
}
else{
	die();
}
?>