import re

def caesar_cipher(string, shift_amount):
    # split string into a list
    split_string = list(string)
    # iterate over the list
    for idx, val in enumerate(split_string):
        # get the ASCII value of the charater 
        charNum = ord(val)
        # Shift the ASCII value 
        newNum = (charNum + shift_amount)
        # if it is a capital letter
        if re.match("[A-Z]", val):
            # if new ASCII value is greater than Z's wrap around to A
            if newNum > ord('Z'):
                newNum = (newNum - ord('Z') + ord('A') - 1)
            # if new ASCII value is lowere than A's wrap around to Z
            elif newNum < ord('A'):
                newNum = ord('Z') - (ord('A') - newNum) + 1
            # set the value to the new charater
            split_string[idx] = chr(newNum)
        # if it is a lower case letter
        elif re.match("[a-z]", val):
            #  if the ASCII value is greater than z's then wrap around to a
            if newNum > ord('z'):
                newNum = (newNum - ord('z') + ord('a') - 1)
            #  if the ASCII value is lower than a's then wrap around to z
            elif newNum < ord('a'):
                newNum = ord('z') - (ord('a') - newNum) + 1
            # set the value to the new charater
            split_string[idx] = chr(newNum)
    # return the joined list as a string
    return ''.join(split_string)

print(caesar_cipher("zZ", 1)) # aA
print(caesar_cipher("aA", -1)) # zZ