
$(document).ready(function(){
	"use strict";

	var window_width 	 = $(window).width(),
	window_height 		 = window.innerHeight,
	header_height 		 = $(".default-header").height(),
	header_height_static = $(".site-header.static").outerHeight(),
	fitscreen 			 = window_height - header_height;


	$(".fullscreen").css("height", window_height)
	$(".fitscreen").css("height", fitscreen);

  //-------- Active Sticky Js ----------//
  $(".default-header").sticky({topSpacing:0});

     if(document.getElementById("default-select")){
          $('select').niceSelect();
    };

    $('.img-pop-up').magnificPopup({
        type: 'image',
        gallery:{
        enabled:true
        }
    });


  // $('.navbar-nav>li>a').on('click', function(){
  //     $('.navbar-collapse').collapse('hide');
  // });

  
  $("#explore-btn").click(function(){
    $("#carouselHomePage").carousel("next");
});

  $("#back-btn").click(function(){
    $("#carouselHomePage").carousel("prev");
});

  // Select all links with hashes
  $('.navbar-nav a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .on('click',function(event) {
  // On-page links
  if (
    location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
    && 
    location.hostname == this.hostname
  ) {
    // Figure out element to scroll to
    var target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
    // Does a scroll target exist?
    if (target.length) {
      // Only prevent default if animation is actually gonna happen
      event.preventDefault();
      $('html, body').animate({
        scrollTop: target.offset().top-50
      }, 1000, function() {
        // Callback after animation
        // Must change focus!
        var $target = $(target);
        $target.focus();
        if ($target.is(":focus")) { // Checking if the target was focused
          return false;
        } else {
          $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
          $target.focus(); // Set focus again
        };
      });
    }
  }
  });

  
 $(".skill1").each(function(){
	 var overseas = $(this).data("born-overseas");
	 $(this).DonutWidget({

      // these are default options
      max: 100, 
      value: overseas, 
      text: "", 
      rotate: 0, 
      caption: "", 
      template: [
        '<div class="donut-hole"><span class="donut-filling"></div>', 
        '<div class="donut-bite" data-segment-index="0"></div>', 
        '<div class="donut-bite" data-segment-index="1"></div>', 
        '<div class="donut-caption-wrapper"><span class="donut-caption"></span></div>'
      ].join(''), 
      colors: {
        primary: "#8490ff",
        background: "#eee"
      },
      size: "large"
      
    });
 });
  
  $(".skill2").each(function(){
	 var excepteng = $(this).data("except-eng");
	 $(this).DonutWidget({

      // these are default options
      max: 100, 
      value: excepteng, 
      text: "", 
      rotate: 0, 
      caption: "", 
      template: [
        '<div class="donut-hole"><span class="donut-filling"></div>', 
        '<div class="donut-bite" data-segment-index="0"></div>', 
        '<div class="donut-bite" data-segment-index="1"></div>', 
        '<div class="donut-caption-wrapper"><span class="donut-caption"></span></div>'
      ].join(''), 
      colors: {
        primary: "#8490ff",
        background: "#eee"
      },
      size: "large"
      
    });
 });

  $(".skill3").each(function(){
	 var speakyours = $(this).data("speak-yours");
	 $(this).DonutWidget({

      // these are default options
      max: 100, 
      value: speakyours, 
      text: speakyours + "%", 
      rotate: 0, 
      caption: "", 
      template: [
        '<div class="donut-hole"><span class="donut-filling"></div>', 
        '<div class="donut-bite" data-segment-index="0"></div>', 
        '<div class="donut-bite" data-segment-index="1"></div>', 
        '<div class="donut-caption-wrapper"><span class="donut-caption"></span></div>'
      ].join(''), 
      colors: {
        primary: "#8490ff",
        background: "#eee"
      },
      size: "large"
      
    });
 }); 
 
 $("#collapse-button").click(function(){
	   var textChange = $(this).text();
	   textChange = textChange == "Show More" ? "Show Less" : "Show More";
	   $(this).text(textChange);
 });

//    $("#to_compare").click(function(){
//    var c_str;
//    c_str = document.getElementById('commun_str').value
//
//    $.ajax(
//    {
//        type:"GET",
//        url: "/compare",
//        contentType: "application/json;charset=UTF-8",
//        data:{
//                 community_str: c_str
//        },
//
//     })
//});

$('[data-toggle="popover"]').popover({
  trigger: 'hover'
 });
 
var tabs = $('.tabs');
var items = $('.tabs').find('a').length;
var selector = $(".tabs").find(".selector");
var activeItem = tabs.find('.active');
var activeWidth = activeItem.innerWidth();
$(".selector").css({
  "left": activeItem.position.left + "px", 
  "width": activeWidth + "px"
});

$(".tabs").on("click","a",function(){
  $('.tabs a').removeClass("active");
  $(this).addClass('active');
  var activeWidth = $(this).innerWidth();
  var itemPos = $(this).position();
  $(".selector").css({
    "left":itemPos.left + "px", 
    "width": activeWidth + "px"
  });
});


var highest= $("#highest").data("percentage");
$(".progress-item").each(function(){
	var current = $(this).data("percentage");
	var newP = current/highest * 100;
	$(this).css("width", newP + "%");
})

});


  

