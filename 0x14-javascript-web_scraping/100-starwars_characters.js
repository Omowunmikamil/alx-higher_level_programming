#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie */

const request = require('request');
const args = process.argv.slice(1);
const movie = 'https://swapi-api.hbtn.io/api/films/' + args[1];

request(movie, (err, response, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (err) {
          console.log(err);
	} else {
          console.log(JSON.parse(body).name);	
        }
      });
    }
  }
});
