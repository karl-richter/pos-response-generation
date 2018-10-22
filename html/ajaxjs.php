<?php
// Fetching Values From URL
$timestamp = $_POST['timestamp'];
$ip = $_SERVER['REMOTE_ADDR'];
$pos = $_POST['pos'];
$ner = $_POST['ner'];
$selectedPOS = $_POST['selectedPOS'];
$description = $_POST['description'];
$connection = mysql_connect("mysql27.1blu.de", "s260795_2796303", "nVw9F)FnY0lqd@%"); // Establishing Connection with Server..
$db = mysql_select_db("db260795x2796303", $connection); // Selecting Database
$query = mysql_query("INSERT INTO `responses` (`timestamp`, `ip`, `pos`, `ner`, `selected_pos`, `question`) VALUES ('$timestamp', '$ip', '$pos', '$ner', '$selectedPOS', '$description')"); //Insert Query
mysql_close($connection); // Connection Closed
?>