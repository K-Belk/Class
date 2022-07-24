const charCount = (string) => {
  result = {}
  for(char of string) {
    if(result[char] > 0){
      result[char]++
    }else {
      result[char] = 1
    }
  }
  return result
  
};



module.exports = {
  charCount
}
