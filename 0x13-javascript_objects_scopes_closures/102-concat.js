#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

const first = argv[2];
const second = argv[3];
const result = argv[4];

fs.readFile(first, (err, fData) => {
  if (err) throw err;
  fs.readFile(second, (err, sData) => {
    if (err) throw err;
    const str = fData + sData;
    fs.writeFile(result, str, (err) => {
      if (err) throw err;
    });
  });
});
