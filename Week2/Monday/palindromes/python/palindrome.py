import re

def palindrome(word):
    # converts to a string then removes all non letters and intergers
    word = re.sub(r"[^a-zA-Z0-9]", '', str(word).lower())
    
    return word == (word[::-1])

