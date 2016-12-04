# python3
# python3.re

	# source: https://www.tutorialspoint.com/python/python_reg_expressions.htm

"""
	A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions (RegEx) are widely used in UNIX.

	The module `re` provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression.

	There are various characters that have special meanings when used in regular expressions. To avoid any confusion, we will use Raw Strings as:

		r'expression'
"""

###########################################################
# The Match Function
###########################################################
print("\n-----{ The Match Function }-----\n")
"""
	Syntax:

		re.match(pattern, string, flags=0)

	Where:

		pattern:

			This is the regular expression to be matched.

		string:

			This is the string, which would be searched to match the pattern at the beginning of string.

		flags:

			You can specify different flags using bitwise OR (|). These are modifiers, which are listed below.

	The `re.match` returns object on success, None on failure. We use the following functions of match object to get matched expression.

		group(num = 0)

			This methid returns entire match (or specific subgroup num)

		groups()

			This method returns all matching subgroups in a tuple (empty if there weren't any)
"""

import re

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
	print("matchObj.group() : ", matchObj.group()) # why does this output the whole thing?
	print("matchObj.group(1) : ", matchObj.group(1)) # why does this output the first word?
	print("matchObj.group(2) : ", matchObj.group(2)) # why does this output the third word?	
	# print("matchObj.group(3) : ", matchObj.group(3)) # this throws an error
else:
	print("No match!")
"""
	Above, in:

		matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

		r'(.*) are (.*?) .*' = pattern

		line = string

		flags = re.M|re.I

	Still confused about the characters used in the pattern.
"""
###########################################################
# Matching Versus Searching
###########################################################
print("\n-----{ Matching Versus Searching }-----\n")
"""
	Python offers two different primitive operations based on regular expressions: match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string.
"""
# import re

line = "Cats are smarter than dogs"
matchObj = re.match( r'dogs', line, re.M|re.I)

if matchObj:
	print("match --> matchObj.group() : ", matchObj.group())
else:
	print("No match!!")

searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
	print("search --> searchObj.group() : ", searchObj.group())
else:
	print("Nothing found!!")

###########################################################
# Search and Replace
###########################################################
print("\n-----{ Search and Replace }-----\n")
"""
	One of the most important re methods that use regular expressions is sub.

	Syntax:

		re.sub(pattern, repl, string, max=0)

	This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max provided. This method returns modified string.
"""

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num:", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)

###########################################################
# Regular Expression Modifiers: Option Flag
###########################################################
"""
	Regular expression literals may include an optional modifier to control various aspects of matching. The mofidiers are specified as an optional flag. You can provide multiple modifiers using exclusive OR (|), as shown previously and may be represented by one of these:

		re.I

			Performs case-insensitive matching.

		re.L

			Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior (\b and \B).

		re.M

			Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).

		re.S

			Makes a period (dot) match any character, including a newline.

		re.U

			Internprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.

		re.X

			Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.
"""
###########################################################
# Regular Expression Patterns
###########################################################
"""
	All characters match themselves except for control characters.

	Control characters include:

		+

		?

		.

		*

		^

		$

		(

		)

		[

		]

		{

		}

		|

		\

		)

	The following lists the regular expression syntax that is available in Python:

		^
			Matches the beginning of line.

		$
			Matches the beginning of line.

		.
			Matches any single character excepct newline. Using m option allows it to match newline as well.

		[...]

			Matches any single character in brackets. For example, [abc] matches the first instance of a, b, or c found in a string.

		[^...]

			Matches any single character not in brackets.

		re*

			Matches 0 or more occurrences of preceding expression.

		re+

			Matches 1 or more occurences of preceding expression.

		re?

			Matches 0 or 1 occurrences of preceding expression.

		re{ n}

			Matches exactly n number of occurrences of preceding expression.

		re{ n, m}

			Matches at least n and at most m occurrences of preceding expression.

		a| b

			Matches either a or b.

		(re)

			Groups regular expressions and remembers matched text.

		(?imx)

			Temporarily toggles on i, m, or x options within a regular expression. If in parenthesis, only that area is affected.

		(?-imx)

			Temporarily toggles off i, m, or x options within a regular expression. If in parenthesis, only that area is affected.

		(?#...)

			Comment

		(?= re)

			Specifies position using a pattern. Doesn't have a range.

		(?! re)

			Specifies position using pattern negation. Doesn't have a range.

		(?> re)

			Matches independent pattern without backtracking

		\w

			Matches word characters.

		\W
		
			Matches nonword characters.

		\s

			Matches whitespace. Equivalent to [\t\n\r\f].

		\S

			Matches non-whitespace.

		\d
			Matches digits. Equivalent to [0-9].

		\D

			Matches non-digits.

		\A
			Matches beginning of string.

		\Z
			Matches end of string. If a newline exists, it matches just before newline.

		\z

			Matches end of string.

		\G

			Matches point where last match finished.

		\b

			Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.

		\B

			Matches nonword boundaries.

		\n, \t, etc

			Matches nth grouped subexpression.

		\10

			Matches nth grouped subexpression if it matches already. Otherwise refers to the octal representation of a character code.
"""

###########################################################
# Regular Expression Examples
###########################################################
"""
	Literal characters:

		python

			matches "python", for example
"""

###########################################################
# Regular Expression Examples
###########################################################
"""
	Character classes

		[Pp]ython

			matches "Python" or "python"

		rub[ye]

			matches "ruby" or "rube"

		[aeiou]

			matches any lowercase vowel

		[0-9]

			same as [0123456789], matches any digit

		[a-z]

			matches any lowecase ASCII letter

		[A-Z]

			matches any uppercase ASCII letter

		[a-zA-Z0-9]

			matches any lowercase or uppercase ASCII letter, as well as any digit

		[^aeiou]

			matches anything other than a lowercase vowel

		[^0-9]

			matches anything other than a digit
"""
###########################################################
# Special Character Classes
###########################################################
"""
		.	

			matches any character except newline

		\d	

			matches a digit: [0-9]

		\D	

			matches a nondigit: [^0-9]

		\s	

			matches a whitespace character: [ \t\r\n\f]

		\S	

			matches nonwhitespace: [^ \t\r\n\f]

		\w	

			matches a single word character: [A-Za-z0-9_]

		\W	

			matches a nonword character: [^A-Za-z0-9_]

"""
###########################################################
# Repetition Cases
###########################################################
"""
		ruby?

			matches "rub" or "ruby": they y is optional

		ruby*

			matches "rub" plus 0 or more ys

		ruby+

			matches "rub" plus 1 or more ys

		\d{3}

			matches exactly 3 digits

		\d{3,}

			matches 3 or more digits
		
		\d{3,5}

			matches 3, 4, or 5 digits
"""
###########################################################
# Nongreedy Repetition
###########################################################
"""
	This matches the smallest number of repetitions:

		<.*>

			greedy repetition/
"""






 