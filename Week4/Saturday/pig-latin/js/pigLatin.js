const translate = (word) => {

  let vowel= /[aeiou]/g
  let qu = /qu/g   
  let words = word.split(' ')
  for (idx in words) {
    if (words[idx].search(qu) >= 0) {
      pos = words[idx].search(qu) + 2
    }
    else if (words[idx].search(vowel) >= 0) {
      pos = words[idx].search(vowel)
    }
    if (pos == 0) {
      words[idx] = words[idx].concat('ay')
    }
    else { 
      if (words[idx][0] == words[idx][0].toUpperCase()) {
              first = words[idx].slice(0, pos).toLowerCase()
              last = words[idx].slice(pos, words[idx].length)
              newFirst = last[0].toUpperCase()
              words[idx] = newFirst.concat(last, first, 'ay')
        } else {
          first = words[idx].slice(0, pos)
          last = words[idx].slice(pos, words[idx].length)
          words[idx] = last.concat(first, 'ay')
      }
    }
  }
  return words.join(' ')
}; 



module.exports = {
  translate
}
