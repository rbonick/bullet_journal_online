var main = function(){
    checkEntryForm();
    showNoteBooleans();

    $("#add-entry-link").click(toggleEntryForm);
    $("#cancel-entry-form").click(toggleEntryForm);

    $(".glyphicon-unchecked").click(checkTodoOff);
};

$(document).ready(main);