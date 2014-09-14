<?php
require_once('common.php');
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Hammer</title>
    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="jumbotron.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="dashboard.css" rel="stylesheet">
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar">1</span>
            <span class="icon-bar">2</span>
            <span class="icon-bar">3</span>
          </button>
          <a class="navbar-brand" href="#">Hammer</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="index.php">Home</a></li>
            <?php if (already_login()) {echo '<li><a href="scans.php">Scans</a></li>';}?>
            <li><a href="plugins.php">Plugins</a></li>
            <li><a href="documents.php">Documents</a></li>
            <li class="active"><a href="about.php">About</a></li>
          </ul>
<?php
if (already_login()) {
echo <<<EOF
          <div class="navbar-form navbar-right" role="form">
            <span class="label label-default">welcome</span>
            <a href="logout.php" class="btn btn-warning">Sign out</a>
          </div>
EOF;
}
else{
echo <<<EOF
          <form class="navbar-form navbar-right" role="form" action="login.php" method="post">
            <div class="form-group">
              <input type="text" placeholder="Name" class="form-control" name="username" id="username">
            </div>
            <div class="form-group">
              <input type="password" placeholder="Password" class="form-control" name="password" id="password">
            </div>
            <button type="submit" class="btn btn-success">Sign in</button>
          </form>
EOF;
}
?>
        </div><!--/.navbar-collapse -->
      </div>
    </div>



    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
