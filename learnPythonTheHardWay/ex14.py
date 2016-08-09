#using command "from" to import ?function? argv
#from module "sys"

from sys import argv


#we assign three parameters to "argv"
script, user_name, age = argv
#and assign '> ' to the variable prompt
prompt = '> '

# then print a variety of shit that takes the 
# arguments we pass to the terminal when executing
# the script
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# we assign the input from the user to the variable likes
likes = raw_input(prompt)

# we assign the input from the user to the variable lives
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

# we assign the input from the user to the variable computer
print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)