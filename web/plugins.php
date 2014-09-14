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
    <link rel="icon" href="images/favicon.ico">

    <title>Hammer</title>
    <!-- Custom styles for this template -->
    <link href="css/jumbotron.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="css/dashboard.css" rel="stylesheet">
    <!-- jquery -->
    <!-- <script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script> -->
    <script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script>

    <script>
    $(document).ready(function () {
      //  hide plugin_code div
      $('#code').hide('fast');
      //  snippet
      $("pre.python").snippet("python",{style:"vim",menu:false,showNum:true});

      //  plugin table
      $('#plugins_table').DataTable({
        // "ajax": "./datatable.json",
        "ajax": "./plugin_search.php",
        // "paging":   false,
        "lengthChange": false, //改变每页显示数据数量
        "pageLength": 10,
        // "info":     false,
        "filter":   false,
        // "ordering": false,
        "order":    [[ 2, "desc" ]],
        "columnDefs": [ {
          "targets": 0,
          "render": function ( data, type, full, meta ) {
            // return "<a class=\"plugin\" href='search.php?name="+encodeURI(data)+"'>"+data+"</a>";
            return "<a class=\"plugin\" href=#>"+data+"</a>";
          }
        } ]
      });

      //  <a> links in tables
      $('#plugins_table').DataTable().on('draw.dt', function () {
        $('.plugin').bind("click",function() {
          var name= $(this).text();
          $.get("plugin_search.php",{name: name},function(data){
            $('#plugins').hide('slow');
            $('#code').show('slow');
            $('#plugin_name').text(name);
            $('#plugin_code').text(data);
          });
        });
      });

      $('#plugin_goback').click(function(){
        $('#plugins').show('slow');
        $('#code').hide('slow');
      });

      //  search button click
      $('#search').click(function() {
        /* Act on the event */
        var ajax_url = "./plugin_search.php?type="+$('#type').val()+"&keyword="+$('#keyword').val();
        $('#plugins_table').DataTable().ajax.url(ajax_url).load();
      });

    });
    </script>
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
            <li class="active"><a href="plugins.php">Plugins</a></li>
            <li><a href="documents.php">Documents</a></li>
            <li><a href="about.php">About</a></li>
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
    <div class="container">
      <div class="row" id="plugins">
            <h2 class="page-header">Plugins</h2>
            <div class="form-inline">
              <div class="btn-group">
                <select class="form-control" name="type" id="type">
                  <option value="0">All Category</option>
                  <option value="1">Common</option>
                  <option value="2">Sensitive Info</option>
                  <option value="3">System</option>
                  <option value="4">Info Collect</option>
                  <option value="5">Web Applications</option>
                  <option value="6">Weak Password</option>
                  <option value="7">Others</option>
                </select>
              </div>
              <div class="form-group">
                <input type="text" class="form-control" id="keyword" placeholder="Keyword" name="keyword">
              </div>
              <button id="search" class="btn btn-default">Search</button>
            </div>
          <div class="table-responsive">
            <table id="plugins_table" class="table table-striped">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Author</th>
                        <th>Web</th>
                        <th>Description</th>
                    </tr>
                </thead>
            </table>
          </div>
      </div>
      <div class="row" id="code" hidden="true">
        <h1><a class="glyphicon glyphicon-circle-arrow-left" id="plugin_goback"></a>&nbsp;<small id="plugin_name"></small></h1>
        <pre class="python" id="plugin_code"></pre>
      </div>
    </div>

    <!-- ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <!-- snippet -->
    <link rel="stylesheet" type="text/css" href="js/jquery.snippet.min.css">
    <script type="text/javascript" charset="utf8" src="js/jquery.snippet.min.js"></script>

    <!-- Bootstrap core JavaScript -->
    <link href="js/bootstrap.min.css" rel="stylesheet">
    <script type="text/javascript" src="js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->


    <!-- DataTables -->
    <link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.2/css/jquery.dataTables.css">
    <script type="text/javascript" charset="utf8" src="http://cdn.datatables.net/1.10.2/js/jquery.dataTables.js"></script>

  </body>
</html>
