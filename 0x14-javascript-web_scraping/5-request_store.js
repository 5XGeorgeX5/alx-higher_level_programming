#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const { argv } = require('process');

request(argv[2], (err, _, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(argv[3], body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
