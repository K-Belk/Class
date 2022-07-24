var rn = require("./romanNumerals");

const romansLazy = rn.toRomansLazy
const romansModern = rn.toRomansModern

console.log(romansLazy(1) === 'I');
console.log(romansLazy(3) === 'III');
console.log(romansLazy(4) === 'IIII');


console.log(romansModern(4) === 'IV')
console.log(romansModern(944) === 'CMXLIV')
console.log(romansModern(150) === 'CL')