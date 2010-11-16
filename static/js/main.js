var rowHeight = 26;

//takes '11/8/2010' and turns into '2010-11-08'
function sqlDate(date) {
    return date.substr(6,10) + '-' + date.substr(0,2) + '-' + date.substr(3,2);
}

$(document).ready(function() {
	//option defaults
    $("#criteria_start, #criteria_end").datepicker({
		defaultDate: -5,
        maxDate: 0,

    });

	$("#criteria_start, #criteria_end").datepicker('setDate', new Date());
	
	//search submit handler
	$("#search_button").click(function() {
		var start = $('#criteria_start').val();
		var end = $('#criteria_end').val();
		var status = $("input['criteria_status']:checked").val();
		
		$.ajax({
			type: 'post',
			url: '/search',
			data: {
				'criteria_start' : sqlDate(start),
				'criteria_end' : sqlDate(end),
				'criteria_status' : status
			},
            beforeSend: function() {
                //TODO: validation
            },
			success: function(data) {
			    //clear table
			    
				//append results to table
				//$("#results").append(data);
			}
		});
		
		return false;
	});
	
	//result drop click handlers
	$("#results tr").live('click', function() {
		var topOffset = $(this).offset().top + rowHeight - 1;
		
		$("#result_drop").css({
			'top': topOffset + 'px'
			// 'display': 'block'
		});
		
		$("#result_drop").slideDown();
	}
    );
	
	$("#rd_close").click(function() {
		$("#result_drop").slideUp();
		return false;
	});

})