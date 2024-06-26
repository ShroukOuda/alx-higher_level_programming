#!/usr/bin/node
const arr = require('./100-data').list;
const mp = arr.map((value, index) => value * index);
console.log(arr);
console.log(mp);
