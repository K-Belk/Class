const factorial = (num) => {

  let result = BigInt(1)
  for(let i = 1; i <= num; i++) {
    let bigInt = BigInt(i)
    result *= bigInt
  }
  return result
};


 module.exports = {
   factorial
 }