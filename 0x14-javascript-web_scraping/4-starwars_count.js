#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const search = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let count = 0;
  for (const info of body.results) {
    for (const character of info.characters) {
      if (character === search) {
        count += 1;
      }
    }
  }
  console.log(count);
});
