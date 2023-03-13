#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));

if (num) {
  console.log(`My number: ${num}`);
}  else if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('Not a number');
}
