"use strict";

const input = document.getElementById("calculation");

if (input.value.includes("+")) {
  const sum = calculation.value.split("+");
  console.log(sum);
} else if (input.value.includes("-")) {
  const sub = calculation.value.split("-");
} else if (input.value.includes("*")) {
  const multi = calculation.value.split("*");
} else if (input.value.includes("/")) {
  const div = calculation.value.split("/");
}

// console.log(sum);
