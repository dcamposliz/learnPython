# Exercise 25: Even More Practice

# This code is to be imported instead of just executed

# --- TODO: write instructions on how to import this thing!

#------------------------------------------------------------------

# we use the `def` keyword to define our own functions
def break_words(stuff):
	# we use the """to tell ourselves what the function does""".
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
	# this essentially creates an array

#------------------------------------------------------------------

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

#------------------------------------------------------------------

def print_first_word(words):
	"""Prints the first words after popping it off."""
	word = words.pop(0)
	print word

#------------------------------------------------------------------

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

#------------------------------------------------------------------

# here we are calling two functions we defined earlier:
#
#		 `break_words()` --- which we are using to split or words
# and
#		`sort_words()` --- which we are using to sort our words
#
# woo!

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

#------------------------------------------------------------------

def print_first_and_last(sentence):
	"""Prints the first and last words and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

#------------------------------------------------------------------

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last ones"""
	words = sort_sentence(sentence) # `sort_sentence()` breaks and sorts
	print_first_word(words)
	print_last_word(words)
