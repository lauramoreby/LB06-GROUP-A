if (localStorage.getItem("passChange") == null) {
  localStorage.setItem("passChange", 'false');
}
if (localStorage.getItem("login") == null) {
  localStorage.setItem("login", 'false');
}
if (localStorage.getItem("logout") == null) {
  localStorage.setItem("logout", 'false');
}

if (localStorage.getItem("newacc") == null) {
  localStorage.setItem("newacc", 'false');
}

function onButton(code) {
      if (code == 13) {
          loseSearchFocus();
          search();
          
      }
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
  if (localStorage.getItem("newacc") == 'true') {
    Materialize.toast('Account created succesfully!', 4000, '');
    localStorage.setItem("newacc", 'false');
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
  alert("Hi");
}

function search() {
  // put the content into a hidden div
  $('#spinner-hidden').html("<br><br><div class = 'spinner'><div class=\"preloader-wrapper big active\"> <div class=\"spinner-layer spinner-green-only\"> <div class=\"circle-clipper left\"> <div class=\"circle\"><\/div> <\/div><div class=\"gap-patch\"> <div class=\"circle\"><\/div> <\/div><div class=\"circle-clipper right\"> <div class=\"circle\"><\/div> <\/div> <\/div> <\/div></div>");
  var query = document.getElementById("clubSearch").value;
  // get the target height
  var url = "http://127.0.0.1:8000/healthapple/healthapplesearchapi/?q=";
  // animate height and set content
  var data = Get(url + query);
  var obj = JSON.parse(data);
  var results = "";
  for (var item in obj){
    var temp = "";
    temp += "<div class = 'title'>" + obj[item]['title'] + "<a href='save_page'><i class='material-icons right float-icon'>add</i></a> </div><br>";
    temp += "<div class = 'title2'>" + obj[item]['summary'] + "</div>";
    temp += "<div class = 'title2'>Flesch score: " + obj[item]['flesch_score'] + "</div>";
    temp += "<div class = 'title2'>Polarity score: " + obj[item]['polarity_score'] + "</div>";
    temp += "<div class = 'title2'>Subjectivity score: " + obj[item]['subjectivity_score'] + "</div>";
    temp += "Source: " + obj[item]['source'] + "<br>";
    temp += "<a class='waves-effect waves btn-flat right blue-text' href=" + String(obj[item]['link']) + ">Visit Page</a><br>";
  //  temp += "<a href=" + obj[item]['link'] + "class='waves-effect waves btn-flat right'>Visit Page</a><br>";
    results += createCard(temp);
  }


  $('#dynamic-results').html(results);
  $('.result_card').hide().show(0);

}

function input () {
  //function will get called every time a user types something into the search box
  var word = document.getElementById("clubSearch").value;

//  $.getJSON( "http://suggestqueries.google.com/complete/search?client=firefox&q="+word, function( data ) {
//});
}

function Get(yourUrl) {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET",yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;
}
