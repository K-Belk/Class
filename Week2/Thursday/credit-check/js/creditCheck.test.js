
var cc = require("./creditCheck");
const checkCredit = cc.checkCredit

test('Card number 5541808923795240 is valid', () => {
  expect(checkCredit('5541808923795240')).toBe("The number is valid!")
})

test('Card number 4024007136512380 is valid', () => {
  expect(checkCredit('4024007136512380')).toBe("The number is valid!")
})

test('Card number 6011797668867828 is valid', () => {
  expect(checkCredit('6011797668867828')).toBe("The number is valid!")
})

test('Card number 5541801923795240 is invalid', () => {
  expect(checkCredit('5541801923795240')).toBe("The number is invalid!")
})

test('Card number 4024007106512380 is invalid', () => {
  expect(checkCredit('4024007106512380')).toBe("The number is invalid!")
})

test('Card number 6011797668868728 is invalid', () => {
  expect(checkCredit('6011797668868728')).toBe("The number is invalid!")
})