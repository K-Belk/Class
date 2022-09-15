def palindrome(word)
  word = word.to_s.downcase.gsub(/[^a-zA-Z0-9]/, '')
  return word == word.reverse
end