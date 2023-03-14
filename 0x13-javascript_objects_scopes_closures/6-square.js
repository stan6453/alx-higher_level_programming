#!/usr/bin/node
const BaseSqaure = require('./5-square');

class Square extends BaseSqaure {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
      return;
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}

module.exports = Square;
