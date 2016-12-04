#again, we are plugging in argv from the module sys
from sys import argv

#again, assigning 'value' argv to variables script and filename
script, filename = argv

#printing stuff
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#running method raw_input, which asks user for input given the questions asked above
raw_input("?")
#the method above literally waits for the user to 'continue' by pressing 
#ENTER so that the rest of the script is executed


#printing some shit
print "Opening the file..."
#defining variable 'target' and assigning method 'open', which takes parameters 'filename' and 'w'
#we previously defined 'filename' to be a function of user input
#i have no idea what 'w' is, however :(
#actually, w stands for the mode in which the file is opened, which is 'write'
#analogously, r stands for 'read', and a stands for 'append'
#does this mean that open always uses two parameters?
#well, according to the python documentation, the following is the standard format for 'calling' the open method
	# open(name[,mode[,buffering]])
		# the buffer argument option specifies the file's buffer size - which is another google away, but im gonna stay focused for now
target = open(filename, 'w')

#we print!
print "Truncating the file. Goodbye!"
#we run our 'function' target, which opens file with given two arguments
#and truncates some stuff...
target.truncate()

#we print more stuff
print "Now I'm going to ask you for three lines."

#set some variables equal to some raw input that user provides
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#print stuff
print "I'm going to write these to the file."

#run write method on top of target variable (given two parameters)
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#this literally has the user re-write the entirety of the text of the
#file in custody

#then we tell the user we're closing the file
print "And finally, we close it."
target.close()
#then we close the file in custody