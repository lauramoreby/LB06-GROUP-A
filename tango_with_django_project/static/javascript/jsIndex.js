// Sets localally cross-page persistant variables for toast notification system

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

if (localStorage.getItem("add_category") == null) {
  localStorage.setItem("add_category", 'false');
}


var search_param = ""; // Search paramater modifier (treatment, medicine...etc)
var api_source = ""; // API filter variable
var latest_query = "";
var latest_result = null;
var selected_category = null;

function onButton(code) { // Searches and loses search focus to hide keyboard on mobile when the enter key is pressed 
      if (code == 13) {
          loseSearchFocus();
          search();
      }
}

function type_fun(search_type) { // Search paramater modifier function 
  search_param = search_type;
}

function apiSelector(api) { // API filter system
  api_source = api;
  if (latest_query != "") {
    get_and_show_results(latest_result); // Redraws results
  }
}

function catSel(cat_name) {
  selected_category = cat_name; // Temp stores selected category
}


function notificationDisplay() { // Main notification and URL redirect + fix system executed on every page load
  if (window.location.href.slice(-11) == '/save_page/') {
    $('#id_url').val(localStorage.getItem("link"));
    if (localStorage.getItem("savedpage") == 'true') {
      window.history.pushState('Home', 'Healthapple', '/healthapple/');
      localStorage.setItem("savedpage", 'false');
      Materialize.toast('Page saved succefully!', 4000, '');
      localStorage.setItem("savedpage", 'false');
    }
  }
  if (window.location.href.slice(-14) == '/add_category/') {
    if (localStorage.getItem("add_category") == 'true') {
      window.location.href = '/healthapple/save_page/';
      $('#id_url').val(localStorage.getItem("link"));
      localStorage.setItem("add_category", 'false');
    }
  }
  if (window.location.href.slice(-12) == 'healthapple/') {
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
}

function notificationEnabler(type) { // Sets the local variable for the type passed to true for the notification system
  localStorage.setItem(type, 'true');
}

function createCard(content) { // Content wrapper helper
  return "<div class = 'main_content_card result_card'><div class = 'inner_main_content_card'>" + content + "</div></div><br>";
}

function toTop() { // Scrolls to top of page // Animates to top of the page
  $('html, body').animate({ scrollTop: 0 }, 'fast');
}

function onScroll() { // Top (App bar) shadow handler
  loseSearchFocus();
  if ($("body").scrollTop() != 0) {topBarShadow.show();}
  else {topBarShadow.hide();}
}

function loseSearchFocus() { // Loses search bar focus (hides keyboard on mobile)
  $("#clubSearch").blur();
}

function getSearchFocus() { // Scrolls to top of page, resets search box value and gives it focus
  anim = Promise.resolve($('html, body').animate({ scrollTop: 0 }, 'fast').promise());
  Promise.all([anim]).then(function () {
      $("#clubSearch").val('');
      $("#clubSearch").focus();
  });
}

var topBarShadow = { // Top (App bar) shadow variable
  show: function() {
      $("#top_bar").css("box-shadow","0px -6px 6px 6px #000000");
  },
  hide: function() {
      $("#top_bar").css("box-shadow","");
  }
};

function save_page(link) { // Saving pages redirector
  localStorage.setItem("link", link);
  window.location.href = 'save_page';
}

function search() { // Displays spinner and sends API request
  $('#dynamic-results').html("");
  $('#spinner-hidden').show();
  var query = document.getElementById("clubSearch").value;
  latest_query = query;
  var url = "/healthapple/healthapplesearchapi/?q=";
  Get(url + query + search_param);
}

function get_and_show_results(result) { // Result generator, takes in results from main API
  latest_result = result;
  var obj = JSON.parse(result);
  var results = "";
  $('#spinner-hidden').hide();
  for (var item in obj){
    if (api_source == 'bing' && obj[item]['source'] == 'HealthFinder') { // API filtering system
      continue;
    }
    if (api_source == 'health' && obj[item]['source'] == 'Bing') { // API filtering system
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

function input () { // Beginnings of an autocorrect / complete system, more within view.py
  var word = document.getElementById("clubSearch").value;
}

function Get(yourUrl) { // Main API Request handler, callsback result generator
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      get_and_show_results(xhttp.responseText);
    }
  };
  xhttp.open("GET", yourUrl, true);
  xhttp.send();
}

function openModal(id) { // Opens given 'Modal' pop up dialog
  $(id).openModal();
}
