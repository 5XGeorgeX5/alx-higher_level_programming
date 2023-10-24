#!/usr/bin/node
const request = require('request');
const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(api, (err, _, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach((char) => {
    request(char, (err, _, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
