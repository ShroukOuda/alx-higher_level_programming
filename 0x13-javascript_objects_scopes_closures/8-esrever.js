#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newList[list.length - 1 - i] = list[i];
  }
  return newList;
};
