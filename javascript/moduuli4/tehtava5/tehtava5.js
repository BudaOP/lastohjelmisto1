"use strict";

const norrisJoke = async () => {
  try {
    const response = await fetch("https://api.chucknorris.io/jokes/random");
    const jsonData = await response.json();
    console.log(jsonData.value);
  } catch (error) {
    console.log(error.message);
  }
};

norrisJoke();
