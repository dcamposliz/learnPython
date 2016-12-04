# once again, importing argv from module sys
from sys import argv

# assigning value of argv to variables script, and input_file
script, input_file = argv

# define function called print_all, which takes in parameter f
# which, f is a variable that stores a file
# and the function altogether reads the file f, and prints it
def print_all(f):
	print f.read()

# ??? f has not been defined. why then can f be used here?
# ??? is f default for file if it has not been defined as 
# something different?

# define function called rewind, which takes in parameter f (which, we have not defined yet)
# which, f is a variable that stores a file 
# and the function altogether seeks a particular part of the file f,
# which, since it takes parameter zero, makes it go to the beginning 
# of the file
def rewind(f):
	f.seek(0)

# define function called print_a_line
# which takes in parameters line_count and f
# line_count seems to be python-original method **** FIX: I THINK IT ACTUALLY IS NOT PYTHON ORIGINAL ****
# and so is readline
def print_a_line(line_count, f):
	print line_count, f.readline()

# we define a variable current_file to be the open method
# on the variable input_file, which takes argv (as it can be seen earlier in the code)
current_file = open(input_file)

# then we print a random string
print "First let's print the whole file:\n"

# then we run our function print_all, and pass it 'current_file' as f
print_all(current_file)
# this means that our function will read the file we passed it, and then print it

# then we print a random string
print "Now let's rewind, kind of like a tape."

#then we run our rewind function, to which we pass current_file as well
rewind(current_file)
# this means we go to position zero of the file

# then we print another random string to the user
print "Let's print three lines:"

# we define a variable current_line to be equal to 1
# and then run our print_a_line function by passing it
# our current_line variable for the line_count parameter
# and passing it current_file for the parameter f
#	recall that current_file is opens the input_file,
#	and the input file is handed to the script during execution
#	as an argv

current_line = 1
print_a_line(current_line, current_file)

# for this line we just iterate

current_line = current_line + 1
print_a_line(current_line, current_file)

# for this line we just iterate

current_line = current_line + 1
print_a_line(current_line, current_file)