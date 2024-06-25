#!/bin/usr/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      let msg = '';
      for (let j = 0; j < this.width; j++) {
        msg += c;
      }
      console.log(msg);
    }
  }
}
module.exports = Square;
