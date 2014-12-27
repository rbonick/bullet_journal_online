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

function toggleTodo(){
    var todoIcon = $(this);
    $.ajax({
        url: "/entry/toggle-todo/" + todoIcon.attr('id'),
        success: function(){
            toggleTodoCheck(todoIcon);
        }
    });
    // Needs an ajax call to actually mark as completed in database
}

function toggleTodoCheck(todoIcon){
    if(todoIcon.hasClass("glyphicon-check")){
        todoIcon.addClass("glyphicon-unchecked");
        todoIcon.removeClass("glyphicon-check");
    } else if(todoIcon.hasClass("glyphicon-unchecked")){
        todoIcon.removeClass("glyphicon-unchecked");
        todoIcon.addClass("glyphicon-check");
    }
}