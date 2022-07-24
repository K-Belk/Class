const cm = require('./calculateMode')
const calculate_mode = cm.calculate_mode

test('[1,2,3,3] returns 3 ', () => {
  expect(calculate_mode([1,2,3,3])).toStrictEqual([3])
})

test('[4.5, 0, 0] returns [0]', () => {
  expect(calculate_mode([4.5, 0, 0])).toStrictEqual([0])
})

test('[1.5, -1, 1, 1.5] returns [1.5]', () => {
  expect(calculate_mode([1.5, -1, 1, 1.5])).toStrictEqual([1.5])
})

test('[1,1,2,2]) returns [1,2]', () => {
  expect(calculate_mode([1,1,2,2])).toStrictEqual([1,2])
})

test('[1,2,3]) returns [1,2,3]', () => {
  expect(calculate_mode([1,2,3])).toStrictEqual([1,2,3])
})

test('["who", "what", "where", "who"]) returns ["who"]', () => {
  expect(calculate_mode(["who", "what", "where", "who"])).toStrictEqual(["who"])
})