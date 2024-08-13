$(document).ready(function () {
  const url = 'https://swapia-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data, textStatus) {
    for (const result of data.results) {
      const sanitizedTitle = $('<div>').text(result.title).html();
      $('UL#list_movies').append(`<li>${sanitizedTitle}</li>`);
    }
  });
});
