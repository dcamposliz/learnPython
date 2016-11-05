
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
