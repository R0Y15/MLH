<?php

    require_once "../templates/headers/adminIndex.html";

      $connection = mysqli_connect("localhost", "root", "");
      mysqli_select_db($connection, "households");
      $table = $_POST['shop'];

      ############################################

      function updater($connection, $table){
        $item = $_POST['item'];
        $unit = $_POST['unit'];
        $unitprc = $_POST['unitprc'];

        $sql = "INSERT INTO $table(`item`, `unit`, `unitPrice`) VALUES ('$item', '$unit', '$unitprc')";
        if (!mysqli_query($connection, $sql)){
          die('Error: ' . mysqli_error($connection));
        }
        echo "1 new item added to shop of ".$table;
        echo '<form class="form" action="menu.php" method="post">';
        echo '<span>';
          echo '<input type="submit" name="add" id="input" class="input clickable editable-input" value="Add More" />';
        echo '</span>';
        echo '<span>';
          echo '<button type="submit" name="back" id="input" class="input clickable editable-input" value="User Home">Admin Home</button>';
        echo '</span> <br />';
        echo '</form>';
      }

      function screen($connection, $table){
        $sql = "SELECT * FROM $table";
        $result = $connection->query($sql);
        $count = 0;

        if (mysqli_query($connection, $sql)){

          if ($result->num_rows <= 0) {
            echo '<br /><h4 class="center">No item yet!</h4>';
            goto back;
          }

          echo '<div class="center main-div">';
          echo '<table class="list-table">';
          echo '<h4>';
            echo '<tr>';
              echo '<th class="num">S.No.</th>';
              echo '<th>Item</th>';
              echo '<th>Unit</th>';
              echo '<th>Unit Price</th>';
            echo '</tr>';
          echo '</h4>';

          if($result->num_rows > 0){
            while($row = $result->fetch_assoc()) {

              echo '<tr>';
                echo '<td class="num">'.++$count.'</td>';
                echo '<td>'.$row["item"].'</td>';
                echo '<td>'.$row["unit"].'</td>';
                echo '<td>₹'.$row["unitPrice"].'</td>';
              echo '</tr>';
            }
          } else {
            echo '</table>';
          }

          back:
          echo '</div>';

        } else{
          die('Error: ' . mysqli_error($connection));
        }
      }

      function edit($connection, $table){
        $sql = "SELECT * FROM $table";
        $result = $connection->query($sql);

        if (mysqli_query($connection, $sql)){
          if($result->num_rows > 0){

            echo '<form class="form editable-form" action="" method="post">';
            echo '<h4><u>Details of new items:-</u></h4>';
            echo '<input type="hidden" name="shop" value="'.$table.'" />';

            while($row = $result->fetch_assoc()) {

                echo '<span>';
                  echo '<input type="text" id="" class="editable-input" name="item[]" value="'.$row["item"].'" />';
                echo '</span>';
                echo '<span>';
                  echo '<input type="text" id="" class="editable-input" name="unit[]" value="'.$row["unit"].'" />';
                echo '</span>';
                echo '<span>';
                  echo ' ₹<input type="text" id="" class="editable-input" name="unitprc[]" value="'.$row["unitPrice"].'" />';
                echo '</span> <br />';
              }
              echo '<input type="submit" name="updater" class="editable-input" value="Update" />';
              echo '<span>';
                echo '<button type="submit" name="back" class="editable-input" value="User Home">Admin Home</button>';
              echo '</span> <br />';
          echo '</form>';
          } else {
              echo "No item yet!";
            }

        } else{
          die('Error: ' . mysqli_error($connection));
        }
        echo "<br /><br />Ends: ".$table;
      }

      function update($connection, $table){

        delete($connection, $table);

        $x = $_POST['item'];
        $u = $_POST['unit'];
        $up = $_POST['unitprc'];

        $s = sizeof($x);

        for ($i=0; $i < $s; $i++) {
          $sql = "INSERT INTO $table(`item`, `unit`, `unitPrice`) VALUES ('$x[$i]', '$u[$i]', '$up[$i]')";
          if (!mysqli_query($connection, $sql)){
            die('Error: ' . mysqli_error($connection));
          }
        }
        header("Location: index.php");
      }

      function delete($connection, $table){
        $sql = "SELECT * FROM $table";
        $result = $connection->query($sql);

        if (mysqli_query($connection, $sql)){
          if($result->num_rows > 0){
            $del = "DELETE FROM $table LIMIT $result->num_rows";
            mysqli_query($connection, $del);
            } else {
              echo "No item yet!";
            }

        } else{
          die('Error: ' . mysqli_error($connection));
        }
      }
      #########################




      if(isset($_POST['add'])) {
        add($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['view'])){
        disp($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['eview'])){
        editableView($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['delete'])){
        delete($connection, $table);
        mysqli_close($connection);
      } else if(isset($_POST['update'])) {
        update($connection, $table);
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
