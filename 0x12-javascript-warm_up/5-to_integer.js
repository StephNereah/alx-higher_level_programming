#!/usr/bin/node
let i = parseInt(process.argv[2]);
if (!isNaN(i)) {
	console.log(`My number: ${i}`);
} else {
	console.log('Not a number');
}
