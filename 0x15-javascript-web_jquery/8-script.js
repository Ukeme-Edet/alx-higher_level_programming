$(document).ready(function () {
  const url = 'https://swapia-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data, textStatus) {
    for (const result of data.results) {
      $('UL#list_movies').append(`<li>${result.title}</li>`);
    }
  });
});
