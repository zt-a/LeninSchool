var aside_menu = false;

function main() {
    $('.aside_menu').hide();
    $('#main').css({ 'margin-left': '0px' });
    $('.main_footer').css({ 'margin-left': '0px' });
    $('.footer').css({ 'margin-left': '0px' });
    aside_menu = true;
}

function openMenu() {
    if (aside_menu == false) {
        $('.aside_menu').hide();
        $('#main').css({ 'margin-left': '0' });
        $('.main_footer').css({ 'margin-left': '0' });
        aside_menu = true;
    } else {
        $('.aside_menu').show();
        $('#main').css({ 'margin-left': '250px' });
        $('.main_footer').css({ 'margin-left': '250px' });
        aside_menu = false;
    }

}