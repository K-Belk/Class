var sp = require("./sumPairs");
const sumPairs = sp.sumPairs

const deepEqual = require('deep-equal');;

console.log(deepEqual(sumPairs([1,2,3,4,5], 9), [[4,5]]))
console.log(deepEqual(sumPairs([1,2,3,4,5], 7), [[2,5], [3,4]]))
console.log(sumPairs([3, 1, 5, 8, 2], 27) == 'unable to find pairs')

