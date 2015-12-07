
$(function(ready){
    $('#query-param-selection-source').on("selectmenuchange",function (ev, ui) {
        var option = $(this).find('option:selected').text();
        $('#query-param-data-source').html(option.toUpperCase());
    });

    $('#query-param-selection-municipality').on("selectmenuchange",function (ev, ui) {
        var option = $(this).find('option:selected').text();
        $('#query-param-municipality').html(option.toUpperCase());
    });

    $('#query-param-selection-year').on("selectmenuchange",function (ev, ui) {
        var option = $(this).find('option:selected').text();
        $('#query-param-year').html(option.toUpperCase());
    });

    $( ".advancedCondition" ).click(function() {
        if($(".advanced").hasClass("hidden")) {
            $(".advanced").removeClass("hidden");
            addAdvancedFilterRow();
        }
    });

    defaultSearchResult();

});

function defaultSearchResult(){
    //TODO: get filters in URL parameters, if they exist.

    var query = {
        "tipPodataka": [
            "rashodi",
            "prihodi"
        ],
        "godine": [
            2015
        ],
        "opstine": [],
        "klasifikacija": {
            "broj": [],
            "pocinjeSa": ""
        },
        "filteri": {}
    };

    // TODO: don't hardcode URL. But Can't use Jinja2 function.
    fethData(query);

}

function applyFilters(){

    // Get basic filter parameters
    var year = parseInt($('#query-param-selection-year').find(":selected").text());
    var municipality = $('#query-param-selection-municipality').find(":selected").val();

    // Prepare filter object
    var query = {
        "tipPodataka": [
            "rashodi",
            "prihodi"
        ],
        "godine": [
            year
        ],
        "opstine": [municipality],
        "klasifikacija": {
            "broj": [],
            "pocinjeSa": ""
        },
        "filteri": {
            "ukupno": {},
            "sopstveniPrihodi": {},
            "prihodiBudzeta": {},
            "donacije": {},
            "ostali": {}
        }
    };


    // Get advanced filter parameters
    $('#advanced-filter-container').children('div').each(function () {
        var currentBudgetItem = undefined;
        var currentOperand = undefined;
        var currentValue = undefined;

        $(this).children('div').each(function () {
            if($(this).hasClass('advanced-filter-selection-budget-item')){
                currentBudgetItem = $(this).children().find(":selected").val();

            }else if($(this).hasClass('advanced-filter-selection-operand')){
                currentOperand = $(this).children().find(":selected").val();

            }else if($(this).hasClass('advanced-filter-selection-value')){
                currentValue = $(this).children().val();
                query['filteri'][currentBudgetItem][currentOperand] = parseInt(currentValue);
            }
        });
    });

    fethData(query);
}

function fethData(query){
    $.ajax({
        type: "POST",
        url: SEARCH_REQUEST_SUM_URL,
        contentType: 'application/json',
        data: JSON.stringify(query),
        success: function(rsp){
            // TODO: Build result table here.
            console.log(rsp);
        }
    });
}


function addAdvancedFilterRow(){
    var filterRow = '<div class="advanced-filter-row">' +
        '<div class="advanced-filter-selection-budget-item col-xs-12 col-sm-3">' +
            '<select class="form-control border-primary search-control">' +
                '<option selected disabled>Budget Item</option>' +
                '<option value="ukupno">Ukupno</option>' +
                '<option value="sopstveniPrihodi">Sopstveni Prihodi</option>' +
                '<option value="prihodiBudzeta">Prihodi Budzeta</option>' +
                '<option value="donacije">Donacije</option>' +
                '<option value="ostali">Ostali</option>' +
            '</select>' +
        '</div>' +
        '<div class="advanced-filter-selection-operand col-xs-12 col-sm-3">' +
            '<select class="form-control border-primary search-control">' +
                '<option selected disabled>Operand</option>' +
                '<option value="veceIliJednako"> is >= </option>' +
                '<option value="manjeIliJednako"> is <= </option>' +
            '</select>' +
        '</div>' +
        '<div class="advanced-filter-selection-value col-xs-12 col-sm-3">' +
            '<input type="text" class="form-control border-primary search-control"/>' +
        '</div>' +
        '<div class="col-xs-2 col-sm-1 text-center">' +
            '<button type="button"  class="form-control border-primary pull-left" style="width: 50%;" onClick="javascript:applyFilters()">&#x2713;</button>' +
            '<button type="button"  class="removeCondition form-control border-secondary pull-left" style="width: 50%;" onClick="javascript:removeAdvancedFilterRow(this)">&#x2715;</button>' +
        '</div>' +
        '<div class="col-xs-4 col-sm-2 pull-right">' +
            '<button type="button" class="addCondition form-control border-primary button-full" onClick="javascript:addAdvancedFilterRow()">Add</button>' +
        '</div>' +
        '<br><br>' +
    '</div>';

    $('#advanced-filter-container').append(filterRow);
}

function removeAdvancedFilterRow(row){
    $(row).closest(".advanced-filter-row").remove();
}

var params = {
        "tipPodataka": ["rashodi", "prihodi"],
        "klasifikacijaBroj": [
            710000,
            712000,
            713000,
            730000,
            733000,
            410000,
            422000,
            460000,
            450000
        ],
        opstine:[]
    }

var params1 =
{
    "tipPodataka": [
        "rashodi",
        "prihodi"
    ],
    "godine": [
        2015,
        2014
    ],
    "opstine": [
        "prijepolje",
        "valjevo",
        "vranje",
        "zvezdara"
    ],
    "klasifikacija": {
        "broj": [

        ],
        "pocinjeSa": ""
    },
    "filteri": {
        "ostali": {

        }
    }
}

	function searchApiCall (argument) {

	    var result1, result2;
	    $.when(

	        $.ajax({
	            method: "POST",
	            url: "../api/prosek",
	            data: JSON.stringify(params),
	            contentType: "application/json;charset=utf-8",
	            dataType: "json",
	            success: function(returnhtml){
	                result1 = returnhtml;
	            }

	        })
	        ,
	        $.ajax({
	            method: "POST",
	            url: "../api/zbir",
	            data: JSON.stringify(params1),
	            contentType: "application/json;charset=utf-8",
	            dataType: "json",
	            success: function(returnhtml){
	                result2 = returnhtml;
	            }

	        })

	    ).then(function() {

	        mainVis(result2);
	        sideVis(result2, result1)
	        //visu(result1, result2)
	    });

    }

/**
  $(function(){

    //append to searchLink
    //if there is alredy that item , put new template to searchLink

    inputOption("dataItem") ;
    inputOption("muncipalityItem");
    inputOption("yearItem");
    inputOption("budgetItem[]");
    inputOption("operatorItem[]");
    inputOption("amountItem[]");

    function inputOption (selector) {
        $("[name='" + selector + "']").on("selectmenuchange",function (ev,ui) {

        var itemName = selector.split("Item")[0];
        var $label = $("#"+itemName+"Label");

        var labelText = $label.html();

        if( labelText.length == 0 || (selector =="dataItem" || selector =="muncipalityItem"))
            $label.html(ui.item.label)
        else {
          var opciono =
              ' <span id="budgetLabel"></span> that <span id="operatorLabel"></span> <span id="amountLabel"></span> ';

          $("#searchLink").append( opciono );
        }

      })
    }


  	$(document).on('click', ".advancedCondition",function(ev){

  		$(".advanced").removeClass("hidden");
  		$(".optionalFieldSet.form-group:first").removeClass("hidden");

  	})

  	$(document).on('click', ".addCondition",function(ev){

  		$(this).parents().filter(".optionalFieldSet").next().removeClass("hidden");



  	})

  	$(document).on('click', ".removeCondition",function(ev){

  		$(this).parents().filter(".optionalFieldSet").addClass("hidden");
		//reset to default
		//if

  	})


  	$("#searchLink").click(function (argument) {
  		var $podaci = $("#searchForm").serialize();

      alert($podaci);

  		searchApiCall( $podaci );
  	})


  })
*/
/*===========================
=            vis            =
===========================*/

//mainVis

function mainVis(data) {


	var opstina = "Zvezdara";
	var kontoBroj = 611;

	data = data.filter(function(la){
		return la.opstina == opstina;
		}).map(function(po){
			po.y =po.ukupno;
			po.name = po.klasifikacijaBroj;
			if(+po.klasifikacijaBroj == kontoBroj)
				{
					po.sliced = true;
					po.selected = true;
				}
			return po;
		})



	var $containerMain = $('#mainVis'),
        chart
       /* origChartWidth = 400,
        origChartHeight = 200,
        chartWidth = origChartWidth,
        chartHeight = origChartHeight*/;

        // Build the chart
        $containerMain.highcharts({
            chart: {
            	backgroundColor: "#7DC1D1",
    			/*width: chartWidth,
            	height: chartHeight,*/
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            title: {
                text: 'Prikaz '+" budžeta opštine " + opstina
            },
            legend:{
            	title:{
            		// text:'Nekakav tekst'
            	},
            	tooltip:"nekakav tekst"

            },
            tooltip: {
            	headerFormat:'<span style="font-size: 10px">Konto: {point.key}</span><br/>',
                pointFormat: ' {series.name}: <b>{point.y} din</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
            series: [{
                name: 'Iznos',
                colorByPoint: true,
                data: data
            }]
        });


}





function sideVis(arg1, arg2) {
	// 2-3 contos with max value + selected one

	// zasad random conta

	var data = [];
	var kategorije = [] ;

	console.log(arg1);

	arg1.filter(function(la){
		return +la.klasifikacijaBroj == 611
		})
		.forEach(function(po){
			var tempOb = {};
			tempOb.data = [ 0.8 * po.ukupno, Math.floor(Math.random()  * po.ukupno), po.ukupno];
			tempOb.name = po.opstina;

			data.push(tempOb);
			kategorije.push(po.opstina)
		})


	/*var data = [{
            name: 'Zvezdara',
            data: [7.0, 6.9, 9.5]
        }, {
            name: 'Novi Beograd',
            data: [-0.2, 0.8, 5.7]
        }, {
            name: 'Zrenjanin',
            data: [-0.9, 0.6, 3.5]
        }];*/


	var $container = $('#sideVisTop'),
        chart,
        origChartWidth = 400,
        origChartHeight = 200,
        chartWidth = origChartWidth,
        chartHeight = origChartHeight;

    $container.highcharts({
    	chart:{
    		backgroundColor: "#7DC1D1",
    		width: chartWidth,
            height: chartHeight
    		},
    	colors:["red","yellow","brown"],
       /* title: {
            text: 'Monthly Average Temperature',
            x: -20 //center
        },*/
       /* subtitle: {
            text: 'Source: WorldClimate.com',
            x: -20
        },*/
        xAxis: {
            categories: ['2013', '2014', '2015']
        },
        yAxis: {
            title: {
                text: 'Iznos'
            },
            plotLines: [{
                value: 0,
                width: 0.5,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '°C'
        },
        legend: {
            /*layout: 'vertical',*/

            verticalAlign: 'bottom',
            borderWidth: 0
        },
        series: data
    });



	var data = [];
	var kategorije = [] ;
	arg1.filter(function(la){
		return +la.klasifikacijaBroj == 611
		})
		.forEach(function(po){
			var tempAr = [po.opstina, po.ukupno];
			data.push(tempAr);
			kategorije.push(po.opstina)
		})


//Average for whole data set


var $container1 = $('#sideVisMiddle'),
        chart,
        origChartWidth = 400,
        origChartHeight = 200,
        chartWidth = origChartWidth,
        chartHeight = origChartHeight;


    $container1 .highcharts({
        chart: {
        	backgroundColor: "#7DC1D1",
    		width: chartWidth,
            height: chartHeight,
            type: 'bar'
        },
        title: {
            text: 'Uporedni prikaz iznosa za konto : ' + 611
        },

        xAxis: {
            categories: kategorije,
            title: {
                text: "Opštine"
            }
        },
        yAxis: {

            title: {
               /* text: 'Population (millions)',
                align: 'high'*/
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' din'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                },
                color: 'red'
            }
        },
      /*  legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 80,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },*/
        credits: {
            enabled: false
        },
        series:[{
        	 name: 'Iznos',
        	 data : data
        }]
    });







///end on load
}



//sideVisTop
//sideVisMiddle
//sideVisBottom




/*=====  End of vis  ======*/