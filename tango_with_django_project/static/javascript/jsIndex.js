
function init() { // Runs when the page is first loaded
}

function createCard(content) {
    return "<div class = 'main_content_card result_card'><div class = 'inner_main_content_card'>" + content + "</div></div><br>"
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

function onSearchBoxInput() {
	document.getElementById("dynamic_results1").innerHTML += "";
	var result = [1,2,3,4,5,6,7,8,9,10];
	var text = "";
	for (i = 0; i < result.length; i++) { 
		text += createCard("Result " + result[i] + " Title<br><br>Description<br>Link");
	}
	document.getElementById("dynamic_results1").innerHTML += text;
}

var topBarShadow = {
    show: function() {
        $("#top_bar").css("box-shadow","0px -6px 6px 6px #000000");
    },
    hide: function() {
        $("#top_bar").css("box-shadow","");
    }
}
