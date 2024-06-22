#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);
args.sort();
args.pop();
if (args.at(-1) === undefined) { console.log(0); } else {
  console.log(args.at(-1));
}
