var main = function(){
    checkEntryForm();
    showNoteBooleans();

    $("#add-entry-link").click(toggleEntryForm);
    $("#cancel-entry-form").click(toggleEntryForm);
};

$(document).ready(main);