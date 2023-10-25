#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let count = 0;
  let prevUser = -1;
  let current = -1;
  const ans = {};
  for (const info of body) {
    current = info.userId;
    if (prevUser === -1) { prevUser = info.userId; }
    if (info.userId !== prevUser) {
      ans[String(prevUser)] = count;
      count = 0;
      prevUser = info.userId;
    }
    if (info.completed === true) {
      count += 1;
    }
  }
  ans[current] = count;
  console.log(ans);
});
