$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (data, textStatus) {
    $('div#hello').text(data.hello);
  });
});
