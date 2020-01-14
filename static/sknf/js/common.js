
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

function removeChracterFromString(string, character) {
    string.replace(/character/g, '');
    return string;
}
