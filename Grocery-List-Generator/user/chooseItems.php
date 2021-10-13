<?php

  require_once "../templates/headers/userConditional.html";

      $connection = mysqli_connect("localhost", "root", "");
      mysqli_select_db($connection, "households");
      $table = $_POST['shop'];

      ############################################

      function getTUsr($t){
        if($t == 'store1'){
          return 'usrStore1';
        } else if($t == 'store2'){
          return 'usrStore2';
        } else if($t == 'others'){
          return 'userOthers';
        }
      }

      function disp($connection, $table){
        $sql = "SELECT * FROM $table";
        $result = $connection->query($sql);
        $bill = 0;
        $count = 0;

        if (mysqli_query($connection, $sql)){

          if ($result->num_rows <= 0) {
            echo '<br /><h4 class="center">No item yet!</h4>';
            goto back;
          }

          echo '<table border="solid" class="list-table">';
          echo '<h4>';
            echo '<tr>';
              echo '<th class="num">S.No.</th>';
              echo '<th>Item</th>';
              echo '<th>Qty</th>';
              echo '<th>Cost</th>';
            echo '</tr>';
          echo '</h4>';

          if($result->num_rows > 0){
            while($row = $result->fetch_assoc()) {
              $bill += $row["cost"];

              echo '<tr>';
                echo '<td class="num">'.++$count.'</td>';
                echo '<td>'.$row["item"].'</td>';
                echo '<td>'.$row["qty"].'(<em>'.$row["unit"].'</em>)'.'</td>';
                echo '<td>₹'.$row["cost"].'</td>';
              echo '</tr>';
            }
          } else {
            echo '</table>';
          }

          echo '<h4 class="center">Your bill: <span id="bill">₹'.$bill.'</span></h4>';

          back:

        } else{
            die('Error: ' . mysqli_error($connection));
          }
      }

      function makeList($connection, $table){
        $tableUser = getTUsr($table);
        $sql = "SELECT * FROM $table";
        $result = $connection->query($sql);
        $boxNum = 0;

        if (mysqli_query($connection, $sql)){
          echo '<form class="form" action="" method="post">';
          if($result->num_rows > 0){
            echo '<h4><u>Select Items:-</u></h4>';
            echo '<input type="hidden" name="shop" value="'.$tableUser.'" />';
            echo '<input type="hidden" name="shopToRead" value="'.$table.'" />';

            while($row = $result->fetch_assoc()) {
              echo '<input id="box'.$boxNum.'" type="checkbox" name="selectedId[]" value="'.$row["id"].'"> <label for="box'.$boxNum++.'">'.$row["item"].'</label></input><br/>';
              $boxNum += 1;
            }

            echo '<section class="button button-right buttons-group">';
              echo '<input type="submit" id="input" class="input clickable" name="getQty" value="Proceed" />';
            echo '</section> <br />';

          echo '</form>';
          } else {
              echo '<br /><h4 class="center">No item to get from here!</h4>';
            echo '</form>';
            }

        } else{
          die('Error: ' . mysqli_error($connection));
        }
      }

      function getQty($connection, $table){
        $tableRead = $_POST['shopToRead'];

        if(!empty($_POST['selectedId'])){

          $rowIds = $_POST['selectedId'];
          $s = sizeof($rowIds);
          echo '<table class="list-table">';

          echo '<form class="form" action="" method="post">';
          echo '<h4 class="center"><u>Enter qty for following:-</u></h4>';
          echo '<input type="hidden" name="shop" value="'.$table.'" />';
          for ($i=0; $i < $s; $i++) {
            $read= "SELECT * FROM $tableRead WHERE `id` = $rowIds[$i]";
            $result = $connection->query($read);

            if (mysqli_query($connection, $read)){
              if($result->num_rows > 0){
                while($row = $result->fetch_assoc()) {

                  echo '<tr>';
                    echo '<td>'.$row["item"].'</td>';
                    echo '<td>'.'<input type="text" name="qty[]" value="" placeholder="Quantity" />'.'</td>';
                    echo '<td>₹'.$row["unitPrice"].'( per <em>'.$row["unit"].'</em> )'.'</td>';
                  echo '</tr>';

                    echo '<input type="hidden" name="item[]" value="'.$row["item"].'" />';
                    echo '<input type="hidden" name="unit[]" value="'.$row["unit"].'" />';
                    echo '<input type="hidden" name="cost[]" value="'.$row["unitPrice"].'" />';
                }
              }
            }
          }
          echo '<tr>';
            echo '<td colspan="3">'.'<input type="submit" name="final" value="Final List" />'.'</td>';
          echo '</tr>';
        echo '</form>';
        } else {
          echo 'Nothing selected!';
        }
        echo '</table>';
      }

      function finalList($connection, $table){

        delete($connection, $table);

        $it = $_POST['item'];
        $qty = $_POST['qty'];
        $unit = $_POST['unit'];
        $price = $_POST['cost'];


        $s = sizeof($it);
        for ($i=0; $i < $s; $i++) {
          $rate = $price[$i] * $qty[$i];
          $sql = "INSERT INTO $table(`item`, `qty`, `unit`, `cost`) VALUES ('$it[$i]', '$qty[$i]', '$unit[$i]', '$rate')";
          if (!mysqli_query($connection, $sql)){
            die('Error: ' . mysqli_error($connection));
          }
        }
        disp($connection, $table);
      }

      function delete($connection, $table){
        $sql = "SELECT * FROM $table";
        $result = $connection->query($sql);

        if (mysqli_query($connection, $sql)){
          if($result->num_rows > 0){
            $del = "DELETE FROM $table LIMIT $result->num_rows";
            mysqli_query($connection, $del);
            } else {
              #echo "No item yet!";
            }

        } else{
          die('Error: ' . mysqli_error($connection));
        }
      }

      ############################################


      if(isset($_POST['selectItems'])) {
        makeList($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['view'])) {
        $table = getTUsr($table);
        disp($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['getQty'])) {
        getQty($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['final'])) {
        finalList($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['back'])) {
        header("Location: index.php");
      } else {
            die("DENIED");
        }
?>
<?php
  require_once "../templates/footers/basicAll.html";
?>
