from math import floor
import re


class Recursive:
	"""
	Factoral - takes a integer and multiply it by one less of it's self repeatedly until it reaches 0
	>>> factorial(4) returns 24  = (4 * 3 * 2 * 1)

	Palindrome - takes in a string and returns True or False if it is the same forwards and backwards.

	>>> palindrome('tacocat') returns True

	Bottles - prints out the classic song '99 bottles of beer on the wall' but takes in a integer for where the song will start

	Roman Numerals - takes in an integer and returns the roman numeral equivlent.

	>>> roman_num(4) returns 'IV'
	"""

	def __init__(self) -> None:
		self.roman_conversion_table = [
		{'decimal': 1000, 'roman': 'M'},
		{'decimal': 900, 'roman': 'CM'},
		{'decimal': 500, 'roman': 'D'},
		{'decimal': 400, 'roman': 'CD'},
		{'decimal': 100, 'roman': 'C'},
		{'decimal': 90, 'roman': 'XC'},
		{'decimal': 50, 'roman': 'L'},
		{'decimal': 40, 'roman': 'XL'},
		{'decimal': 10, 'roman': 'X'},
		{'decimal': 9, 'roman': 'IX'},
		{'decimal': 5, 'roman': 'V'},
		{'decimal': 4, 'roman': 'IV'},
		{'decimal': 1, 'roman': 'I'}    
		]

	def factorial(self, x):
		"""
		Factoral - takes a integer and multiply it by one less of it's self repeatedly until it reaches 0
	>>> factorial(4) returns 24  = (4 * 3 * 2 * 1)
		"""
		if x <= 1:
			return 1
		else:
			return x * self.factorial(x-1)


	def palindrome(self, string):
		''' 
		calls clean_string
		then passes the clean string into palindrome to check if it is a palindrome and returns True or False
		'''
		clean = self.clean_string(string)
		return self.recursive_palindrome(clean)

	def clean_string(self, string):
		"""
		removes all whitespaces and punctuation
		"""
		return re.sub(r"[^a-zA-Z0-9]", '', str(string).lower())

	def recursive_palindrome(self, string):
		"""
		Returns True or False if the inputted string is the same forwards and backwards.
		"""
		length = len(string)
		if length == 1:
			return True
		elif string[0] != string[length-1]:
			return False
		else:
			return self.recursive_palindrome(string[1:-1])


	def bottles(self, num):
		"""
		Bottles - prints out the classic song '99 bottles of beer on the wall' but takes in a integer for where the song will start
		"""

		if num == 1:
			print(f"""Take one down and pass it around, no more bottles of beer on the wall.
	No more bottles of beer on the wall, no more bottles of beer.
	Go to the store and buy some more, 99 bottles of beer on the wall.""")
		else:
			print(f"""{num} bottles of beer on the wall, {num} bottles of beer. 
	Take one down and pass it around, {num-1} bottles of beer on the wall.""")
			return self.bottles(num-1)


	def roman_num(self, num, i=0):
		"""
		Roman Numerals - takes in an integer and returns the roman numeral equivlent.

	>>> roman_num(4) returns 'IV'
		"""
		
		if num == 0 or i == len(self.roman_conversion_table):
			return ''
		
		dec = self.roman_conversion_table[i].get('decimal')
		rom = self.roman_conversion_table[i].get('roman')
		divisible_by = floor(num/dec)
		
		
		if  divisible_by > 0:
			return (rom * divisible_by) + self.roman_num(num % dec, i+1 )

		else:
			return self.roman_num(num, i+1)
