const picker = prices => {
  let days = [0,0]
  let profit = 0
  for (let i = prices.length - 1; i >= 0 ; i--) {
      for (let j = 0; j < i; j++) {
        if ((prices[i] - prices[j]) > profit) {
          profit = prices[i] - prices[j]
          days[0] = j
          days[1] = i
        }
      }
    }
  return days

}


module.exports = {
    picker
}