'use strict';


const num1 = parseInt(prompt("Please enter your number:"));
const num2 = parseInt(prompt("Please enter your number:"));
const num3 = parseInt(prompt("Please enter your number:"));

const sum = num1 + num2 + num3;

const product = num1 * num2 * num3;

const average = sum / 3;

document.querySelector('#target').innerHTML = 'Sum: ' + sum + '<br>Product: ' + product + '<br>Average: ' + average;