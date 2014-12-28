function autocollapse() {
    var navbar = $('#autocollapse');
    var navbarHeader = $(".navbar-header");
    var navbarBody = $(".navbar-body");
    navbar.removeClass('collapsed');
    navbarHeader.hide();

    if(window.matchMedia('(max-width: 400px)').matches) {
        navbar.addClass('collapsed');
        navbarHeader.show();
        navbarBody.hide();
    }
}

function navbarToggle() {
    var navbarBody = $(".navbar-body");
    navbarBody.slideToggle();
}

$(document).on('ready', autocollapse);
$(window).on('resize', autocollapse);

$("#navbar-toggle").click(navbarToggle);