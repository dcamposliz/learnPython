# once again importing argv from module sys
from sys import argv
#and importing exists from os.path
from os.path import exists

#setting a value of argv to the variables script, from_file, and to_file
script, from_file, to_file = argv
#this means the user needs to input the names of the files
# he is trying to mess in the same command when executing the script
# in the terminal

#printing a string that takes in two other strings
#namely, the names of the from_file, and to_file
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?

#now, giving in_file variable a value of open(from_file)
in_file = open(from_file)
#mearning that this variable is assigned the output from the method
#open, from the file from_file.
#interesting that we didn't specify the 'mode,' which means we
#are resorting to the default to the 'r' mode, for reading the file
#------
#now, setting another variable, which reads the opened from_file
#interesting to note that 'read' also takes in parameters, size,
#here is an example: fileObject.read( size );
#size in this case is the number of bytes to be read from the file 
indata = in_file.read()
#but the method above has no spefified size - what is the default?
#the entire size of the file?

#then we print out the length using leng() of the from_file
# notice that the size of from_file is exogenous at least
# in the scope of this code
# beyond that, i am assuming that len() returns a number data type
# since we are using %d to output the info within the string
print "The input file is %d bytes long" % len(indata)

#now we are asking the machine if the file that we are trying to 
#output to exists. This we do by pulling the method exists
#from the module os.path - which we mentioned earlier.
#exists() returns a boolean: true for exists and false for does not
#we 'force' print by using %r instead of say, %s
print "Does the output file exist? %r" % exists(to_file)

#now we pause the script by waiting for user input, aka ENTER pressing
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#we create a variable called out_file, which opens a to_file in write mode
out_file = open(to_file, 'w')
#then we run a write method on the file we opened, writing in what we

#read from the other file, with the indata variable
out_file.write(indata)

#then we print stuff
print "Alright, all done."

#then we close both input and output files
out_file.close()
in_file.close()