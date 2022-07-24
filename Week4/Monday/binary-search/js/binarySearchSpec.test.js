
const bs = require('./binarySearch')


var smallArray = [1,2,3,4,5]
var largeArray = [1,5,7,2,3,8,4,9]
largeArray.sort()

test(" Num 1 in small array is index 0", () => {
  expect(bs.binarySearch(1, smallArray)).toBe(0)
})

test(" Num 2 in small array is index 1", () => {
  expect(bs.binarySearch(2, smallArray)).toBe(1)
})

test(" Num 3 in small array is index 2", () => {
  expect(bs.binarySearch(3, smallArray)).toBe(2)
})

test(" Num 4 in small array is index 3", () => {
  expect(bs.binarySearch(4, smallArray)).toBe(3)
})

test(" Num 5 in small array is index 4", () => {
  expect(bs.binarySearch(5, smallArray)).toBe(4)
})

test(" Num 7 in large array is index 5", () => {
  expect(bs.binarySearch(7, largeArray)).toBe(5)
})

test(" Num 6 is not in large array", () => {
  expect(bs.binarySearch(6, largeArray)).toBe(-1)
})
