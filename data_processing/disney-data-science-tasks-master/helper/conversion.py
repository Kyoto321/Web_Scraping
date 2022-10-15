import re

'''
https://github.com/KeithGalli/disney-data-science-tasks

whenever dealing with patterns import regex 
number = r"\d+" means one or more digits
\. = decimal place
* = zero numbers
\d* = zero or more numbers
rf" = two multiple syntax
\s = space character
| = or

'''
amounts = r"thousand|million|billion"	# word syntax
number = r"\d+(,\d{3})\.*\d*"	# number = 970 , 000 . 123

word_re = rf"\${number}(-|\sto\s)?({number})?\s({amounts})"
value_re = rf"\${number}"

'''

TODO

Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value

use test_money_conversion.py to test your solution
'''

def word_to_value(word):
	value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
	return value_dict[word]

def parse_word_syntax(string):
	value_string = re.search(number, string).group()
	value = float(value_string.replace(",", ""))
	word = re.search(amounts, string, flags=re.I).group().lower()
	word_value = word_to_value(word)
	return value*word_value

def parse_value_syntax(string):
	value_string = re.search(number, string).group()
	value = float(value_string.replace(",", ""))
	return value

	'''
	money_conversion("$12.2 million") --> 12200000 	## word syntax
	money_conversion("$790,000") --> 790000 	## value syntax
	'''

def money_conversion(money):

	if isinstance(money, list):
		money = money[0]

	word_syntax = re.search(word_re, money, flags=re.I)
	value_syntax = re.search(value_re, money)	## work based on the dollar sign

	if word_syntax:
		return parse_word_syntax(word_syntax.group())

	elif value_syntax:
		return parse_value_syntax(value_syntax.group())

print(money_conversion("$790 millions"))
