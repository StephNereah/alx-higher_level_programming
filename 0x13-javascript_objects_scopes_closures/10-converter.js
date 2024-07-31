#!/usr/bin/node
exports.converter = function (base) {
  function c (number) {
    return number.toString(base);
  }
  return c;
};
