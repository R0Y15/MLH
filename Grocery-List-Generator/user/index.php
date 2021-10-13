<?php
  require_once "../templates/headers/userIndex.html";
?>


    <div class="index">
      <div id="heading" class="heading">
        <h2 class="center">Welcome User!</h2>
      </div>
      <form class="form form-index" action="menu.php" method="post">
        <div id="heading" class="sub-heading">
          <h4 class="center">Choose</h4>
        </div>
        <section class="button-center">
          <input type="submit" id="input" class="input clickable" name="old" value="Previous Lists" />
          <input type="submit" id="input" class="input clickable" name="create" value="Create New List" />
        </section> <br />
      </form>
    </div>
<?php
  require_once "../templates/footers/basicAll.html";
?>
