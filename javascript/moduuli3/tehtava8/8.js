"use strict";

const start = document.getElementById("start");
const firstNum = document.getElementById("num1");
const secondNum = document.getElementById("num2");
const options = document.getElementById("operation");
const output = document.getElementById("result");

start.addEventListener("click", function () {
  const num1 = parseFloat(firstNum.value);
  const num2 = parseFloat(secondNum.value);

  if (options.value === "add") {
    const result = num1 + num2;
    output.innerHTML = `${result}`;
  } else if (options.value === "sub") {
    const result = num1 - num2;
    output.innerHTML = `${result}`;
  } else if (options.value === "multi") {
    const result = num1 * num2;
    output.innerHTML = `${result}`;
  } else if (options.value === "div") {
    const result = num1 / num2;
    output.innerHTML = `${result}`;
  }
});
