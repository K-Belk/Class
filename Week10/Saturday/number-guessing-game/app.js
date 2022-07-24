console.log("HELLO CHARLIE PLATOON!")

const container = document.querySelector(".container")


const getRandomNumber = () => {
  return Math.floor(Math.random() * 101)
}

let randomNumber = getRandomNumber()

const guessing = () => {
  const guess = document.getElementById('number_input')
  results = checkGuess(guess.value)
  console.log(results)
  storeNumber(guess.value, results)
  return(guess.value)
}

const checkGuess = (guess) => {
  if (guess > randomNumber) {
    return 'Lower'
  } else if (guess < randomNumber) {
    return 'Higher'
  } else {
    return 'Winner'
  }
}

const storeNumber = (num, results) => {
  const outerDiv = document.createElement('div')
  outerDiv.className = 'guesses'
  container.appendChild(outerDiv)
  const divNum = document.createElement('div')
  divNum.innerText = num
  const divRes = document.createElement('div')
  divRes.innerText = results
  outerDiv.appendChild(divNum)
  outerDiv.appendChild(divRes)
}