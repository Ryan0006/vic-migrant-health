$(function() {
	var isoCountries = [];
	var placeholder = {id: '', text: 'Your country/region'};
	isoCountries.push(placeholder);
	var languageCSV = [];
	var textUnique = [];
	
	d3.csv("../../static/community/csv/country_codes.csv",function(data){
		data.forEach(function(d){
			var country = {
				id: d.Country,
				text: d.Country,
				code: d.Alpha2code
			}
			isoCountries.push(country);
		});
		
		$("[name='country']").select2({
		placeholder: "Your country/region",
		templateResult: formatCountry,
		templateSelection: formatCountry,
		data: isoCountries,
		allowClear: true
		});
		
		var selectedC = $('#selected-country').attr('data-country');
		if (selectedC !== undefined){
			$("[name='country']").val(selectedC);
			$("[name='country']").trigger('change');
			var ctext = $("[name='country']").select2('data')[0].text;

			$('#selected-country').attr('data-country-name', ctext);
		};
		
	});
	
	
	d3.csv("../../static/community/csv/languages1.csv",function(data){
		data.forEach(function(d) {
			var row = {id:d.id, text:d.text}
			textUnique.push(d);
		});		
		$("[name='language']").select2({
		tags: true,
		placeholder: "Your language",
		templateSelection: formatLanguage,
		templateResult: formatLanguage,
		data: textUnique,
		allowClear: true
		});
	});
	
	d3.csv("../../static/community/csv/language_per_country.csv",function(data){
		data.forEach(function(d) {
			var row = {id: d.Country,
			text: d.Language
			};
			languageCSV.push(row);
		});	
		var selectedC = $('#selected-country').attr('data-country');
		if (selectedC !== undefined){
			var selected = $("[name='country']").select2('data')[0];

			$("[name='country']").trigger({
				type: 'select2:select',
				params: {
					data: selected
				}
			});
		};
	});
	

	
	function formatCountry (country) {
	  if (!country.id) { return country.text; }
	  var $country = $(
	  '<div style="display:flex;align-items:center;">' +
		'<div class="flag flag-'+ country.code.toLowerCase() + '"></div>' +
		'<div class="flag-text" style="text-align: top;">'+ country.text+"</div>" +
	  '</div>'
	  );
	  return $country;
	};
	
	
	var currentCountry = "";
	
	$("[name='country']").on('select2:select', function (e) {
		currentCountry = e.params.data.text;
		var filteredList = [];
		languageCSV.forEach(function(d){
			if (currentCountry !== ""){
				if (d.id === currentCountry){
					var lang = {id: d.text, text: d.text};
					filteredList.push(lang);
				}
			}
		});
		$("[name='language'] option[value]").remove();
		$("[name='language']").select2({
			placeholder: "Your language",
			templateSelection: formatLanguage,
			templateResult: formatLanguage,
			data: filteredList,
			tags: true,
			allowClear: true,
			"language": {
				"noResults": function(){
					   return "No Results Found in Our Database (Try enter manually)";
				   }
			}
		});
		var selected = $('#selected-language').attr('data-language');
		var selectedC = $('#selected-country').attr('data-country-name');

		if (selectedC !== undefined){
			if (currentCountry === selectedC){
				if (selected !== undefined){

					$("[name='language']").val(selected);
					$("[name='language']").trigger('change');
				};			
			};			
		};

	});
	
	$("[name='country']").on('select2:unselect', function (e) {
		
		$("[name='language'] option[value]").remove();
		$("[name='language']").select2({
		tags: true,
		placeholder: "Your language",
		templateSelection: formatLanguage,
		templateResult: formatLanguage,
		data: textUnique,
		allowClear: true
		});
	});
	
		
	function formatLanguage (language) {

	  if (!language.id) { return language.text; }
	  var $language = $(
	  '<div class="row align-items-center" style="display:block;">' +
		'<span class="flag-text">'+ language.text+"</span>" +
	  '</div>'
	  );
	  return $language;
	};	
		
	});
