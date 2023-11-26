"use strict";

const target = document.querySelector('#target');

const item1 = document.createElement("li");
const item2 = document.createElement("li");
const item3 = document.createElement("li");

item2.classList.add("my-item");

const t1 = document.createTextNode('First item');
const t2 = document.createTextNode('Second item');
const t3 = document.createTextNode('Third item');

item1.appendChild(t1);
item2.appendChild(t2);
item3.appendChild(t3);

target.appendChild(item1);
target.appendChild(item2);
target.appendChild(item3);