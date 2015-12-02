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
        "tipPodataka": [],
        "godine": [parseInt($('#years').val())],
        "opstine": municipalities,
        "klasifikacija": {
            'broj': classifications,
            "pocinjeSa": ""
        },
        "filteri":{}
    };

    if ($('#select_both_sources').is(":checked")){
        data['tipPodataka'] = ["rashodi", "prihodi"];
    }else{
        data['tipPodataka'] = [$('#data_type').val()];
    }

    if($('#pocinje_sa').val() != ""){
        data['klasifikacija']['pocinjeSa'] = $('#pocinje_sa').val();
    }

    if ($('#ukupno').is(":checked")){
        data.filteri.ukupno = {};
        if ($('#ukupno_gte').val() != ""){
            data.filteri.ukupno.veceIliJednako = parseInt($('#ukupno_gte').val());
        }
        if ($('#ukupno_lte').val() != ""){
            data.filteri.ukupno.manjeIliJednako = parseInt($('#ukupno_lte').val());
        }

    }

    if ($('#sopstveni_prihodi').is(":checked")){
        data.filteri.sopstveniPrihodi = {};
        if ($('#sopstveni_prihodi_gte').val() != ""){
            data.filteri.sopstveniPrihodi.veceIliJednako = parseInt($('#sopstveni_prihodi_gte').val());
        }
        if ($('#sopstveni_prihodi_lte').val() != ""){
            data.filteri.sopstveniPrihodi.manjeIliJednako = parseInt($('#sopstveni_prihodi_lte').val());
        }

    }

    if ($('#prihodi_budzeta').is(":checked")){
        data.filteri.prihodiBudzeta = {};
        if ($('#prihodi_budzeta_gte').val() != ""){
            data.filteri.prihodiBudzeta.veceIliJednako = parseInt($('#prihodi_budzeta_gte').val());
        }
        if($('#prihodi_budzeta_lte').val() != ""){
            data.filteri.prihodiBudzeta.manjeIliJednako = parseInt($('#prihodi_budzeta_lte').val());
        }
    }

    if ($('#donacije').is(":checked")){
        data.filteri.donacije = {};
        if ($('#donacije_gte').val() != ""){
            data.filteri.donacije.veceIliJednako = parseInt($('#donacije_gte').val());
        }
        if ($('#donacije_lte').val() != ""){
            data.filteri.donacije.manjeIliJednako = parseInt($('#donacije_lte').val());
        }

    }

    if ($('#ostali').is(":checked")){
        data.filteri.ostali = {};
        if ($('#ostali_gte').val() != ""){
            data.filteri.ostali.veceIliJednako =  parseInt($('#ostali_gte').val());
        }
        if ($('#ostali_lte').val() != ""){
            data.filteri.ostali.manjeIliJednako =  parseInt($('#ostali_lte').val());
        }

    }

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

function initFiltersDisplay(){
     if($('#ukupno').prop('checked')){
          $('#ukupno_gte').prop("disabled", false);
          $('#ukupno_lte').prop("disabled", false);
        }else{
          $('#ukupno_gte').prop("disabled", true);
          $('#ukupno_lte').prop("disabled", true);
        }

        $('#ukupno').change(function(){
            if($('#ukupno').prop('checked')){
              $('#ukupno_gte').prop("disabled", false);
              $('#ukupno_lte').prop("disabled", false);
            }
            else{
              $('#ukupno_gte').prop("disabled", true);
              $('#ukupno_lte').prop("disabled", true);
            }
        });

     if($('#sopstveni_prihodi').prop('checked')){
          $('#sopstveni_prihodi_gte').prop("disabled", false);
          $('#sopstveni_prihodi_lte').prop("disabled", false);
        }else{
          $('#sopstveni_prihodi_gte').prop("disabled", true);
          $('#sopstveni_prihodi_lte').prop("disabled", true);
        }

        $('#sopstveni_prihodi').change(function(){
            if($('#sopstveni_prihodi').prop('checked')){
              $('#sopstveni_prihodi_gte').prop("disabled", false);
              $('#sopstveni_prihodi_lte').prop("disabled", false);
            }
            else{
              $('#sopstveni_prihodi_gte').prop("disabled", true);
              $('#sopstveni_prihodi_lte').prop("disabled", true);
            }
        });

     if($('#prihodi_budzeta').prop('checked')){
          $('#prihodi_budzeta_gte').prop("disabled", false);
          $('#prihodi_budzeta_lte').prop("disabled", false);
        }else{
          $('#prihodi_budzeta_gte').prop("disabled", true);
          $('#prihodi_budzeta_lte').prop("disabled", true);
        }

        $('#prihodi_budzeta').change(function(){
            if($('#prihodi_budzeta').prop('checked')){
              $('#prihodi_budzeta_gte').prop("disabled", false);
              $('#prihodi_budzeta_lte').prop("disabled", false);
            }
            else{
              $('#prihodi_budzeta_gte').prop("disabled", true);
              $('#prihodi_budzeta_lte').prop("disabled", true);
            }
        });

    if($('#donacije').prop('checked')){
          $('#donacije_gte').prop("disabled", false);
          $('#donacije_lte').prop("disabled", false);
        }else{
          $('#donacije_gte').prop("disabled", true);
          $('#donacije_lte').prop("disabled", true);
        }

        $('#donacije').change(function(){
            if($('#donacije').prop('checked')){
              $('#donacije_gte').prop("disabled", false);
              $('#donacije_lte').prop("disabled", false);
            }
            else{
              $('#donacije_gte').prop("disabled", true);
              $('#donacije_lte').prop("disabled", true);
            }
        });

    if($('#ostali').prop('checked')){
          $('#ostali_gte').prop("disabled", false);
          $('#ostali_lte').prop("disabled", false);
        }else{
          $('#ostali_gte').prop("disabled", true);
          $('#ostali_lte').prop("disabled", true);
        }

        $('#ostali').change(function(){
            if($('#ostali').prop('checked')){
              $('#ostali_gte').prop("disabled", false);
              $('#ostali_lte').prop("disabled", false);
            }
            else{
              $('#ostali_gte').prop("disabled", true);
              $('#ostali_lte').prop("disabled", true);
            }
        });
}
