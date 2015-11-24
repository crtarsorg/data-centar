function get_request_form_data(parentDivId) {

    var municipalities = [];
    $('#municipalities :selected').each(function (i, selected) {
        municipalities[i] = $(selected).val();
    });

    var classifications = [];
    $('#classifications :selected').each(function (i, selected) {
        classifications[i] = parseInt($(selected).val());
    });

    var data = {
        "tipPodataka": $('#data_type').val(),
        "godine": [parseInt($('#years').val())],
        "opstine": municipalities,
        "klasifikacijaBroj": classifications
    };

    return data;
}
function getFormData(referenceId){


    var classifications = [];
    $('#'+ referenceId + ' #classifications :selected').each(function(i, selected){
      classifications[i] = parseInt($(selected).val());
    });

    var data = {
        "tipPodataka": $( '#'+ referenceId + ' #data_type' ).val(),
        "godine": [parseInt($('#'+ referenceId + ' #years').val())],
        "klasifikacijaBroj": classifications
    };

    return data;
}

function executePost(data, postUrl, respBoxId, reqBoxId){
    $.ajax({
          type: "POST",
          url: postUrl,
          contentType: 'application/json',
          data: JSON.stringify(data),
          success: function(rsp){
              $('#' + reqBoxId).text(JSON.stringify(data, null, 4));
              $('#' + respBoxId).text(JSON.stringify(rsp, null, 4));
              Prism.highlightAll();
          }
        });
}