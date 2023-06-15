#!/usr/bin/node
// Argument value output with JavaScript

const myArg = process.argv[2];

if (myArg) {
  console.log(myArg);
} else {
  console.log('No argument');
}
