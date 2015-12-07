//https://developers.google.com/youtube/player_parameters?hl=en


var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";

var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;

function onYouTubePlayerAPIReady() {
    player = new YT.Player('ytplayerLanding', {
        /* height: '390',
         width: '640',*/
        videoId: 'k7uuLp5FpJA',
        playerVars: {
            'showinfo': 0,
            /*'controls': 1,*/
            'autohide': 1
        }

    });
};



function generateRandomQuery(){
    // Eventually, this logic will have to be expanded for datasources that are not budges (.e.g. procurements) and different years.
    var budgetType = utils.getRandomBudgetType().toUpperCase();
    var municipality = utils.getRandomMunicipality().toUpperCase();

    var text = "Show me data about " +
        "<span id='query-param-data-source'>BUDGET</span> " +
        "<span id='query-param-budget-type'>" + budgetType + "</span> " +
        "for <span id='query-param-municipality'>" + municipality + "</span> " +
        "in <span id='query-param-year'>2015</span>";

    $("#searchWithParams").html(text);
}

function executeRandomQuery(getUrl){

     var data = {
         'source': $('#query-param-data-source').html(),
         'type': $('#query-param-budget-type').html(),
         'municipality': $('#query-param-municipality').html(),
         'year': parseInt($('#query-param-year').html()),
     };

     $.ajax({
         type: "GET",
         url: getUrl,
         contentType: 'application/json',
         data: data
    });
}


$(function() {

    $("#anotherFavQuery").click(function() {
        generateRandomQuery();
    });

});

$(function() {


    var colors = (function() {
        var colors = [],
            base = Highcharts.getOptions().colors[0],
            i;

        for (i = 0; i < 10; i += 1) {
            // Start out with a darkened base color (negative brighten), and end
            // up with a much brighter color
            colors.push(Highcharts.Color(base).brighten((i - 3) / 7).get());
        }
        return colors;
    }());




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

    var params2 = {
        "tipPodataka": [
            "rashodi",
            "prihodi"
        ],
        "godine": [
            2015
        ],
        "opstine": [

        ],
        "klasifikacija": {
            "broj": [
            ],
            "pocinjeSa": ""
        },
        "filteri": {}
    };


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
            data: JSON.stringify(params2),
            contentType: "application/json;charset=utf-8",
            dataType: "json",
            success: function(returnhtml){
                result2 = returnhtml;
            }

        })



    ).then(function() {


        visu(result1, result2)
    });

    // if is it exact match - take that, other case, take all childes and sum it
    function filterByConto (arrayCities, conto) {

      var tempValues = 0;

      arrayCities.forEach(function (datum) {
        var rx = new RegExp("^"+conto+"0+");
        var rx2 = new RegExp("^"+conto);

        if(rx.test( datum.klasifikacijaBroj ) )
          return (datum.ukupno);

          else if(rx2.test( datum.klasifikacijaBroj ) )
            tempValues+= datum.ukupno;
      })
      return tempValues;
    }


    function filterCitiesByContos (raw, cities, contos) {


      var gradovi  =[];

        cities.forEach(function (city) {
            var tempCity = {};

            tempCity.muncipality = city;
            tempCity.data = [];

            var tempData = raw.filter(function (el) {
              return el.opstina == city
            })

            contos.forEach(function (conto) {
                var tempConto = {};
                tempConto.conto = conto;
                tempConto.value = filterByConto(tempData, conto)

                tempCity.data.push( tempConto );
            })


            gradovi.push(tempCity);

        })

      return gradovi;
    }
    //http://stackoverflow.com/a/14438954
  function onlyUnique(value, index, self) {
      return self.indexOf(value) === index;
  }

    function visu (arrayAvg, arrayCities) {

    // calculate

    var data = [
    {
        "conto": 710000,
        "opis": "Prihodi",
        "vrednost": 1
    }, {
        "conto": 712000,
        "opis": "Porez na zarade",
        "vrednost": 1
    }, {
        "conto": 713000,
        "opis": "Porez na imovinu",
        "vrednost": 1
    }, {
        "conto": 730000,
        "opis": "Donacije i transferi",
        "vrednost": 1
    }, {
        "conto": 733000,
        "opis": "Transferi od drugih nivoa vlasti",
        "vrednost": 1
    }, {
        "conto": 410000,
        "opis": "Rashodi za zaposlene",
        "vrednost": 1
    }, {
        "conto": 422000,
        "opis": "Troškovi putovanja",
        "vrednost": 1
    }, {
        "conto": 460000,
        "opis": "Donacije, dotacije i transferi",
        "vrednost": 1
    }, {
        "conto": 450000,
        "opis": "Subvencije",
        "vrednost": 1
    }]

    var cities = arrayCities.map(function (la) {
      return la.opstina;
    })

    cities = cities.filter(onlyUnique);

    var contos = [71,712,713,73,733,41,422,46,45];

    var res = filterCitiesByContos(arrayCities, cities, contos )



    var updatedData = [];

    arrayAvg.forEach(function(el){

      var temp = data.filter(function (el1) {
        return +el1.conto == +el.conto;
      })

      temp = temp[0]

      if(temp != undefined)
        {
          temp.vrednost = el.avg;
          updatedData.push(temp);
        }
    })

    data.concat(updatedData)

    console.log(data);

    // filter muncipalities
    var gradovi = []

    gradovi = res;


    var niz = [];

    gradovi.forEach(function(lo) {
      var tempData = lo.data.map(function (a) {
        return a.value
      })

      var temp_el = {
          type: 'column',
          name: lo.muncipality,
          data: tempData /*[3000, 2000, 1000, 3000, 4000, 5000, 8000, 15000, 18000]*/
      }

      niz.push(temp_el);

    })
    var zaProseke = niz.map(function(la){ return la.data })
    var prosek = [] ;

    zaProseke.forEach(function (arg) {
      for (var i = 0, len = arg.length; i < len ; i++) {
        if(prosek[i] ==undefined) prosek[i]=1;
        prosek[i] +=Math.round(arg[i]/len);
      }
    })


console.log(prosek);

    /* for pie*/
    data.forEach(function(temp) {
        temp.name = temp.opis;
        temp.y = temp.vrednost;
    })

    var podaci = data;
    var imena = podaci.map(function(el) {
        return el.name;
    })

    /* for pie*/

    niz.push({
        type: 'spline',
        name: 'Average',
        data: prosek,
        marker: {
            lineWidth: 2,
            lineColor: Highcharts.getOptions().colors[3],
            fillColor: 'white'
        }
    });



    niz.push({
        type: 'pie',
        name: 'Iznos',
        data: podaci,
        center: [960, 80],
        size: 150, // function dynamic value, depending on screen size
        colors: colors,
        showInLegend: false,
        allowPointSelect: true,
        dataLabels: {
            enabled: false,
            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
            style: {
                "color": "white",
                "fontSize": "11px",
                "fontWeight": "bold",
                "textShadow": "none"
            }
        }
    });



    var chartMain = $('.vis').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            backgroundColor: "#7DC1D1"

        },
        title: {
            text: 'Data for 10 muncipalities',
            style: {
                color: "white"
            }
        },
        colors: ["#a6cee3","#1f78b4","#b2df8a","#33a02c","#fb9a99","#e31a1c","#fdbf6f","#ff7f00","#cab2d6","#6a3d9a"],//colors,
         yAxis: {
            type: 'logarithmic',
            minorTickInterval: 0.35
        },
        xAxis: [{
            offset: 0,
            width: 900,
            left: 100,
            categories: imena,
            labels: {
                style: {
                    color: "white",
                    "fontSize": "14px"
                }
            }
        }],
        tooltip: {
            followPointer:true,
            pointFormat: ' {series.name}: <b>{point.y} din</b>'
        },


        labels: {
              /*items: [{
                  html: 'Data for 10 muncipalities',
                  style: {
                      left: '250px',
                      top: '5px',
                      color: (Highcharts.theme && Highcharts.theme.textColor) || 'white'
                  }
              }]*/
        },
        series: niz,
        navigation: {
            buttonOptions: {
                theme: {
                    'stroke-width': 1,
                    "fill":"#7DC1D1",
                    stroke: 'silver',
                    r: 0,
                    states: {
                       /* hover: {
                            fill: '#bada55'
                        },
                        select: {
                            stroke: '#039',
                            fill: '#bada55'
                        }*/
                    }
                }
            }
        }
    });


  }

    ///end of script
});