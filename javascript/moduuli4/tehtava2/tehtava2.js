"use strict";

const form = document.querySelector("form");
const input = document.getElementById("query");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  try {
    const response = await fetch(
      `https://api.tvmaze.com/search/shows?q=${input.value}`
    );
    const jsonData = await response.json();
    console.log(jsonData);
  } catch (error) {
    console.log(error.message);
  }
});
