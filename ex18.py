# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

	#we are defining a functions above. 
	#functions do three things:
	# 1 - they name pieces of code the same way that 
	#     variables name strings and numbers
	# 2 - they take arguments the way your scripts take argv
	# 3 - using 1 and 2 they let you make your own "mini-scripts"
	#     or "tiny commands"

# ok, that *args is actually pointless, we can just the following:

#	below we are defining a function, which takes two parameters
#	(which have not been defined yet, or do not have to be)
#	we also define what the function does, which is print a string
#	which incorporates the arguments inputed by the user
#	when executing the function
def print_two_again(arg1, arg2):
	print "arg1: %r. arg2: %r" % (arg1, arg2)

# this one just takes one argument

#	below we are defining a function, which takes one parameter
#	(which has not been defined yet, or does not have to be)
#	we also define what the function does, which is print a string
#	which incorporates the argument inputed by the user
#	when executing the function
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments

# 	below we are defining a function, which takes no parameters
#	we also define what the function does, which is print a string
#	and that's it

def print_none():
	print "I got nothin'."

#	now we are actually executing the functions we defined earlier
#	and we are handing them parameters, or arguments

print_two("David","Campos")
print_two_again("David","Campos")
print_one("First!")
print_none()

#-----------------------------------------------------#

# BREAKING THINGS AND STUFF !!

print_two("Aaron", 'middlename')
print_two(3, "Daniel")

# we are defining another function, and 'proving' that the arguments
# first, last, and age do not have to be 'defined'
# do we consider these 'argumets to be variables?'

def print_personal(first, last, age):
	print "Hi! I am %s %s, and I am %r years old." % (first, last, age)

print_personal("David", "Campos", 25)

#-----------------------------------------------------#

