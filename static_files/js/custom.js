var main = function(){
    checkEntryForm();

    $("#add-entry-link").click(toggleEntryForm);
    $("#cancel-entry-form").click(toggleEntryForm);
};

$(document).ready(main);