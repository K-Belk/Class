const caesarCipher = (string, shiftAmount) => {
    string = string.split('')
    for (idx in string) {
        let charNum =  string[idx].charCodeAt(0) //  gives ascii number 
        let newNum = charNum + shiftAmount
        if (string[idx].match(/[a-zA-Z]/)) {
          let zZ = String
          let aA = String
          if (string[idx].match(/[A-Z]/) )   {
              aA = 'A'
              zZ = 'Z'              
            } else if (string[idx].match(/[a-z]/)){
              aA = 'a'
              zZ = 'z'              
            }
            z = zZ.charCodeAt(0)
            a = aA.charCodeAt(0)            
          if (newNum > z) {
            newNum = newNum - z + a - 1
          } else if (newNum < a) {
            newNum = z - (a - newNum)+ 1
          }
          string[idx] = String.fromCharCode(newNum)
      }
  }
    return string.join('')
  }


module.exports = {
  caesarCipher
}
