var main = function(){
    $("#entry-form").hide();

    $("#add-entry-link").click(toggleEntryForm);
    $("#cancel-entry-form").click(toggleEntryForm);
};

$(document).ready(main);