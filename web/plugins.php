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
            <?php if (already_login()) {echo '<li><a href="scan.php">Scans</a></li>';}?>
            <li><a href="about.php">About</a></li>
            <li><a href="documents.php">Documents</a></li>
            <li class="active"><a href="plugins.php">Plugins</a></li>
            <li><a href="contact.php">Contact</a></li>
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

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li class="active"><a href="#">Overview</a></li>
            <li><a href="#">Reports</a></li>
            <li><a href="#">Analytics</a></li>
            <li><a href="#">Export</a></li>
          </ul>
        </div>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
            <h1 class="page-header">Plugins</h1>
            <form class="form-inline" role="form">
                <div class="btn-group">
                    <select class="form-control">
                        <option value="-1">All Category</option>
                        <option value="2">Common</option>
                        <option value="3">Sensitive Info</option>
                        <option value="4">System</option>
                        <option value="5">Info Collect</option>
                        <option value="6">Web Applications</option>
                        <option value="1">Weak Password</option>
                        <option value="7">Others</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="text" class="form-control" id="exampleInputPassword2" placeholder="Keyword">
                </div>
                <button type="submit" class="btn btn-default">Search</button>
            </form>

          <div class="table-responsive">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1,001</td>
                  <td>Lorem</td>
                  <td>ipsum</td>
                  <td>dolor</td>
                  <td>sit</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
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
