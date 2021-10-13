<?php
  require_once "../templates/headers/adminIndex.html";
?>

    <div class="main-div">
      <div id="heading" class="heading">
        <h2 class="center">Welcome Admin!</h2>
      </div>
      <form class="form form-index menu" action="menu.php" method="post">
        <div id="heading" class="sub-heading">
          <h4 class="center">Choose</h4>
        </div>
        <section class="button-center">
          <input type="submit" id="input" class="input clickable" name="update" id="input" class="input clickable" value="Update a Table" />
          <input type="submit" id="input" class="input clickable" name="add" id="input" class="input clickable" value="Add Items" />
          <input type="submit" id="input" class="input clickable" name="view" id="input" class="input clickable" value="Display table" />
        </section> <br />
      </form>
    </div>

<?php
  require_once "../templates/footers/basicAll.html";
?>
