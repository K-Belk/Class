var fact = require("./factorial");

const factor = fact.factorial

console.log(factor(8) === 40320n);
console.log(factor(18) === 6402373705728000n);
console.log(factor(45) === 119622220865480194561963161495657715064383733760000000000n);
// Test how high of a number your program can calculate. Can you push it further?
