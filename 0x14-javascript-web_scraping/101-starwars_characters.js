#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const charDict = {};

    const fetchCharacter = async (character) => {
      try {
        const response = await new Promise((resolve, reject) => {
          request(character, (error, _, body) => {
            if (error) {
              reject(error);
            } else {
              resolve(body);
            }
          });
        });
        const { url, name } = JSON.parse(response);
        charDict[url] = name;
      } catch (error) {
        console.error(error);
      }
    };

    const fetchAllCharacters = async () => {
      try {
        await Promise.all(characters.map(fetchCharacter));
        for (const key of characters) {
          console.log(charDict[key]);
        }
      } catch (error) {
        console.error(error);
      }
    };

    await fetchAllCharacters();
  }
});
