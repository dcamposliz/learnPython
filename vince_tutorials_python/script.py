# VINCE LA - PYTHON TUTORIAL
#
# notes by David Campos

# BASIC DATA TYPES

# strings
x = "A string"
y = 'A string'
z = '''A string'''
print(x)
print(y)
print(z)

x == y == z
print("Next we will print a boolean data type, not a string:")
print(x == y == z)


quote = "The governor said that there was a 'fat chance' of the bill passing"
print(quote)

# all data in python can be classified by its `type`, for example:

string1 = "This is a string"
integer = 1

print(string1)
print(integer)

# we can use `int()` and `float()` to convert strings into numbers

waa = 123 + int("123")
print(waa)

# STRING OPERATIONS

# concatenation: joining strings together

x = "Colorless green ideas"
space = " "
y = "sleep furiously."
z = x + space + y
print(z)

# concatenation involving numbers

money = 10

# to be able to print the `money` variable in the context of a string, we have to apply the str() method to it

someStatement = "I have " + str(money) + " dollars"
print(someStatement)

# repetition

x = "Repeat after me. "
print(x * 2)

print("Echo" * 10)

# practice problem: the plus operator

shampoo = 5
milk = 3
eggs = 5
bacon = 5

print("The total cost is $" + str(shampoo + milk + eggs + bacon))

# STRING METHODS

numberStatement = "555"
numberStatement.isnumeric()
print(numberStatement.isnumeric())

# getting lowercase

x = "LOWERCASE ME"
x.lower()
print(x.lower())

x = "capitalize me!"
x.upper()
print(x.upper())

# string formatting via str.format()

'My {0} is {1}'.format('car','new')
print('My {0} is {1}.'.format('car','new'))

x = "David"
"My name is {0}".format(x)
print("My name is {0}".format(x))

houses_amount = 100
"There are {0} houses in this square mile.".format(houses_amount)
print("There are {0} houses in this square mile.".format(houses_amount))
