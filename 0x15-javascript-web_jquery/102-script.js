$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
});
