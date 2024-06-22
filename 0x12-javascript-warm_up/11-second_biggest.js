#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);
args.sort((a, b) => a - b);
if (args[args.length - 2] === undefined) { console.log(0); } else {
  console.log(args[args.length - 2]);
}
