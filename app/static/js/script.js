function get_request_form_data(parentDivId){

    var municipalities = [];
        $('#municipalities :selected').each(function(i, selected){
          municipalities[i] = $(selected).val();
        });

        var classifications = [];
        $('#classifications :selected').each(function(i, selected){
          classifications[i] = parseInt($(selected).val());
        });

        var data = {
            "tipPodataka": $( '#data_type' ).val(),
            "godine": [parseInt($('#years').val())],
            "opstine": municipalities,
            "klasifikacijaBroj": classifications
        };

    return data
}