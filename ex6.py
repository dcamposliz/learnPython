#assigns string value to variable "x"
x = "There are %d types of people." % 10

#assigns string value to variable "binary"
binary = "binary"

#assigns string value to variable "don't"
do_not = "don't"

#assigns string value to variable "y", which is a function of two other variables previously defined
y = "Those who know %s and those who %s." % (binary, do_not)

#prints string defined as x
print x

#prints string defined as y
print y

#prints random string (which is also a function of "x", we also say that this takes in "x". not sure about the right way of "saying" this, at least in this context)
print "I said: %r." % x

#prints random string (which is also a function of "y", we also say that this takes in "y".)
print "I also said: '%s'. " % y

#defines variable "hilarious" as boolean, which takes value "false"
hilarious = False

#defines variable "joke_evaluation" as a string that takes in another string to be printed - which has not been perfectly defined yet
joke_evaluation = "Isn't that joke so funny?! %r"

#prints the string "joke_evaluation" which takes in the value "false" of the variable hilarious
print joke_evaluation % hilarious



w = "This is the left side of..."

e = "a string with the right side."


print w + e

# do %r count as strings? or only %s? along the same stream of thought, are there four or five strings inside of strings in this thing?