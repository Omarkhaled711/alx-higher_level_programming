#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i += 1) {
    arr.push(Number(process.argv[i]));
  }
  arr.sort((x, y) => y - x);
  console.log(arr[1]);
}
