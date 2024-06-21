#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined) { console.log('Missing number of occurrences'); } else if (argv[2] > 0) {
  while (argv[2]--) {
    console.log('C is fun');
  }
}
