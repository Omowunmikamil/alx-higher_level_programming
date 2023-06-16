#!/usr/bin/node
// Print with basic javaScript

const fun = 'C is fun';

if (process.argv.lenght >= 3) {
  let index = process.argv[2];
  while (index > 0) {
    console.log(fun);
    index--;
  }
} else {
  console.log('Missing number of occurrences');
}
