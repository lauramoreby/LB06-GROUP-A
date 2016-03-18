if (localStorage.getItem("passChange") == null) {
  localStorage.setItem("passChange", 'false');
}
if (localStorage.getItem("login") == null) {
  localStorage.setItem("login", 'false');
}
if (localStorage.getItem("logout") == null) {
  localStorage.setItem("logout", 'false');
}

function notificationDisplay() {
  if (localStorage.getItem("passChange") == 'true') {
    Materialize.toast('Password changed succesfully!', 4000, '');
    localStorage.setItem("passChange", 'false');
  }
  if (localStorage.getItem("login") == 'true') {
    Materialize.toast('You are now logged in!', 4000, 'left');
    localStorage.setItem("login", 'false');
  }
  if (localStorage.getItem("logout") == 'true') {
    Materialize.toast('You are now logged out!', 4000, '');
    localStorage.setItem("logout", 'false');
  }
}

function notificationEnabler(type) {
  localStorage.setItem(type, 'true');
}

function createCard(content) {
  return "<div class = 'main_content_card result_card'><div class = 'inner_main_content_card'>" + content + "</div></div><br>";
}

function toTop() { // Scrolls to top of page
  $('html, body').animate({ scrollTop: 0 }, 'fast');
}

function onScroll() {
  loseSearchFocus();
  if ($("body").scrollTop() != 0) {topBarShadow.show();}
  else {topBarShadow.hide();}
}

function loseSearchFocus() {
  $("#clubSearch").blur();
}

function getSearchFocus() { // Scrolls to top of page, resets search box value and gives it focus
  anim = Promise.resolve($('html, body').animate({ scrollTop: 0 }, 'fast').promise());
  Promise.all([anim]).then(function () {
      $("#clubSearch").val('');
      $("#clubSearch").focus();
  });
}

var topBarShadow = {
  show: function() {
      $("#top_bar").css("box-shadow","0px -6px 6px 6px #000000");
  },
  hide: function() {
      $("#top_bar").css("box-shadow","");
  }
};

function passChange() {
	$('.error').fadeIn(400).delay(3000).fadeOut(400); //fade out after 3 seconds
}