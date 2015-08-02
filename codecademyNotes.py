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

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# now my question is, do we need to import raw_input from any module?
# or, loosely speaking, is it inherent?

my_string = "This is an awesome string!"
print len(my_string)
print my_string.upper()

#-----------------------------------------#


#----DATE AND TIME

'''
	
'''

from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day


from datetime import datetime
now = datetime.now()
print '%s/%s/%s' % (now.month, now.day, now.year)


from datetime import datetime
now = datetime.now()
print '%s:%s:%s' % (now.hour, now.minute, now.second)


from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)


#-----------------------------------------#


#----CONDITIONALS & CONTROL FLOW

'''
	
'''

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

#-----------------------------------------#


#----DATE AND TIME

'''
	
'''