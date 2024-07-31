#!/usr/bin/node
let eren = 0;
exports.logMe = function (item) {
  console.log(eren + ': ' + item);
  eren++;
};
