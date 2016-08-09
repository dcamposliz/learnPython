
#imports argv from module sys
from sys import argv

#assigns argv to script and filename
script, filename = argv

#we assing the method open to the variable function txt,
#to which we pass the argument or parameter filename,
#i am not sure if open only works for txt files, i'd be 
#surprised if it did
txt = open(filename)

#we tell the user the name of the file that is being opened
#in this case, the name of the file is an argument that
#has been passed by the user, and that is assumed to exist
#within the same directory as the script?
print "Here's your file %r:" % filename
#we print the contents of the txt file mentioned
print txt.read()

#we ask the user to pass the script the name of the file
#that he wants to print (both metadata & contents)
print "Type the filename again:"
#we assign the value of the user's input to the variable 
#file_again
#basically what we are doing is enabling the user to open
#the file in two different ways, FIRST by initially passing 
#name of the file to the script through argv
#and SECOND by using raw_input
file_again = raw_input("> ")
#then we create a function txt_again that uses the methon
#open, as a function of the argument stored in file_again
txt_again = open(file_again)

#we print the contents of the file that was passed to 
#the script from the user
print txt_again.read()

