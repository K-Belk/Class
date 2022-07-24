import re



def translate(word_or_phrase):
  vowel = "[aeiou]"
  qu = 'qu'
  words = re.split("[\s]", word_or_phrase)
  # print(words)
  for idx in (range(len(words))):
      if re.match("[a-zA-Z]", words[idx]):
        # checks if word starts with 'qu' and sets the index position to the end of the 'qu'
        if re.search(qu,words[idx].lower()):
          q = re.search(qu,words[idx].lower())
          idx_change = q.end()
        # checks if for the first vowel and sets the index position
        elif re.search(vowel,words[idx].lower()):
          m = re.search(vowel,words[idx].lower())
          idx_change = m.start()
        # if the word starts with a vowel then just ad 'ay' to the end

        if idx_change == 0:
          words[idx] += 'ay'
        # finds the first vowel and takes all the letters before and moves them to the end then adds 'ay' to the end
        else:
          if words[idx][0].isupper():
            # if first letter is upper case then it lowers the original first and uppers the new first 
            words[idx] = words[idx][idx_change].upper() + words[idx][idx_change+1::] + words[idx][:idx_change].lower() + 'ay'
          else:
            words[idx] = words[idx][idx_change::] + words[idx][:idx_change] + 'ay'

  return ' '.join(words)


print(translate("Hi, I'm Zach")) # => Ihay, I'may Achzay

# print(translate("Hi, I'm Zach.\nHow are you?"))
# => Ihay, I'may Achzay.
# => Owhay areway ouyay?