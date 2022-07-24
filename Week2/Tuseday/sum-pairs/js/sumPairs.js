const sumPairs = (array, sum) => {
  let result = []
  for(let i = 0; i <= array.length; i++){
    for(let j = i; j <= array.length; j++){
      if(array[i] + array[j] == sum) {
        result.push([array[i], array[j]])
      }
    }
  }
  if(result.length > 0){
    return result
  } else return 'unable to find pairs'
};

console.log(sumPairs([1,2,3,4,5], 7))

module.exports = {
  sumPairs
}