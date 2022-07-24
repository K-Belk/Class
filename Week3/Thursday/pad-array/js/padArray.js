

/** 
 * If length of the array is > minSize then
 * take the difference between the length and minSize and push on that many of the value
 * If the length of array is <= the min size then
 * return array
 */
const pad = (array, minSize, value = null) => {
  let results = array
  if (array.length < minSize) {
    sizeDifference = minSize - array.length
    for (let i = 0; sizeDifference > i; i++){
      results.push(value)
    }
  }
  return results
}

// console.log(pad([1,2,3], 5))

module.exports = {
  pad
}