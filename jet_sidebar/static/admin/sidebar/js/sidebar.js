jQuery(function ($) {

    $(".sidebar-dropdown > a").click(function() {
        event.preventDefault();
          $(".page-wrapper").removeClass("toggled-min");
          $(".page-wrapper").addClass("toggled");
          $('#close-sidebar').attr('style','display: block;');
          $('.show-sidebar').attr('style','display: none;');
          $('#body-class').addClass('menu-pinned');
          $('#body-class').removeClass('menu-unpinned');
          $(".sidebar-submenu").slideUp(200);
        if ($(this).parent().hasClass("active")){
            $(".sidebar-dropdown").removeClass("active");
            $(this).parent().removeClass("active");
        } else {
            $(".sidebar-dropdown").removeClass("active");
            $(this).next(".sidebar-submenu").slideDown(200);
            $(this).parent().addClass("active");
            $('#icon_small').attr('class', 'icon_small-none');
            $('#icon_large').attr('class', 'icon_large-block');
        }
    });


function get_cookie(name){
    return document.cookie.split(';').some(c => {
        return c.trim().startsWith(name + '=');
    });
}

// já inicia a sidebar aberta caso nao tenha nada carregado no cookie do navegador do cliente
sidebar_initial_val = get_cookie('sidebar_pinned');
if(sidebar_initial_val == false){
    $(".sidebar-dropdown").removeClass("active");
    $(this).next(".sidebar-submenu").slideDown(200);
    $(this).parent().addClass("active");
    $('#icon_small').attr('class', 'icon_small-none');
    $('#icon_large').attr('class', 'icon_large-block');
}


$("#close-sidebar").click(function() {
  var date = new Date();

  // Default at 365 days.
  days = 365;

  // Get unix milliseconds at current time plus number of days
  date.setTime(+ date + (days * 86400000)); //24 * 60 * 60 * 1000
  get_cookie('sidebar_pinned');
  document.cookie = "sidebar_pinned=false; expires=" + date.toGMTString() + "; path=/";
  $(".page-wrapper").removeClass("toggled");
  $(".page-wrapper").addClass("toggled-min");
  $('#close-sidebar').attr('style','display: none;');
  $('.show-sidebar').attr('style','display: block;');
  $('#body-class').removeClass('menu-pinned');
  $('#body-class').addClass('menu-unpinned');

  $(".sidebar-dropdown").removeClass("active");
  $(".sidebar-submenu").slideUp(200);
  $('#icon_small').attr('class', 'icon_small-block');
  $('#icon_large').attr('class', 'icon_large-none');

});

$(".show-sidebar").click(function() {
  var date = new Date();

  // Default at 365 days.
  days = 365;

  // Get unix milliseconds at current time plus number of days
  date.setTime(+ date + (days * 86400000)); //24 * 60 * 60 * 1000
  get_cookie('sidebar_pinned');
  document.cookie = "sidebar_pinned=true; expires=" + date.toGMTString() + "; path=/";
  $(".page-wrapper").removeClass("toggled-min");
  $(".page-wrapper").addClass("toggled");
  $('#close-sidebar').attr('style','display: block;');
  $('.show-sidebar').attr('style','display: none;');
  $('#body-class').addClass('menu-pinned');
  $('#body-class').removeClass('menu-unpinned');
  $('#icon_small').attr('class', 'icon_small-none');
  $('#icon_large').attr('class', 'icon_large-block');
});

/* mobile actions */
$(".show-sidebar-mobile").click(function() {
  $(".page-wrapper").removeClass("toggled");
  $(".page-wrapper").addClass("toggled-min");
  $('#close-sidebar').attr('style','display: none;');
  $('.show-sidebar').attr('style','display: block;');
});


});

/***********************************************************************************************************************/

