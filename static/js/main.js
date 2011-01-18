/*----------session object---------*/

var session = {
    'page': 1,
    //sort tracking vars
    // asc=0, desc=1, unsorted=-1
    'date_sort': 1,
    'accession_sort': -1,
    'status_sort': -1
};

/*----------UTILS---------*/
//takes '11/8/2010' and turns into '2010-11-08'
function sqlDate(date) {
    return date.substr(6,10) + '-' + date.substr(0,2) + '-' + date.substr(3,2);
}

//gives hash merging functionality via extend(arr1,arr2)
Object.extend = function(destination, source) {
    for (var property in source)
        destination[property] = source[property];
    return destination;
};

//validate dates
function validateDates() {
	var bDate = $("#begin_date").val();
	var eDate = $("#end_date").val();
	
	//validate correct date syntax
	var datePattern = /\d{1,2}\/\d{1,2}\/\d{4}/;
	if(bDate.match(datePattern) != null && eDate.match(datePattern) != null) {
		return true;
	}
}

/*---------RESULT HELPER FUNCTIONS----------*/
//update number of results
function updateNumberResults(data) {
	$("#num_results p").html(data.numresults + ' results');
}

//update pagination
function updatePagination(data) {
    var html = '';
    
    var pages = data.totalpages;
    
    if(pages != 0) {
        html += 'Page ';
    }
    
    for(var i=1;i<=pages;i++) {
        if(i == session.page) {
            html += "<span class='current_page'>" + i + "</span>";
        } else {
            html += "<a href='#' class='page_select'>" + i + "</a>";            
        }
    }
    
    $('#pagination').html(html);
}

//generates html for inner accordion content
function createRowContent(pairs) {
    var html = '';
    var correct = [];
    var notcorrect = [];
    
    for(var i=0;i<pairs.length;i++) {
        var p = pairs[i];
        
        if(p.status == 'passed') {
            correct.push("<span>" + p.icd + " : " + p.cpt + "</span>")
        }
        
        if(p.status == 'failed') {
            notcorrect.push("<span>" + p.icd + " : " + p.cpt + "</span>")
        }        
	}
	
	html += "<p><strong>Correct (ICD:CPT)</strong><br>";
	for(var i in correct) {
	    html += correct[i] + '<br>';
	}
	
	html += "<br><strong>Not Correct (ICD:CPT)</strong><br>";
	for(var n in notcorrect) {
	    html += notcorrect[n] + '<br>';
	}
	
	html += "</p>";
	return html;
}

//return html for row
function createRow(record) {
	var row = "";
	
	row += "<li class='record'>\
	<h3>\
		<span class='date date_fold'>" + record.date + "</span>\
		<span class='time'>" + record.time + "</span>\
		<span class='accession'>" + record.accession + "</span>";
	
	if(record.status == 'passed') {
		row += "<span class='status-pass'>" + record.status + "</span>";
	} else {
		row += "<span class='status-fail'>" + record.status + "</span>";
	}
	row += "</h3>";
	
	row += createRowContent(record.codepairs);

	row +=  "</li>";
	
	return row;
}
//takes the returned data and sticks into results
function resultsToTable(data) {
    var results = data.records
    for(var i=0;i<results.length;i++) {
        $("ul#results").append(createRow(results[i]));
    }
}

/*----------AJAX---------*/
//submits the form, takes a hash of options
function doSubmit(options) {
    //get normal variables
    var start = $('#begin_date').val();
	var end = $('#end_date').val();
	var status = $('input:checked').map(function(i,n) {
        return $(n).val();
    }).get();
    
    var sendData = {
        'begin_date' : sqlDate(start),
		'end_date' : sqlDate(end),
		'status' : status
    }
    
    //merge with optional
    var merged = Object.extend(sendData, options);
    
    $.ajax({
		type: 'get',
		url: '/search',
		dataType: 'json',
		traditional: true,
		data: merged,
        beforeSend: function() {
            if(!validateDates()) {
				return false;
			}
        },
        error: function() {
            
        },
		success: function(data) {
		    //clear table
		    $(".record").remove();
		    
		    //append results to table
            resultsToTable(data);
            
		    //update page
		    session.page = data.page;
		    
			//update number results
			updateNumberResults(data);
			
            //update pagination
            updatePagination(data);
		}
	});
}

//sorting calls
function submitSort(sortColumn) {
    //check the columns current sort direction and reverse it
    var sortFlag = sortColumn + '_sort';

    var dir = '';

    if(session[sortFlag] == 0) {
        session[sortFlag] = 1;
        dir = 'desc';
    } 
    else if(session[sortFlag] == 1 || session[sortFlag] == -1) {
        session[sortFlag] = 0;
        dir = 'asc';
    }
    
    //reset the vars
    session.date_sort = -1;
    session.accession_sort = -1;
    session.status_sort = -1;
    
    if(dir == 'desc') {
        session[sortFlag] = 1;
    } else if(dir == 'asc') {
        session[sortFlag] = 0;
    }

    doSubmit({'sortby': sortColumn, 'sortdir': dir});
    
}


$(document).ready(function() {
    /*----------UI---------*/
    
    //accordion
    $("ul#results li:not(#result_header) h3").live('click', function() {
        $('span:first-child', this).toggleClass('date_fold date_unfold');
        $(this).next().toggle('slow'); 
    });
    
    //search button
    $("#search_btn").button();
    
    //more options
    $("#more_options_btn").toggle(function() {
       $(this).html('Fewer options'); 
    }, function() {
       $(this).html('More options');        
    });
    
	//datepicker defaults
    $("#begin_date, #end_date").datepicker({
		defaultDate: -5,
        maxDate: 0,
        showOn: "button",
		buttonImage: "/static/images/cal.png",
		buttonImageOnly: true
    }).keydown(function(event) {
        if(event.which === $.ui.keyCode.ENTER) {
            $('#search_btn').click();
        }
    });
    
    //set today's date
	$("#begin_date, #end_date").datepicker('setDate', new Date());
	
	//show search options
	$("#more_options_btn").click(function() {
	    $("#options").slideToggle();
	});
	
	//date + time integrated hover
	$("#date_header a, #time_header a").hover(function() {
		$("#date_header a, #time_header a").css('text-decoration', 'underline');
	}, function() {
		$("#date_header a, #time_header a").css('text-decoration', 'none');
	});
	
    /*----------CORE---------*/
	
	//search submit handler
	$("#search_btn").click(function() {
        doSubmit({});
        session.page = 1;
        
		return false;
	});
    
    $(".page_select").live('click', function() {
        session.page = $(this).html();
        
        var sendData = {'page':session.page};
        doSubmit(sendData);
        return false;
    });
    
    //result header click handler (sorting)
    $('#date_header a, #accession_header a, #status_header a').click(function() {
        submitSort($(this).html().toLowerCase());
    });
	$('#time_header a').click(function() {
		$('#date_header a').click();
	});

})