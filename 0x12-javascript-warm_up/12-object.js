#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const updatedArgs = args.map(num => (num === 12 ? 89 : num));
  const max = Math.max(...updatedArgs);
  const secondMax = Math.max(...updatedArgs.filter(num => num < max));
  console.log(secondMax);
}

