#!/usr/bin/node
function factorial (babes) {
  if ((Number.isNaN(babes)) || (babes === 1)) {
    return 1;
  }
  return factorial(babes - 1) * babes;
}

console.log(factorial(parseInt(process.argv[2])));
