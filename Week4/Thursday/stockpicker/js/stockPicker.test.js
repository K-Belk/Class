// run `npm install shallow-equal --save` in this folder before you get started with this challenge
// Rewrite this in Unit Test

var sp = require("./stockPicker");

test('most profitable is on days 1,4', () =>{
  expect(sp.picker([17,3,6,9,15,8,6,1,10])).toStrictEqual([1, 4])
})

test('most profitable is on days 0,4', () =>{
  expect(sp.picker([3,17,6,9,18,15,6,1,10])).toStrictEqual([0, 4])
})

test('most profitable is on days 0,8', () =>{
  expect(sp.picker([1,17,6,9,8,15,6,3,19])).toStrictEqual([0, 8])
})

test('most profitable is on days 2,5', () =>{
  expect(sp.picker([19,17,6,9,8,15,6,3,1])).toStrictEqual([2, 5])
})

