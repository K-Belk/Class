def anagram_for(word, list_of_words)
  matches = []
  word = word.downcase.chars.sort.join
  for i in list_of_words do
    sorted = i.downcase.chars.sort.join
    if sorted == word
      matches.append(i)
    end
  end
  return matches
end