// Can you translate this driver code to unit tests?

var ana = require("./characterMatch");
const isCharacterMatch = ana.isCharacterMatch

console.log(isCharacterMatch('charm', 'march') === true);
console.log(isCharacterMatch('zach', 'attack') === false);
console.log(isCharacterMatch('CharM', 'mARcH') === true);
console.log(isCharacterMatch('abcde2', 'c2abed') === true);

console.log("This test is for the challenge quesiton");
console.log(isCharacterMatch('Anna Madrigal', 'A man and a girl') === true);
