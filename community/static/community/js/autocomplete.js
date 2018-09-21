var availableValues = [];
$( function() {

	var availableSuburbs = [];
	
	d3.csv("../../static/community/csv/autoSuburbs.csv",function(data){
		data.forEach(function(d){
			var row = {label: d.Label, value: d.Label};
			var value = d.Label;
			availableSuburbs.push(row);
			availableValues.push(value);
		});
		var input = document.getElementById("top-search");
		if (input !== null){
			var awesomplete = new Awesomplete(input);
			// new Awesomplete(input, {list: availableSuburbs});
			awesomplete.list = availableSuburbs;
		}
	});
	

});
function validateForm() {
		var nameField = $('#top-search').val();
		console.log(nameField);

		if ($.inArray(nameField, availableValues) === -1){
			alert("Please select a suburb from dropdowns");
			return false;
		}
		return true;
};
