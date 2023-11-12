'use strict';

const numbers = []

for (let i = 0; i < 5; i++) {
    const num = prompt("Please enter a number: ");
    numbers.push(num)
}

for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i])
}