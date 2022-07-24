const checkCredit = (cardNumber)  => {
  let resultsSum = []
  for(let i = cardNumber.length - 1; i >= 0; i--) {
    if(i % 2 == 0) {
      let twoTimes = cardNumber[i] * 2
      if(twoTimes > 9) {
        twoTimes = String(twoTimes)
        resultsSum.push(Number(twoTimes[0]) + Number(twoTimes[1]))
      } else {resultsSum.push(twoTimes)}
    } else {
      resultsSum.push(Number(cardNumber[i]))
    }
  }
  resultsSum = resultsSum.reduce((a,b) => {return a + b})
  if(resultsSum % 10 == 0) {
    return "The number is valid!"
  } else{
    return "The number is invalid!"
  }
}

console.log(checkCredit('5541808923795240'))

module.exports = {
  checkCredit
}
