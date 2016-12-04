# -----------------------------------------------------
# CHAPTER 2
# -----------------------------------------------------
# A CRASH COURSE IN PYTHON
# -----------------------------------------------------
# Oct 22, 2016
#
# annotated by David A Campos
# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# WHITE SPACE FORMATTING
# -----------------------------------------------------

    # python uses indentation (instead of curly braces)
    # to delimit blocks of code

for i in [1, 2, 3, 4, 5]:
    print i
    for j in [1, 2, 3, 4, 5]:
        print j
        print i + j
    print i
print "done looping"

# -----------------------------------------------------

    # lists are readable

long_winded_computation = {1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20}

    # so are lists of lists

list_of_lists = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]

# -----------------------------------------------------

    # use backslash to indicate that statement continues
    # onto the next line

two_plus_three =    2 + \
                    3

# -----------------------------------------------------

    # this should output an error
    # but it doesn't because our version of
    # python is chill

for i in [1, 2, 3, 4, 5]:

    # notice the blank line
    print i

# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# MODULES
# -----------------------------------------------------

    # a python module is simply a python source file,
    # which can expose classes, functions, and global
    # variables. When imported from another source file,
    # the name is treated as a namespace.

    # a python namespace is a space that holds a bunch
    # of names. The Python namespace says that they are
    # a mapping from names to objects. Think of it as a
    # big list of all the names you have defined, either
    # explicitly or by importing modules. It's something
    # that gets created whenever necessary by the system.
    # no need to worry about it.

        # here is some info on `namespaces`
        # https://bytebaker.com/2008/07/30/python-namespaces/

# -----------------------------------------------------

    # we can simply import the module

import re
my_regex = re.compile("[0-9]", re.I)

# -----------------------------------------------------

    # we can import the module with an alias
    # in case we already have a different
    # `re` in our code

import re as regex
my_regex = regex.compile("[0-9]", regex.I)

# -----------------------------------------------------

    # some modules have ugly names, and we want
    # to use a conventional alias

import matplotlib.pyplot as plt

# -----------------------------------------------------

    # if you only need specific values from a module,
    # you can import them specifically

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# -----------------------------------------------------

    # we can also be dumb, and have conflicting
    # names in our namespace

# match = 10
# from re import *    # uh oh, re has a match functions
# print match         # "<function re.match>"

# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# ARITHMETIC
# -----------------------------------------------------

    # by default, python will carry out integer divisions

5 / 2   # should output 2
# from __future__ import division
5 / 2   # should output 2.5 now that we imported `division`
2 + 2

# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------

def double(x):
    """ This is where you put additional notes about your
    function. For example, this function takes an input,
    `x`, and returns `x * 2`."""
    return x * 2


# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# STRINGS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# EXCEPTIONS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# LISTS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# TUPLES
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# DICTIONARIES
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# SETS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# CONTROL FLOW
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# TRUTHINESS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# SORTING
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# LIST COMPREHENSIONS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# GENERATORS AND ITERATORS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# RANDOMNESS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# REGULAR EXPRESSIONS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# OBJECT-ORIENTED PROGRAMMING
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# FUNCTIONAL TOOLS
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# ENUMERATE
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# `zip` AND ARGUMENT UNPACKING
# -----------------------------------------------------





# -----------------------------------------------------

#
#
#

# -----------------------------------------------------
# `args` AND `kwargs`
# -----------------------------------------------------





# -----------------------------------------------------

#
# For further exploration
#

    # The Python Tutorial: https://docs.python.org/2/tutorial/

    # The IPython Tutorial: http://ipython.org/ipython-doc/2/interactive/tutorial.html

    # Python for Data Analysis Book: http://shop.oreilly.com/product/0636920023784.do
