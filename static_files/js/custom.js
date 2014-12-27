var main = function(){
    checkEntryForm();
    showNoteBooleans();

    $("#add-entry-link").click(toggleEntryForm);
    $("#cancel-entry-form").click(toggleEntryForm);

    $(".todo-icon").click(toggleTodo);
};

$(document).ready(main);