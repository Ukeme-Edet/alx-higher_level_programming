#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    }
    console.log(completedTasks);
  }
});
