#!/usr/bin/node
function callMeMoby (x, theFunction) {
  if (x > 0) {
    while (x--) {
      theFunction();
    }
  }
}
module.exports.callMeMoby = callMeMoby;
