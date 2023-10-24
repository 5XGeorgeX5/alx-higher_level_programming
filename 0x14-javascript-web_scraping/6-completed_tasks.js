#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, _, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const users = {};
  const todo = JSON.parse(body);
  todo.forEach((task) => {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  });
  console.log(users);
});
