#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieID}/`, (err, res, body) => {
  if (err) process.exit(1);
  const data = JSON.parse(body);
  console.log(data.title);
});
