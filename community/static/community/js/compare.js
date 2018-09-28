$(function(){
	var compareBtn = document.getElementById("compare-btn");
	var goCompare = document.getElementById("goCompare-btn");
	var hasOpen = false;
	if (compareBtn !== null){
		$("#compare-btn").click(function(){
			if (hasOpen === false){
				$(".compare-item").each(function(){
					$(this).attr("style","display: inline-block");
					
				});
				$("#compare-btn").text("Cancel");
				$("#goCompare-btn").attr("style","display: inline");
				$("#compare-div").attr("class","col col-md-6");
				$("#gocompare-div").attr("class","col col-md-6");
				hasOpen = true;
				$("#compareHintModal").modal("show");
				$(".suburb-btn").each(function(){
					$(this).attr("class","btn primary-btn2 suburb-btn my-2 my-sm-0 isDisabled");
				});
			}
			else{
				$(".compare-item").each(function(){
					$(this).attr("style","display: none");
					
				});
				$("#compare-btn").text("Compare Suburbs");
				$("#goCompare-btn").attr("style","display: none");
				$("#compare-div").attr("class","col col-md-12");
				$("#gocompare-div").attr("class","col col-md-12");
				hasOpen = false;
				$(".suburb-btn").each(function(){
					$(this).attr("class","btn primary-btn2 suburb-btn my-2 my-sm-0");
				});
			}
			
		var $checkboxes = $('#suburb-area input[type="checkbox"]');
        
		$checkboxes.change(function(){
			var countCheckedCheckboxes = $checkboxes.filter(':checked').length;
			$('#goCompare-btn').text("Go Compare (" + countCheckedCheckboxes + "/4)");
			if (countCheckedCheckboxes <=1){
				$('#goCompare-btn').attr("disabled","disabled");
			}
			else {
				$('#goCompare-btn').removeAttr("disabled");
			}
			if (countCheckedCheckboxes >= 4){
				$('#suburb-area input[type="checkbox"]:not(:checked)').attr("disabled", "disabled");
			}
			else {
				$('#suburb-area input[type="checkbox"]').removeAttr("disabled");
			}
			// $('#edit-count-checked-checkboxes').val(countCheckedCheckboxes);
		});
			
		});
	};
// DIRTY Responsive pricing table JS

$( "ul" ).on( "click", "li", function() {
  var pos = $(this).index()+2;
  $("tr").find('td:not(:eq(0))').hide();
  $('td:nth-child('+pos+')').css('display','table-cell');
  $("tr").find('th:not(:eq(0))').hide();
  $('li').removeClass('active');
  $(this).addClass('active');
});

var number = $("#compare-num").data("number");
console.log(number);
if (number !== undefined){
	if (number === 4){
		$('.stat').attr("colspan",3)
	}
	if (number === 3){
		$('.stat').attr("colspan",4)
	}
	if (number === 2){
		$('.stat').attr("colspan",6)
	}
};

// Initialize the media query
  var mediaQuery = window.matchMedia('(min-width: 640px)');
  
  // Add a listen event
  mediaQuery.addListener(doSomething);
  
  // Function to do something with the media query
  function doSomething(mediaQuery) {    
    if (mediaQuery.matches) {
      $('.sep').attr('colspan',13);
    } else {
      $('.sep').attr('colspan',2);
    }
  }
  
  // On load
  doSomething(mediaQuery);	

});