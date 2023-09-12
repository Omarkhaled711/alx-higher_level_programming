#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === '' || c === null || c === undefined) {
      c = 'X';
    }
    c = String(c);
    for (let i = 0; i < this.size; i += 1) {
      console.log(c.repeat(this.size));
    }
  }
};
