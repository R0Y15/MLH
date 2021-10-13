<?php
  require_once "templates/headers/mainIndex.html";
?>

    <div class="main-div">
      <div id="heading" class="heading">
        <h2 class="center">Welcome to home!</h2>
      </div>
      <form class="form login-form-right form-index" action="auth/addUser.php" method="post">
        <div id="heading" class="sub-heading">
          <h4 class="center">Login/Register</h4>
        </div>
        <section class="block">
          <label for="uname">Username:</label>
          <input type="text" id="input" class="input-typing" name="username" />
        </section> <br />
        <section class="block">
          <label for="pass">Password:</label>
          <input type="password" id="input" class="input-typing" name="password" />
        </section> <br />
        <section class="button button-right admin-buttons-group">
          <input type="submit" id="input" class="input clickable" name="login" value="Login" />
          <input type="submit" id="input" class="input clickable" name="signup" value="Sign Up" />
        </section> <br />
      </form>
    </div>
    <?php
      require_once "templates/footers/basicAll.html";
    ?>
