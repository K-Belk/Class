
const pa = require('./padArray')
const pad = pa.pad

test('[1,2,3], 5 returns [1,2,3,null,null]', () => {
  expect(pad([1,2,3], 5)).toStrictEqual([1,2,3,null,null])
})

test('[1,2,3], 2 returns [1,2,3]', () => {
  expect(pad([1,2,3], 2)).toStrictEqual([1,2,3])
})

test('[1,2,3], 6, "dog" returns [1,2,3,"dog","dog","dog"]', () => {
  expect(pad([1,2,3], 6, "dog")).toStrictEqual([1,2,3,"dog","dog","dog"])
})

