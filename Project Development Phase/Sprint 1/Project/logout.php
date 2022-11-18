<?php   
session_start();

session_unset();
session_destroy();
haeder("Location:index.php");