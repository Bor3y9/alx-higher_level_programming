#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(response.body);
    console.log(data.title);
  }
});
