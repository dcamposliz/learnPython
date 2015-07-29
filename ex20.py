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

# define function called rewind, which takes in parameter f
# which, f is a variable that stores a file
# and the function altogether seeks a particular part of the file f,
# which, since it takes parameter zero, makes it go to the beginning 
# of the file
def rewind(f):
	f.seek(0)

# define function called print_a_line
# which takes in parameters line_count and f
# line_count 
# which, f is a variable that stores a file
# and the function altogether seeks a particular part of the file f,
# which, since it takes parameter zero, makes it go to the beginning 
# of the file
def print_a_line(line_count, f):
	print line_count, f.readline()


current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)