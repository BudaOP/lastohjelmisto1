'use strict';

const numList = [];

let num = parseInt(prompt("Please enter a number (stop by typing zero): "));
let loop = true

while (loop) {
    if (num !== 0) {
        numList.push(num);
        num = parseInt(prompt("Please enter a number (stop by typing zero): "));}
        else {
            loop = false
            numList.sort((a, b) => b - a);
            console.log(numList)
    }
}