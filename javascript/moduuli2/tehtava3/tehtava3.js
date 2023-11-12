'use strict';

const dogList = [];

for (let i = 0; i < 6; i++) {
    const name = prompt("Please enter the name of the dog: ");
    dogList.push(name)
}

dogList.sort();

const target = document.querySelector('#target');

for (let i = dogList.length - 1; i >= 0; i--) {
    target.innerHTML += `<li>${dogList[i]}</li>`;
}
