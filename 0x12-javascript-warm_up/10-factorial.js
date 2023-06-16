#!/usr/bin/node
// JavaScript factorial

const fac = parseInt(process.argv[2]);

function findFactorial (fac) {
  if (!fac) { return 1; }

  if (fac <= 0) { return; }
  return findFactorial(fac - 1) * fac;
}
console.log(findFactorial(fac));
