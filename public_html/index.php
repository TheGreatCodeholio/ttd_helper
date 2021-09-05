<?php
    /**
     * Index.php for TTD Helper
     * @license      Apache License v2.0
     * @author       Smashedbotatos <ian@icarey.net>
     * @copyright    Copyright © 2009-2021 iCarey Computer Services.
     *
     */
    error_reporting(E_ALL);
    ini_set('display_errors', 1);

    $config = parse_ini_file('includes/config.ini.php', 1, true);
    require_once 'classes/basic.php';
?>

    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset="utf-8">
        <title>TTD Helper Recent Calls</title>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,300i,400,400i,500,500i,700,700i" rel="stylesheet">
        <!-- Icon Fonts -->
        <script defer src="js/all.min.js"></script>
        <!-- Custom CSS -->
        <link rel="stylesheet" href="css/ttd_helper.css">
        <!-- Favicon Configuration -->
        <link rel="apple-touch-icon" sizes="180x180" href="img/icon/apple-touch-icon.png">
        <link rel="icon" type="image/png" sizes="32x32" href="img/icon/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="img/icon/favicon-16x16.png">
        <link rel="manifest" href="img/icon/site.webmanifest">
        <link rel="mask-icon" href="img/icon/safari-pinned-tab.svg" color="#c50000">
        <link rel="shortcut icon" href="img/icon/favicon.ico">
        <meta name="apple-mobile-web-app-title" content="BC Fire">
        <meta name="application-name" content="BC Fire">
        <meta name="msapplication-TileColor" content="#525252">
        <meta name="msapplication-config" content="img/icon/browserconfig.xml">
        <meta name="theme-color" content="#ffffff">
        <!-- JavaScript
        <script src="js/icarey.js"></script> -->
    </head>
    <body>
    <div class="container"> <!-- Main Container -->
    <div class="row">
      <div class="col-12">
          <h3 class="align-content-center pagetitle">Today's Calls</h3>
          <hr />
          <?php
          $database = new DatabaseConnect($config['mysql']['host'], $config['mysql']['user'], $config['mysql']['password'], $config['mysql']['database'], $config['mysql']['port']);
          $resultcalls = $database->query("SELECT * FROM ttd_calls WHERE call_time >=  CURDATE() ORDER BY call_time DESC");
          $timezone = "";
          if (is_link("/etc/localtime")) {
              $filename = readlink("/etc/localtime");
              $pos = strpos($filename, "zoneinfo");
              if ($pos) {
                  $timezone = substr($filename, $pos + strlen("zoneinfo/"));
              } else {
                  $timezone = $default;
              }
          } else {
              $timezone = file_get_contents("/etc/timezone");
              if (!strlen($timezone)) {
                  $timezone = $default;
                  }
          }
          date_default_timezone_set($timezone);

          if ($database->num_rows($resultcalls) == 0) {
              echo '<div class="alert alert-danger" role="alert">No Recent Calls</div>';
          } else {
              while ($row = $database->fetch($resultcalls)) {
                  $id = $row['call_id'];
                  $call_department = $row['call_tone_name'];
                  $call_mp3 = $row['call_mp3_url'];
                  $call_time = $row['call_time'];

                  echo '<div class="row mb-0 well well-bcfire">';
                  echo '<div class="col"> <h6 style="color: #c24c4c">' . $call_department . '</h6></div></div>';
                  echo '<div class="row mb-2 ml-2">';
                  echo '<div class="col">' . $call_time . '</div>';
                  echo '<audio controls>';
                  echo '<source src="' . $call_mp3 . '" type="audio/mpeg">';
                  echo 'Your browser does not support the audio element.';
                  echo '</audio>';
                  echo '</div>';
              }
          }

          ?>


        <div class="container footer">
            <div class="row">
                <a class="icarey-orange-text mt-4 mb-4 ml-4" href="https://www.icarey.net">&nbsp;iCarey Computer Services &copy;2009-<?php echo date('Y');?></a>
            </div>
        </div>
      </div>
      </div>
    </div> <!-- Main Container Close -->
<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="js/jquery-3.3.1.slim.min.js"></script>
<script src="js/popper.js"></script>
<script src="js/bootstrap.min.js"> </script>
</body>
</html>
