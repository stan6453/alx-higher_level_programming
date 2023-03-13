#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1 || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(Number(process.argv[2])));
