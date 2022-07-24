import re

def char_count(str):
  str = re.sub("\W", '', str)
  result = {}
  for char in str:
    if char in result:
      result[char] += 1
    else:
      result[char] = 1
  return result
