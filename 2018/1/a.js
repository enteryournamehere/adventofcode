const fs = require('fs');
let input = fs.readFileSync('./input.txt', {encoding: 'utf-8'});

console.log(eval('0' + input));

// 508
