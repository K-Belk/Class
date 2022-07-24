


  const conversionTableLazy = [
    {decimal: 1000, roman: 'M'},
    {decimal: 500, roman: 'D'},
    {decimal: 100, roman: 'C'},
    {decimal: 50, roman: 'L'},
    {decimal: 10, roman: 'X'},
    {decimal: 5, roman: 'V'},
    {decimal: 1, roman: 'I'}    
  ]

const toRomansLazy = (num) => {
  
  let romanNumResult = ""

  for(let i = 0; i < conversionTableLazy.length; i++) {

    // how many times it is divisible by the decimal
    let divisibleBy  =  Math.floor(num / conversionTableLazy[i].decimal)

    // changes the num to the remainder 
    num = num % conversionTableLazy[i].decimal
  
    for(let j = 0; j < divisibleBy; j++) {

      romanNumResult += conversionTableLazy[i].roman
    }
  }
  
  return romanNumResult
}


const conversionTableModern = [
  {decimal: 1000, roman: 'M'},
  {decimal: 900, roman: 'CM'},
  {decimal: 500, roman: 'D'},
  {decimal: 400, roman: 'CD'},
  {decimal: 100, roman: 'C'},
  {decimal: 90, roman: 'XC'},
  {decimal: 50, roman: 'L'},
  {decimal: 40, roman: 'XL'},
  {decimal: 10, roman: 'X'},
  {decimal: 9, roman: 'IX'},
  {decimal: 5, roman: 'V'},
  {decimal: 4, roman: 'IV'},
  {decimal: 1, roman: 'I'}    
]

const toRomansModern = (num) => {
  let romanNumResult = ""

  for(let i = 0; i < conversionTableModern.length; i++) {

    // how many times it is divisible by the decimal
    let divisibleBy  =  Math.floor(num / conversionTableModern[i].decimal)

    // changes the num to the remainder 
    num = num % conversionTableModern[i].decimal
  
    for(let j = 0; j < divisibleBy; j++) {

      romanNumResult += conversionTableModern[i].roman
    }
  }
  
  return romanNumResult
}

// console.log(toRomansLazy(501))

module.exports = {
  toRomansLazy,
  toRomansModern
}