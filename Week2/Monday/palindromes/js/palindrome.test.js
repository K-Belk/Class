const pal = require("./palindrome")
const palindrome = pal.palindrome

test('racecar is a palindrome', () => {
  expect(palindrome('racecar')).toBe(true);
});

test('Noon is a palindrome', () => {
  expect(palindrome('Noon')).toBe(true);
});

test('ciVic is a palindrome', () => {
  expect(palindrome('ciVic')).toBe(true);
});

test('nice is a palindrome', () => {
  expect(palindrome('nice')).toBe(false);
});

test('434 is a palindrome', () => {
  expect(palindrome(434)).toBe(true);
});

test('123 is a palindrome', () => {
  expect(palindrome(123)).toBe(false);
});

test('"Sore was I ere I saw Eros." is a palindrome', () => {
  expect(palindrome("Sore was I ere I saw Eros.")).toBe(true);
});
test('"A man, a plan, a canal -- Panama" is a palindrome', () => {
  expect(palindrome("A man, a plan, a canal -- Panama")).toBe(true);
});