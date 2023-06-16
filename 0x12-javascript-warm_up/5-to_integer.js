#!/usr/bin/node
// Argument handling with JavaScript

let arg = parseInt(process.argv[2]);

if (arg) {
  arg = 'My number: ' + arg;
  console.log(arg);
} else {
  console.log('Not a number');
}
