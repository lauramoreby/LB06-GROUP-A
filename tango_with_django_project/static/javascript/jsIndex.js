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

if (localStorage.getItem("savedpage") == null) {
  localStorage.setItem("savedpage", 'false');
}

if (localStorage.getItem("category") == null) {
  localStorage.setItem("category", 'false');
}


var search_param = "";
var api_source = "";
var latest_query = "";
var latest_result = null;

function onButton(code) {
      if (code == 13) {
          loseSearchFocus();
          search();
          
      }
}

function type_fun(search_type) {
  search_param = search_type;
}

function apiSelector(api) {
  api_source = api;
  if (latest_query != "") {
    Materialize.toast('Results updated', 2000, '');
    get_and_show_results(latest_result);
  }
  else {
    Materialize.toast('Source updated', 2000, '');
  }
}

function notificationDisplay(test) {
  if (window.location.href.slice(-11) == '/save_page/') {
    $('#id_url').val(localStorage.getItem("link"));
    if (localStorage.getItem("savedpage") == 'true') {
      window.history.pushState('Home', 'Healthapple', '/healthapple/');
    }
  }
  if (window.location.href.slice(-14) == '/add_category/') {
    $('#id_url').val(localStorage.getItem("category"));
    if (localStorage.getItem("add_category") == 'true') {
      window.history.pushState('Home', 'Healthapple', '/healthapple/');
    }
  }
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
  if (localStorage.getItem("savedpage") == 'true') {
    Materialize.toast('Page saved succefully!', 4000, '');
    localStorage.setItem("savedpage", 'false');
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

function save_page(link) {
  localStorage.setItem("link", link);
  window.location.href = 'save_page';
}

function search() {
  $('#dynamic-results').html("");
  // put the content into a hidden div
  $('#spinner-hidden').show();
  var query = document.getElementById("clubSearch").value;
  latest_query = query;
  var url = "/healthapple/healthapplesearchapi/?q=";
  Get(url + query + search_param);
}

function get_and_show_results(result){
  latest_result = result;
  var obj = JSON.parse(result);
  var results = "";
  $('#spinner-hidden').hide();
  for (var item in obj){
    if (api_source == 'bing' && obj[item]['source'] == 'HealthFinder') {
      continue;
    }
    if (api_source == 'health' && obj[item]['source'] == 'Bing') {
      continue;
    }
    var temp = "";
    temp += "<div class = 'title'>" + obj[item]['title'] + "<a href='javascript:save_page(\"" + obj[item]['link'] + "\")'><i class='material-icons right float-icon'>add</i></a> </div><br>";
    temp += "<div class = 'title2'>" + obj[item]['summary'].replace(/<(?:.|\n)*?>/gm, '') + "</div>"; 
    temp += "<br><div class = 'title2'><a href=\"javascript:openModal('#flesch-modal')\"><i class=\"material-icons scores\">info_outline</i></a> Flesch Score: " + obj[item]['flesch_score'] + "</div>";
    temp += "<div class = 'title2'><a href=\"javascript:openModal('#polarity-modal')\"><i class=\"material-icons scores\">info_outline</i></a> Polarity Score: " + obj[item]['polarity_score'] + "</div>";
    temp += "<div class = 'title2'><a href=\"javascript:openModal('#subjectivity-modal')\"><i class=\"material-icons scores\">info_outline</i></a> Subjectivity Score: " + obj[item]['subjectivity_score'] + "</div>";
    temp += "<br>Source: " + obj[item]['source'] + "<br>";
    temp += "<a class='waves-effect waves btn-flat right blue-text' href=" + String(obj[item]['link']) + ">Visit Page</a><br>";
    results += createCard(temp);
  }
  if (results == ""){results = createCard("No results found, try changing the query or API source")};
  $('#dynamic-results').html(results);
  $('.result_card').hide().show(0);
}

function testing() {
  alert("hello");
}


function input () {
  //function will get called every time a user types something into the search box
  var word = document.getElementById("clubSearch").value;

//  $.getJSON( "http://suggestqueries.google.com/complete/search?client=firefox&q="+word, function( data ) {
//});
}

function Get(yourUrl) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      get_and_show_results(xhttp.responseText);
    }
  };
  xhttp.open("GET", yourUrl, true);
  xhttp.send();
}

function openModal(id) {
  $(id).openModal();
}
