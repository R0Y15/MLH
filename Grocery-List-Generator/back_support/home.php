<?php
  require_once "../templates/headers/adminIndex.html";

      function home(){
        if(isset($_POST['add'])) {
          echo "<hr />";
          echo '<span>';
            echo '<label for="item">Item: </label>';
            echo '<input type="text" id="item" class="editable-input" name="item" value="" />';
          echo '</span> <br />';
          echo '<span>';
            echo '<label for="unit">Unit: </label>';
            echo '<input type="text" id="unit" class="editable-input" name="unit" value="" />';
          echo '</span> <br />';
          echo '<span>';
            echo '<label for="unotPrice">Unit Price: ₹</label>';
            echo '<input type="text" id="unotPrice" class="editable-input" name="unitprc" value="" />';
          echo '</span> <br />';
            echo '</br><input type="submit" class="editable-input" name="add" value="Add New Item" />';
        } else if(isset($_POST['view'])){
          echo '<input type="submit" name="view" value="View List" />';
        } else if(isset($_POST['update'])){
            echo '<input type="submit" id="input" class="input clickable" name="eview" value="Editable View" />';
        } else if(isset($_POST['back'])) {
          header("Location: index.php");
        } else {
              die("DENIED");
          }
      }

    ?>


    <div class="main-div">
      <div id="heading" class="heading">
        <h2 class="center">Select a Shop</h2>
      </div>
      <div class="database center">
        <form class="form form-index" action="listUpdate.php" method="post"><div id="heading" class="sub-heading">
          <h4 class="center">Available currently:</h4>
        </div>
        <div class="shops">
        <section class="block">
          <input id="1" type="radio" name="shop" value="store1" checked="checked" />
          <label for="1">Store1</label>
        </section> <br />
        <section class="block">
          <input id="2" type="radio" name="shop" value="store2" />
          <label for="2">Store2</label>
        </section> <br />
        <section class="block">
          <input id="3" type="radio" name="shop" value="others" />
          <label for="3">Other Stores</label> <br />
        </section> <br />
        </div>

          <section class="button-center">
            <?= operation(); ?>
            <input type="submit" id="input" class="input clickable" name="back" value="Back" />
            <!--<input type="submit" name="delete" value="Delete" />-->
          </section> <br />
        </form>
      </div>
    </div>

<?php
  require_once "../templates/footers/basicAll.html";
?>
