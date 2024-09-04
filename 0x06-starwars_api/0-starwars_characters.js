#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get Movie ID from the first positional argument
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

request('https://swapi-api.hbtn.io/api/films/' + movieId, function (err, res, body) {
  if (err) throw err;

  const characters = JSON.parse(body).characters; // Parse the response body to get characters array

  // Function to print characters in order
  const printCharacters = (characters, index) => {
    if (index === characters.length) return; // Base case: all characters printed

    request(characters[index], function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name); // Print the character name
      printCharacters(characters, index + 1); // Recursively call the function for the next character
    });
  };

  printCharacters(characters, 0); // Start printing characters from the first character
});
