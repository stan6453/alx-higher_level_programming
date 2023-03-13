#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = process.argv;
console.log(add(Number(args[2]), Number(args[3])));
