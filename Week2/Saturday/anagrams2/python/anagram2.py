# Don't forget to run the tests (and create some of your own)

import re

def is_character_match(string1, string2):
	regex = "[\W]"
	string1 = re.sub(regex,'', string1.lower())
	string2 = re.sub(regex,'', string2.lower())
	if len(string1) == len(string2):
		pos = 0
		while pos <= len(string1) - 1:
			if string2[pos] in string1:
				string1 = string1.replace(string2[pos], ' ', 1)
				string2 = string2.replace(string2[pos], ' ', 1)
			pos += 1
	return True if string1 == string2 else False



def anagrams_for(word, list_of_words):
	matches = []
	for i in list_of_words:
		if is_character_match(word, i) == True:
			matches.append(i)
	return matches

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

