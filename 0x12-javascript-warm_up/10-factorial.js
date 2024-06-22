#!/usr/bin/node
const { argv } = require('node:process');
const arg = Number(argv[2]);
function fact (num) {
  let fact = 1;
  if (isNaN(num)) { return 1; }
  for (let i = num; i > 1; i--) { fact *= i; }
  return fact;
}
console.log(fact(arg[2]));
