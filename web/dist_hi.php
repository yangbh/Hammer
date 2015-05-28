<?php
require_once('common.php');

//  check login first
if (!already_login()) {
	error_jump();
}
?>
<?php
$type = trim($_REQUEST['type']);
$userid = get_userid();
$time = time();
$ip = $_SERVER["REMOTE_ADDR"];

//	
if ($type=='start') {
	$os = check_sql(trim($_REQUEST['os']));
	$mac = check_sql(trim($_REQUEST['mac']));

	//
	//
	//	处理worker
	// check wether this worker already exists
	$query = "SELECT ID,Status,IP FROM Dispatcher WHERE OS='$os' AND MAC='$mac' AND User_ID='$userid'";
	// echo $query.'<br>';

	$result = mysql_query($query);
	$row = mysql_fetch_row($result);

	// if exists, update Last_Time, and if the status is offline, then change to online
	if ($row) {
		// echo 'dispatcher already exists';
		// var_dump($row);
		$dispatcherId = $row[0];
		$status = $row[1];
		$ipOld = $row[2];
		// echo $dispatcherId,$status,$ipOld;

		$query = "UPDATE Dispatcher set Last_Time='$time'";
		if (!$status) {
			$query .= ", Status=True";
		}
		if ($ip!=$ipOld) {
			$query .= ", IP='$ip'";
			// echo $query.'<br>';
		}
		$query .= " WHERE ID='$dispatcherId'";
		// echo $query.'<br>';
		$result = mysql_query($query);
		if ($result) {
			// echo 'update dispatcher success';
		}
		else{
			// echo 'update dispatcher falied';
		}
	}
	// else, insert a new dispatcher an
	else{
		$query = "INSERT INTO Dispatcher(OS,MAC,IP,Last_Time,User_ID,Status) VALUES('$os','$mac','$ip','$time','$userid',1)";
		// echo $query.'<br>';
		$result = mysql_query($query);
		if ($result) {
			// echo 'update dispatcher success';
		}
		else{
			// echo 'update dispatcher falied';
		}
		$query = "SELECT ID FROM Dispatcher WHERE OS='$os' AND MAC='$mac' AND IP='$ip' AND User_ID='$userid'";
		$result = mysql_query($query);
		$row = mysql_fetch_row($result);
		$dispatcherId = $row[0];
	}

	//
	//
	// 分配任务
	// 
	// Step1: get workers num and jobs num
	$query = "SELECT count(*) FROM Dispatcher WHERE Status=1";
	$result = mysql_query($query);
	$row = mysql_fetch_row($result);
	$workersNum = intval($row[0]);
	// echo '$workersNum='.$workersNum.'<br>';

	$query = "SELECT count(*) FROM Task WHERE Status='waiting'";
	$result = mysql_query($query);
	$row = mysql_fetch_row($result);
	$jobsNum = intval($row[0]);
	// echo '$jobsNum='.$jobsNum.'<br>';

	// Step2: count out the num and dispatch the job
	$limit = 0;
	if ($workersNum && $jobsNum) {
		// $limit = ($jobsNum%$workersNum)?intval($jobsNum/$workersNum)+1:intval($jobsNum/$workersNum);
		$limit = 1;
	}
	// echo '$limit='.$limit.'<br>';

	$ret = array('data' => array(),'code' => 1, 'info' => 'thanks, no task');
	//	
	if ($limit) {
		try {
			// echo 'in try'.'<br>';
			//	防止两个sql语句的运行时间空隙可造成并发混乱，加上mysql锁
			$query = "LOCK TABLE Task write";
			$result = mysql_query($query);

			$query = "SELECT ID,Target,Arguments FROM Task WHERE Status='waiting' LIMIT $limit";
			// echo $query.'<br>';
			
			$result = mysql_query($query);
			// die();
			while ($row = mysql_fetch_row($result)){
				// var_dump($row);
				
				// 更新每个task状态
				$taskid = $row[0];
				$ret['data']['targetname'] = $row[1];
				$ret['data']['taskid'] = $taskid;
				// 暂时设为others而不是running,待worker反馈接收到任务才置为running状态
				$sql = "UPDATE Task SET Status='running' ,Dispatcher_ID='$dispatcherId' WHERE ID='$taskid' AND Status='waiting'";
				// echo $sql.'<br>';
				mysql_query($sql);
				// var_dump($row[2]);
				// $arg = json_decode(base64_decode($row[2]));
				$arg = json_decode($row[2],true);
				// var_dump($arg);
				foreach ($arg as $key => $value){
					$ret['data'][$key] = $value;
				}
				// var_dump($ret);
			}
			$ret['info'] = 'dispatch ' . $limit . ' tasks';
			
		} catch (Exception $e) {
			$ret['code'] = 0;
			$ret['info'] = 'an error occured: '.$e->getMessage();
			// print $e->getMessage();
		}
		//	确保解除锁
		//	其实mysql的锁机制是进程锁定，如果该进程退出了，那么它在mysql上设置的锁自然就不存在了
		//	所有下面这两句不用也可
		$query = "UNLOCK TABLE";
		$result = mysql_query($query);
	}
	echo json_encode($ret);
}


//
elseif ($type=='end') {
	$taskid = check_sql(trim($_REQUEST['taskid']));
	$query = "UPDATE Task SET Status='done' WHERE ID='$taskid'";
	$result = mysql_query($query);
	if ($result) {
		echo 'ok, change task status to done';
	}
	else{
		echo 'something wrong';
	}
}

?>