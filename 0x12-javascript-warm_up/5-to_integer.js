#!/usr/bin/node
const number = process.argv[2];
isNaN(number) ? console.log('Not a number') : console.log('My number: ' + parseInt(number, 10));
