const palindrome = (word) => {
  
  word = String(word).toLowerCase().replace(/[^a-z0-9]/g, '')

  return word == word.split('').reverse().join('')

};



module.exports = {
  palindrome
}