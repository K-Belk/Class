const calculate_mode = (arrayIn) => {
  let counted = {}
  for (value of arrayIn){
    if(value in counted){
      counted[value]++
    } else {
      counted[value] = 1
    }
  }
  let countedArray = Object.entries(counted)
  let sortedArray = countedArray.sort((a,b) => b[1] - a[1])
  let results = []
  let maxNum = 0
  for (count of sortedArray){
    if (count[1] >= maxNum){
      if ((/[0-9]/).test(count[0])) {
        results.push(Number(count[0]))
      } else {
        results.push(count[0])
      }
      maxNum = count[1]
    }
  }
  return results
}

module.exports = {
  calculate_mode
}