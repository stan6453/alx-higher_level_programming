#!/usr/bin/node
const fs = require('fs');

for (const args of process.argv.slice(2)) {
  fs.readFile(args, (err, data) => {
    if (!err) {
      process.stdout.write(data.toString());
    }
  });
}
