
# defining a function that adds two arguments and
# then prints the operations being carried out
# and returns the solution :)
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
# same for subtraction
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
# same for multiplication
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
# same for division
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
# printing random string!
print "Let's do some math with just functions!"

# now we are declaring some variables to be equal to
# the output of our defined functions above
# as a function of specified parameters/arguments
age = add(20, 5)
height = subtract(74, 4)
weight = multiply(5, 14)
iq = divide(100, 2)

# now we are printing a string that takes
# the values of the variables we just declared
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# now we are taking into consideration order of operations
# as it relates to how we write this kind of stuff
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "\nCan you do the puzzle by hand?"
