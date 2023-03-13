#!/usr/bin/node
function callMeMoby (num, func) {
  for (let i = 0; i < num; i++) {
    func();
  }
}
module.exports.callMeMoby = callMeMoby;
