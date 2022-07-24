var sp = require("./sumPairs");
const sumPairs = sp.sumPairs

test('Array [1,2,3,4,5] sum 9 pairs [4,5]', () => {
  expect(sumPairs([1,2,3,4,5], 9)).toEqual([[4,5]])
})

test('Array [1,2,3,4,5] sum 7 pairs [2,5], [3,4]]', () => {
  expect(sumPairs([1,2,3,4,5], 7)).toEqual([[2,5], [3,4]])
})

test("Array [3, 1, 5, 8, 2] sum 27 reruns  'unable to find pairs'", () => {
  expect(sumPairs([3, 1, 5, 8, 2], 27)).toBe('unable to find pairs')
})