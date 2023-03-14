#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  list.forEach((element) => arr.unshift(element));
  return arr;
};
