<?php
  require_once "../templates/headers/userIndex.html";

      function operation(){
        if(isset($_POST['old'])) {
          echo '<input type="submit" id="input" class="input clickable" name="view" value="View List" />';
        } else if(isset($_POST['create'])){
          echo '<input type="submit" id="input" class="input clickable" name="selectItems" value="Add Items" />';
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
        <form class="form form-index" action="chooseItems.php" method="post"><div id="heading" class="sub-heading">
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
