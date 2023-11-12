'use strict';


const name = prompt("Please enter your name:");

const randomNumber = Math.floor(Math.random() * 4) + 1;

let room;

switch (randomNumber) {
    case 1:
        room = "Gryffindor";
    case 2:
        room = "Slytherin";
    case 3:
        room = "Hufflepuff";
    case 4:
        room = "Ravenclaw";
}

document.querySelector('#target').innerHTML = `${name}, you are ${room}.`;