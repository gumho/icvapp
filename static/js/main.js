var rowHeight = 26;

$(document).ready(function() {
	//option defaults
    $("#criteria_start, #criteria_end").datepicker({
		defaultDate: -5,
        maxDate: 0                
    });

	$("#criteria_start, #criteria_end").datepicker('setDate', new Date());
	
	//search submit handler
	$("#search_button").click(function() {
		var start = $('#criteria_end').val();
		var end = $('#criteria_end').val();
		var status = $("input['criteria_status']:checked").val();
		
		$.ajax({
			type: 'post',
			url: '/search',
			data: {
				'criteria_start' : start,
				'criteria_end' : end,
				'criteria_status' : status
			},
			success: function(data) {
				//append results to table
				alert(data);
			}
		});
		
		return false;
	});
	
	//result drop click handlers
	$("#results tr:not(:first)").toggle(function() {
		var topOffset = $(this).offset().top + rowHeight - 1;
		
		$("#result_drop").css({
			'top': topOffset + 'px'
			// 'display': 'block'
		});
		
		$("#result_drop").slideDown();
		$(this).css('background-color', '#eee');
	},
	function() {
		$("#result_drop").slideUp();
		$(this).css('background-color', '#fff');
	});
	
	$("#rd_close").click(function() {
		$("#result_drop").slideUp();
		return false;
	});

})