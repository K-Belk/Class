var char = require("./charCount");

test(" 'aaabbc' contains 3 a's ", () => {
  expect(char.charCount("aaabbc")['a']).toBe(3)
})

test(" 'aaabbc' contains 2 b's ", () => {
  expect(char.charCount("aaabbc")['b']).toBe(2)
})

test(" 'aaabbc' contains 1 c ", () => {
  expect(char.charCount("aaabbc")['c']).toBe(1)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 6 a's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['a']).toBe(6)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 4 e's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['e']).toBe(4)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 3 l's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['l']).toBe(3)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 3 p's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['p']).toBe(3)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 2 w's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['w']).toBe(2)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 2 d's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['d']).toBe(2)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 2 o's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['o']).toBe(2)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 2 t's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['t']).toBe(2)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 2 y's ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['y']).toBe(2)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 1 k ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['k']).toBe(1)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 1 h ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['h']).toBe(1)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 1 i ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['i']).toBe(1)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 1 c ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['c']).toBe(1)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 1 n ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['n']).toBe(1)
})

test(" 'rplyoacadawpettlleaodeeywapkniha' contains 1 r ", () => {
  expect(char.charCount('rplyoacadawpettlleaodeeywapkniha')['r']).toBe(1)
})