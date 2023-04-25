#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const pageUrl = process.argv[2];
const outputFile = process.argv[3];

request(pageUrl, (err, res, body) => {
  if (err) process.exit(1);
  fs.writeFile(outputFile, body, 'utf-8', (err) => {
    if (err) process.exit(1);
  });
});
