#----PYTHON SYNTAX
'''

1. variables
2. datatypes
3. whitespace
4. comments
5. arithmetic operations

'''

#-----------------------------------------#


#----TIP CALCULATOR

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip
	
	#notice the interesting syntax when
	#telling the machine how many 'floats'
	#to print
print("\n")
print("TIP CALCULATOR STUFF:")

print("Cost of the meal, plus tax, plus tip is %.2f" % total)
print("\n")

#-----------------------------------------#


#----STRINGS & CONSOLE OUTPUT

'''
escaping characters are interesting
	\'
	\n
	what else?

each character in a string is indexed

Methods that use dot notation only work with strings.

String Concatenation

The % operator after a string is used to combine a 
string with variables. The % operator will replace a %s 
in the string with the string variable that comes after it.


'''

print("\n")
print("STRINGS and CONSOLE OUTPUT:")


fifth_letter = "MONTY"[4]
print(fifth_letter)
#assigns 'Y' to the variable fifth_letter

parrot = "Norwegian Blue"
print len(parrot)

parrot = "Norwegian Blue"
print parrot.lower()

parrot = "norwegian blue"
print parrot.upper()

pi = 3.14
print str(pi)

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

print "Spam " + "and " + "eggs"

print "The value of pi is around " + str(3.14)