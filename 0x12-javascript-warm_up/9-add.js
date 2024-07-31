#!/usr/bin/node

// function declaration
function add (a, b) {
  return a + b;
}

// get command line arguments
const args = process.argv.slice(2);

// convert a and b into an integer with base 10
const a = parseInt(args[0], 10);
const b = parseInt(args[1], 10);

// check if arguments are integers or not
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
// call the function to return sum of arguments
  console.log(add(a, b));
}
