const fs = require('fs');
let input = fs.readFileSync('./input.txt', {encoding: 'utf-8'});

let arr = input.split('\n');
arr = arr.map((item) => parseInt(item));

const seenFrequencies = [];
let frequency = 0;
let i = 0;
let found = 0;

while(!found) {
    frequency += arr[i];
    console.log(frequency)
    if (seenFrequencies.includes(frequency)) found = true;
    seenFrequencies.push(frequency);
    i++;
    if (i == arr.length) i = 0;
}
// 549
