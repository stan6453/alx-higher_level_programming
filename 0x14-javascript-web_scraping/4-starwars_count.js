#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) process.exit(1);

  let count = 0;
  const data = JSON.parse(body);
  for (const movies of data.results) {
    for (const character of movies.characters) {
      if (character.endsWith('/18/')) count++;
    }
  }
  console.log(count);
});
