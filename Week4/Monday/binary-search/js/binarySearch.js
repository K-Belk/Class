const findMiddle = (min, max) => {
  return Math.floor((min + max)/2)
}

const binarySearch = (num, arrOfNums, searchMin=0, searchMax=0) => {
  if (searchMin == 0){
    searchMin = arrOfNums[0]
  }
  if (searchMax == 0) {
    searchMax = arrOfNums[arrOfNums.length - 1] + 1
  }
  mid = findMiddle(searchMin, searchMax)


  if (arrOfNums.includes(num) == false){
    return -1
  } else if (num > mid) {
      return binarySearch(num, arrOfNums, mid, searchMax)
  } else if (num < mid) {
      return binarySearch(num, arrOfNums, searchMin, mid)
  } else if (num == mid) {
      return arrOfNums.indexOf(num)
  }

}

module.exports = {
  findMiddle,
  binarySearch
}
