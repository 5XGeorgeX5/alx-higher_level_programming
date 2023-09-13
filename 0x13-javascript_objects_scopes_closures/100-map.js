#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((value, i) => value * i);
console.log(list);
console.log(newList);
