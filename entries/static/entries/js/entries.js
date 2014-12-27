function checkEntryForm() {
    // See if the entry form has an error on it (meaning it wasn't successfully added
    if($(".error-input").length){
        // If so, then set the "Add Entry" to hidden and show the form instead
        $("#add-entry").hide();
        $("#entry-form").show();
    } else {
        // Otherwise just hide the entry form
        $("#entry-form").hide();
    }
}

function toggleEntryForm(){
    console.log("Entry form toggled!");
    $("#add-entry").toggle();
    $("#entry-form").toggle();
}

function showNoteBooleans(){
    $('.explore').hide();
    $('.inspiration').hide();

    var type_select = $('#id_type');
    type_select.change(function () {
        if ($(this).val() == 'note') {
            $('.explore').show();
            $('.inspiration').show();
        }
        else {
            $('.explore').hide();
            $('.inspiration').hide();
        }
    });
}