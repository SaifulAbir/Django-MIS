
function getCurrentDate(bdformat=false) {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    if (bdformat){
        today = dd + '-' + mm + '-' + yyyy;
        return today;
    }else {
        today = yyyy + mm + dd;
        return today;
    }

}

function getCurrentDateStandard() {
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    today = yyyy + '-' + mm + '-' + dd;
    return today;
}

function getDateBdFormatToStandardDateFormat(date) {
    var array = date.split("-");
    var date = array[2]+'-'+array[1]+'-'+array[0];
    return date;
}

function eventAllInputFieldEnabled() {
    $( "#id_start" ).prop( "disabled", false );
    $( "#id_end" ).prop( "disabled", false );
    $( "#id_title" ).prop( "disabled", false );
}