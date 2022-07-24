const an = require("./armstrongNumbers");
const findArmstrongNumbers = an.findArmstrongNumbers

function createArrayOfNum(maxValue) {
  return Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

test('Input of 0 should return 0', () => {
  expect(findArmstrongNumbers([0])).toStrictEqual([0]);
});

test('Input an array from 0 and 8 sequential  elements long should return an array from 0 to 7', () => {
  expect(findArmstrongNumbers(createArrayOfNum(8))).toStrictEqual([0, 1, 2, 3, 4, 5, 6, 7]);
});

test('Input an array from 0 and 99 sequential  elements long should return an array from 0 to 9', () => {
  expect(findArmstrongNumbers(createArrayOfNum(99))).toStrictEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
});


test('Input an array from 0 and 999 sequential  elements long should return an array from 0 to 9, 153, 370, 371, 407', () => {
  expect(findArmstrongNumbers(createArrayOfNum(999))).toStrictEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]);
});