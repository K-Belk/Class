

const factorial = (x) => {
  if (x <= 1){
    return 1
  } else {
    return x * factorial(x-1)
  }
};

const palindrome = (str) => {
  let clean = cleanString(str)
  return recursivePalindrome(clean)
};

const cleanString = (str) => {
  return String(str).toLowerCase().replace(/[^a-z0-9]/g, '')
}

const recursivePalindrome = (str) => {
  let length = str.length
  if (length == 1) {
    return true
  } else if (str[0] != str[length - 1]){
    return false
  } else {
    return recursivePalindrome(str.slice(1, length-1))
  }

}

const bottles = (num) => {
  if (num == 1) {
    return(`Take one down and pass it around, no more bottles of beer on the wall.
    No more bottles of beer on the wall, no more bottles of beer.
    Go to the store and buy some more, 99 bottles of beer on the wall.`)
  } else {
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer. 
    Take one down and pass it around, ${num-1} bottles of beer on the wall.`)
    return bottles(num-1)
  }
};

const romanConversionTable = [
  {'decimal': 1000, 'roman': 'M'},
  {'decimal': 900, 'roman': 'CM'},
  {'decimal': 500, 'roman': 'D'},
  {'decimal': 400, 'roman': 'CD'},
  {'decimal': 100, 'roman': 'C'},
  {'decimal': 90, 'roman': 'XC'},
  {'decimal': 50, 'roman': 'L'},
  {'decimal': 40, 'roman': 'XL'},
  {'decimal': 10, 'roman': 'X'},
  {'decimal': 9, 'roman': 'IX'},
  {'decimal': 5, 'roman': 'V'},
  {'decimal': 4, 'roman': 'IV'},
  {'decimal': 1, 'roman': 'I'}    
  ]

const romanNum = (num, i = 0) => {
  if (num == 0 || i == num.length) {
    return ''
  }
  let dec = romanConversionTable[i].decimal
  let rom = romanConversionTable[i].roman
  let divisibleBy = Math.floor(num/dec)

  if (divisibleBy > 0) {
    return (rom.repeat(divisibleBy)) + romanNum(num % dec, i + 1)
  } else {
    return romanNum(num, i + 1)
  }
};



// console.log(factorial(4))
// console.log(palindrome('tacocat'))
// console.log(bottles(3))
console.log(romanNum(13))
// console.log(romanConversionTable[0].decimal)


module.exports = {
  factorial,
  palindrome,
  bottles,
  romanNum
  
}