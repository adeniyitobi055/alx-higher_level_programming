#!/usr/bin/node

const request = require('request');
const charId = '18';
let count = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
