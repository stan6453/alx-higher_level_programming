#!/usr/bin/node
const args = process.argv.slice(2);
const nums = args.map((arg) => Number(arg));
nums.sort((a, b) => b - a);
nums[1] ? console.log(nums[1]) : console.log('0');
