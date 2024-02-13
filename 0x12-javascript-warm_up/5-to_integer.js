#!/usr/bin/node
const uwu = parseInt(process.argv[2]);
if (isNaN(uwu)) {
	console.log('Not a number');
} else {
	console.log('My number: ' + uwu);
}
