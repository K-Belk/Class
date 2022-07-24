
const r = require('./recursionChallenge')

test('factorial of 4 is 24', () => {
  expect(r.factorial(4)).toBe(24)
})

test('tacocat is a palindrome', () => {
  expect(r.palindrome('tacocat')).toBe(true)
})

test('roman numeral of 944 is CMXLIV', () => {
  expect(r.romanNum(944)).toBe('CMXLIV')
})