#!/usr/bin/node
function factorial(n) {
  return n === 0 || isNaN(n) ? : n * factorial(n - 1);

const num = Number(process.argv[2]);
const result = factorial(num);

console.log(result);
