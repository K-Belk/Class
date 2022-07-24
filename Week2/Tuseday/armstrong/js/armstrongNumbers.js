// How can you make this more scalable and reusable later?

const findArmstrongNumbers = (array) => {

  let armstrongNumbers = []
  for(num in array) {
    let checkResults = armstrongCheck(array[num])
    if(checkResults != null) {
      armstrongNumbers.push(checkResults)
    }
  } return armstrongNumbers
};

const intToArray = (int) => {
  return String(int).split('')
}

const armstrongCheck = (num) => {
  
  let array = intToArray(num)
  let length = array.length
  let armstrong = 0
  for(int in array){
    armstrong += Number(array[int])**length
  }
  return (armstrong == num ? armstrong:null)
}

console.log(findArmstrongNumbers([10, 120, 3, 153]))

module.exports = {
  findArmstrongNumbers
}
