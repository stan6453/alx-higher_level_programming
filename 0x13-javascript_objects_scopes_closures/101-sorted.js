#!/usr/bin/node
const dict = require('./101-data').dict;
const map = {};
for (const key in dict) {
  if (map[dict[key]]) {
    map[dict[key]].push(key);
  } else {
    map[dict[key]] = [key];
  }
}
console.log(map);
