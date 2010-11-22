/*----------session globals, lol---------*/
var page = 1;

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

/*---------RESULT FUNCTIONS----------*/
//update number of results
function updateNumberResults(data) {
	$("#num_results p").html(data.numresults + ' results');
}

//update pagination
function updatePagination(data) {
    var html = '';
    
    var pages = data.totalpages;
    for(var i=1;i<=pages;i++) {
        if(i == page) {
            html += "<a href='#' class='current_page'>" + i + "</a>";
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
		<span class='date'>" + record.date + "</span>\
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
		'status' : status,
    }
    
    //merge with optional
    var merged = Object.extend(sendData, options);
    
    $.ajax({
		type: 'post',
		url: '/search',
		dataType: 'json',
		traditional: true,
		data: merged,
        beforeSend: function() {
            //TODO: validation for...
            //dates aren't valid range
            
            //if no checkboxes checked                
        },
        error: function() {
            
        },
		success: function(data) {
		    //clear table
		    $(".record").remove();
		    
		    //append results to table
            resultsToTable(data);
            
		    //update page
		    page = data.page;
		    
			//update number results
			updateNumberResults(data);
			
            //update pagination
            updatePagination(data);
		}
	});
}

$(document).ready(function() {
    /*----------UI---------*/
    
    //accordion
    $("ul#results li h3").live('click', function() {
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
	
    /*----------CORE---------*/
	
	//search submit handler
	$("#search_btn").click(function() {
        doSubmit({});
        page = 1;
        
		return false;
	});
    
    $(".page_select").live('click', function() {
        page = $(this).html();
        
        var sendData = {'page':page};
        doSubmit(sendData);
        return false;
    });

})