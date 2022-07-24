
const isCharacterMatch = (string1, string2) => {
  let regex = /[^a-z0-9]/g
  string1 =string1.toLowerCase().replace(regex, '')
  string2 =string2.toLowerCase().replace(regex, '')
  if( string1.length == string2.length){
    let pos = 0
    while(pos <= string1.length){
      if(string1.includes(string2[pos])){
        string1 = string1.replace(string2[pos], ' ')
        string2 = string2.replace(string2[pos], ' ')
      }
      pos++
    }    
    return string1 == string2 ? true:false
  } 
    return false
  
}

module.exports = {
  isCharacterMatch
}
