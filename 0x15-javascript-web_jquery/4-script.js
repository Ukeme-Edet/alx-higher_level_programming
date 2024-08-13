$(document).ready(function () {
  $('div#update_header').click(function () {
    $('header').hasClass('green')
      ? $('header').removeClass('green') && $('header').addClass('red')
      : $('header').removeClass('red') && $('header').addClass('green');
  });
});
