#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.slice(2);
if (args[0] === undefined) { console.log('No argument'); }
args.forEach(element => {
  console.log(`${element}`);
});
