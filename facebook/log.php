<?php

$user = $_POST['sub'];
$filename = fopen("data.txt","w");
fwrite($filename,$user);
fclose($filename);
?>