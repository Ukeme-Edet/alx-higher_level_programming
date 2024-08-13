$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  function translate () {
    const lang = $('INPUT#language_code').val();
    $.get(url + lang, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress((e) => e.which === 13 && translate());
});
