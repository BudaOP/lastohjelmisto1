'use strict';

const participantsList = [];
const participants = parseInt(prompt("Please enter a number of participants: "));

for (let i = 1; i <= participants; i++) {
    const name = prompt("Please enter a name: ");
    participantsList.push(name)
}

participantsList.sort();

const target = document.querySelector('#target');

for (let i = 0; i < participants; i++) {
    target.innerHTML += `<li>${participantsList[i]}</li>`;
}
