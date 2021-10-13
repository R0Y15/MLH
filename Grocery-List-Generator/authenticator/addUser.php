<?php

  function signup($connection, $uname, $pass){
    $sql = "INSERT INTO `user`(`username`, `password`) VALUES ('$uname', '$pass')";
    if (!mysqli_query($connection, $sql)){
      die('Error: ' . mysqli_error($connection));
    }
    echo "Signed Up successfully";
  }

  function login($connection, $uname, $pass){
    $sql = "SELECT * FROM `user`";
    $result = $connection->query($sql);

    if (mysqli_query($connection, $sql)){
      if($result->num_rows > 0){
        while($row = $result->fetch_assoc()) {
          if($uname===$row['username'] && $pass===$row['password']){
            if ($uname=='admin') {
              header("Location: ../admin");
              exit();
            } else{
              header("Location: ../user");
              exit();
            }
          }
        }
        echo "Invalid Credentials!";
      } else {
          echo "No item yet!";
        }

    } else{
      die('Error: ' . mysqli_error($connection));
    }
  }

  $connection = mysqli_connect("localhost", "root", "");
  mysqli_select_db($connection, "households");
  $uname = $_POST['username'];
  $pass = $_POST['password'];

  if(isset($_POST['signup'])) {
    signup($connection, $uname, $pass);
  } else if(isset($_POST['login'])) {
    login($connection, $uname, $pass);
  } else {
        die("DENIED");
    }
?>
