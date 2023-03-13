#!/usr/bin/node
const argCount = process.argv.length;
argCount <= 2 && console.log('No argument');
argCount > 2 && console.log('Argument found');
