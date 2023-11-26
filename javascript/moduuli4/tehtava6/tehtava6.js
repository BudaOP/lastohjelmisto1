"use strict";

const form = document.querySelector("form");
const input = document.getElementById("query");
const jokes = document.getElementById("jokes");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  try {
    const response = await fetch(
      `https://api.chucknorris.io/jokes/search?query=${input.value}`
    );
    const jsonData = await response.json();

    jokes.innerHTML = "";

    jsonData.result.forEach((result) => {
      const article = document.createElement("article");
      const p = document.createElement("p");

      p.innerHTML = result.value;

      article.appendChild(p);
      jokes.appendChild(article);
    });
  } catch (error) {
    console.log(error.message);
  }
});
