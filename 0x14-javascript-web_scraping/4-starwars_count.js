#!/usr/bin/node
const request = require('request');

function counter (count, film) {
  if (film.characters.find((character) => character.endsWith('/18/'))) {
    count++;
  }
  return count;
}

request(process.argv[2], (err, _, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.reduce(counter, 0);
  console.log(count);
});
