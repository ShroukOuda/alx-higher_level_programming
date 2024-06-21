#!/usr/bin/node
const { argv } = require('node:process');
const numArgs = Number(argv[2]);
if (!isNaN(numArgs)) { console.log(`My number: ${Math.floor(numArgs)}`); } else {
  console.log('Not a number');
}
