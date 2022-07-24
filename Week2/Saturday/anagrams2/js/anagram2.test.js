var ana = require("./anagram2")

listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

test('threads should return a array with a length of 4', () => {
  expect(ana.anagramsFor('threads', listOfWords).length).toBe(4)
})

test('threads should return a array with index 0 being threads', () => {
  expect(ana.anagramsFor('threads', listOfWords)[0]).toBe("threads")
})

test('threads should return a array with index 1 being "trashed"', () => {
  expect(ana.anagramsFor('threads', listOfWords)[1]).toBe("trashed")
})

test('threads should return a array with index 2 being hardest', () => {
  expect(ana.anagramsFor('threads', listOfWords)[2]).toBe("hardest")
})

test('threads should return a array with index 3 being hatreds', () => {
  expect(ana.anagramsFor('threads', listOfWords)[3]).toBe("hatreds")
})

test('apple should return a array with a length of 0', () => {
  expect(ana.anagramsFor('apple', listOfWords).length).toBe(0)
})