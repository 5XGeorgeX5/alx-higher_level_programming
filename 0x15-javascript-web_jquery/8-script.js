$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const movies = data.results;
  $.each(movies, (_, movie) => {
    const name = movie.title;
    const list = $('<li>').text(name);
    $('UL#list_movies').append(list);
  });
});
