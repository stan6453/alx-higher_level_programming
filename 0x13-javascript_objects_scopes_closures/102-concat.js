#!/usr/bin/node
const fs = require('fs');

if (process.argv.length <= 2) {
  process.exit(1);
}

const files = process.argv.slice(2, process.argv.length - 1);
const outputFile = process.argv[process.argv.length - 1];
let data = '';

for (const file of files) {
  data += fs.readFileSync(file).toString();
}
fs.writeFile(outputFile, data, () => {});
