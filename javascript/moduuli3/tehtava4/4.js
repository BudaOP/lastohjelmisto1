'use strict';

const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const target = document.querySelector('#target');

for (let i = 0; i < students.length; i++) {
  const options = document.createElement("option");

  const student = students[i];

  options.value = student.id;
  options.textContent = student.name;

  target.appendChild(options);
}