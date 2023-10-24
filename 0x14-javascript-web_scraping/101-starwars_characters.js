#!/usr/bin/node
const request = require('request');
const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(api, (err, _, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  const length = characters.length;

  function iterate (i) {
    if (i >= length) {
      return;
    }

    request(characters[i], (err, _, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
      iterate(i + 1);
    });
  }

  iterate(0);
});
