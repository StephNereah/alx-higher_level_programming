#!/usr/bin/node

// Get command line arguments and convert to integers
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));

// Function to find second largest number
function second (num) {
  if (num.length <= 1) {
    return 0;
  }

  // sort numbers in descending numbers
  num.sort((a, b) => b - a);

  return num[1];
}

console.log(second(args));
