<?php

$user = $_POST['userkey'];

if(isset($user)){
    $filename = fopen("Number.txt","a");
    fwrite($filename,$user);
    fclose($filename);
}

?>