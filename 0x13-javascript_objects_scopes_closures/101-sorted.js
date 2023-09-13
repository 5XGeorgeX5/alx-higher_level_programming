#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const id in dict) {
  const occurrence = dict[id];
  if (newDict[occurrence] === undefined) {
    newDict[occurrence] = [id];
  } else {
    newDict[occurrence].push(id);
  }
}
console.log(newDict);
