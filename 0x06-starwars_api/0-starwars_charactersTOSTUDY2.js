Using axios

npm install axios --global  # global installion of axios

#!/usr/bin/node

const axios = require('axios');

const getFilmCharacters = async (filmId) => {
  try {
    const response = await axios.get(`https://swapi-api.hbtn.io/api/films/${filmId}`);
    const characters = response.data.characters;

    // Fetch each character's name in the correct order
    for (const url of characters) {
      const characterResponse = await axios.get(url);
      console.log(characterResponse.data.name);
    }
  } catch (err) {
    console.error(err.message);
  }
};

// Get the film ID from command-line arguments
const filmId = process.argv[2];
if (filmId) {
  getFilmCharacters(filmId);
} else {
  console.error("Please provide a film ID.");
}

/*
 * Explanation
axios.get: Fetches the film data and characters.
Async/Await: Ensures that character names are fetched in the correct order.
for...of loop: Iterates over the list of character URLs and fetches their names.
*/


/*Using Native fetch (Node.js v18+)
If you're using Node.js v18 or higher, you can use the native fetch API:
*/
#!/usr/bin/node

const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const getFilmCharacters = async (filmId) => {
  try {
    const response = await fetch(`https://swapi-api.hbtn.io/api/films/${filmId}`);
    const data = await response.json();
    const characters = data.characters;

    // Fetch each character's name in the correct order
    for (const url of characters) {
      const characterResponse = await fetch(url);
      const characterData = await characterResponse.json();
      console.log(characterData.name);
    }
  } catch (err) {
    console.error(err.message);
  }
};

// Get the film ID from command-line arguments
const filmId = process.argv[2];
if (filmId) {
  getFilmCharacters(filmId);
} else {
  console.error("Please provide a film ID.");
}

/*Explanation
Dynamic fetch Import: Since fetch is not available by default in earlier Node.js versions, this dynamic import ensures compatibility. You can replace this with a simple require('node-fetch') if using an older version.
Async/Await and Fetch: Ensures sequential execution to maintain the order of the character names.
Both alternatives will fulfill the original code's functionality while using modern and more efficient methods for HTTP requests.
These alternative codes do not fully meet the specific requirements listed in your question for the following reasons:

Use of the request Module: The requirements specify that you must use the request module. Both alternative solutions use either axios or fetch, which do not satisfy this requirement.

Code Compliance: The provided alternatives are compliant with modern JavaScript practices and use const and let instead of var, which is good. However, they might not be strictly semistandard-compliant due to the different modules used (axios and fetch).

Execution Format: Both scripts can be made executable, but they must use the request module as explicitly required.
*/
