<!DOCTYPE html>

<html>

<head>
    
    <title>  LOGIN</title>

    <link rel="stylesheet" type="text/css" href="style.css">

</head>

<body>

     <form action="login.php" method="post">
    <h2> TEAM ID : PNT2022TMID37162 </h2>
    <h2> SMART WASTE MANAGEMENT SYSTEM FOR METROPOLITAN CITIES </h2>
        
     <h2>ADMIN LOGIN</h2>

        <?php if (isset($_GET['error'])) { ?>

            <p class="error"><?php echo $_GET['error']; ?></p>

        <?php } ?>

        <label>User Name</label>

        <input type="text" name="uname" placeholder="User Name"><br>

        <label>Password</label>

        <input type="password" name="password" onclick="location.website='https://node-red-aomre-2022-11-11.mybluemix.net/red/#flow/e6fd724dad5f7f7e';" placeholder="Password"><br> 

        <button type="submit">Login</button>

     </form>

</body>

</html>