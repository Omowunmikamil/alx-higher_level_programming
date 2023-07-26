#!/usr/bin/node
/* Script that reads and prints the content of a file */

const fs = require('fs');
const file = process.argv[2];

fs.writeFile(file, text, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
