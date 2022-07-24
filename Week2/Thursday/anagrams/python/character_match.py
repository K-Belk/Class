# Don't forget to run your tests!
import re

def is_character_match(string1, string2):
	regex = r"[^a-zA-Z0-9]"
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


