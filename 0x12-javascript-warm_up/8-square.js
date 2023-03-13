#!/usr/bin/node
let num = process.argv[2];
if (!isNaN(num)) {
  num = Number(num);
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('x');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
