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
