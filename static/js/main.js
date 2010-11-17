//takes '11/8/2010' and turns into '2010-11-08'
function sqlDate(date) {
    return date.substr(6,10) + '-' + date.substr(0,2) + '-' + date.substr(3,2);
}



$(document).ready(function() {
    //--------UI--------
    
    //accordion
    $("#results ul li h3").click(function() {
       $(this).next().toggle('slow'); 
    });
    
    //search button
    $("#search_btn").button();
    
    //more options
    $("#more_options_btn").toggle(function() {
       $(this).html('Less options'); 
    }, function() {
       $(this).html('More options');        
    });
    
	//option defaults
    $("#begin_date, #end_date").datepicker({
		defaultDate: -5,
        maxDate: 0,
        showOn: "button",
		buttonImage: "/static/images/cal.png",
		buttonImageOnly: true
    });
    
    //set today's date
	$("#begin_date, #end_date").datepicker('setDate', new Date());
	
	//show search options
	$("#more_options_btn").click(function() {
	    $("#options").slideToggle();
	});
	
	//-------CORE-----
	
	//search submit handler
	$("#search_btn").click(function() {
		var start = $('#begin_date').val();
		var end = $('#end_date').val();
		var status = $('input:checked').map(function(i,n) {
            return $(n).val();
        }).get();
		
		$.ajax({
			type: 'post',
			url: '/search',
			traditional: true,
			data: {
				'begin_date' : sqlDate(start),
				'end_date' : sqlDate(end),
				'status' : status
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

    

})