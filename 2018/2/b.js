const fs = require('fs');
let input = fs.readFileSync('./input.txt', {encoding: 'utf-8'});

let arr = input.split(/\s+/).map(str => str.split(''));

let matchArr = [];

for (let i = 0; i<arr.length; i++) {
    for (let j = i + 1; j<arr.length; j++) {
        let matchCount = 0;
        let matches = '';
        for (let k = 0; k<arr[i].length; k++) {
            if (arr[i][k] === arr[j][k]) {
                matchCount++;
                matches += arr[i][k];
            }
        }
        matchArr.push([matchCount, matches]);
    }
}

// sort descending by number of matched letters
matchArr.sort((a, b) => {
    return b[0] - a[0];
})

console.log(matchArr[0][1]);
// wmlnjevbfodamyiqpucrhsukg
