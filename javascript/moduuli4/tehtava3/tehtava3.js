"use strict";

const form = document.querySelector("form");
const input = document.getElementById("query");
const results = document.getElementById("results");

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  try {
    const response = await fetch(
      `https://api.tvmaze.com/search/shows?q=${input.value}`
    );
    const jsonData = await response.json();
    console.log(jsonData);

    results.innerHTML = "";

    jsonData.forEach((result) => {
      const heading = document.createElement("h2");
      heading.textContent = result.show.name;

      const a = document.createElement("a");
      a.href = result.show.url;
      a.target = "_blank";

      const img = document.createElement("img");
      img.src = result.show.image?.medium;
      img.alt = result.show.name;

      const article = document.createElement("article");

      const summary = document.createElement("div");
      summary.innerHTML = result.show.summary;

      article.appendChild(heading);
      article.appendChild(a);
      article.appendChild(img);
      article.appendChild(summary);

      results.appendChild(article);
    });
  } catch (error) {
    console.log(error.message);
  }
});
