const fs = require('fs');
let input = fs.readFileSync('./input.txt', {encoding: 'utf-8'});

let arr = input.split(/\s+/).map(str => str.split('').sort());

let totalTwo = 0;
let totalThree = 0;

for (let i = 0; i < arr.length; i++) { // Go through the boxes
    let letterCounts = {};
    for (let j = 0; j < arr[i].length; j++) { // Go through the box id
        let boxid = arr[i];
        if (!letterCounts[boxid[j]]) letterCounts[boxid[j]] = 1; 
        if (j == boxid.length - 1) { //last letter
            let addTwo = false;
            let addThree = false;
            for (let letter in letterCounts) {
                if (letterCounts[letter] === 2) addTwo = true;
                else if (letterCounts[letter] === 3) addThree = true;
            }
            if (addTwo) totalTwo++;
            if (addThree) totalThree++;
        }
        else {
            if (boxid[j+1] == boxid[j]) letterCounts[boxid[j]]++;
        }
    }
}

console.log('Checksum:', totalTwo * totalThree);
// 7350
