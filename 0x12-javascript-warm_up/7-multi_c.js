#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const len = Math.floor(Number(process.argv[2]));
  for (let i = 0; i < len; i += 1) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
