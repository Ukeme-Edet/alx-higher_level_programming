#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
