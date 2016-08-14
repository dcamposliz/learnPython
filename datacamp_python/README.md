#notes ( datacamp [ python ] )

Some basics:

	print()	-	printing
	type()	-	variable type
	**		-	exponents
	+ 		-	sum & concatenation
	str()
	float()
	int()

--

A list is a collection of python data types.

	list = [1,2,3]

can access list elements via indices.

	i = 0, 1, 2, ..., n
	where (n - 1) is the number of elements in the list

for example, if we enter:
	
	list = [1,2,3]

	list[0]

	> 1

if we enter:

	list = [1,2,3]

	list[2]

	> 3

if we enter:

	list = [1,2,3]

	list[-1]

	> 3

this is called 'indexing'.

we can also do 'slicing'.

if we enter:

	list = [1,2,3,4,5]

	list[1:3]

	> 2, 3

this means that:

	[   start   :    end     ]
	  inclusive   exclusive
	
if we enter:

	list = [1,2,3,4,5]

	list[:2]

	> 1, 2, 3

if we enter:

	list = [1,2,3,4,5]

	list[1] + list[3]

	> 6

we can do cool stuff:

	areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

	downstairs = areas[:6]
	upstairs = areas[-4:]

	print(downstairs)
	print(upstairs)

	> ['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
	> ['bedroom', 10.75, 'bathroom', 9.5]



	x = [["a","b","c"],["d","e","f"],["g","h","i"]]

	x[2][0]

	x[2][:2]

--

LIST MANIPULATION

we can update list elements. for example, if we have:

	list = [1, 2, 3, 4, 5]

	list[0]

	> 1

say we want to modify element at position 0, then we do:

	list[0] = "waa"

	list

	> ["waa", 2, 3, 4, 5]

say we want to add elements to a list, we do:

	list = [1, 2, 3, 4, 5]

	list + [6, 7, 8, 9, 10]

	> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

of course, we can declare new variables and assign these values

additionally, we can delete items from the list. for this, we do:

	list = [1, 2, 3, 4, 5]

	del(list[0])

	list

	> [2, 3, 4, 5]

--

behind the scenes

when we declare a list variable and assign values to it, we are not actually 'storing values' to our list variable. instead, our list variable points to the values we assign to it.

let's see an example to sense how this works:

	list = [1, 2, 3, 4, 5]

	x = list

	x[0] = "blah"

	list

	> ["blah", 2, 3, 4, 5]

insteresting that when we change the value of element with index 0 for list variable x, index 0 for list variable list also changes.

if we want to copy a list whose values are independent from the first list, we can do the following:

	list = [1,2,3,4,5]

	x = list(list)

as you can see, we used the list() function. we can also use slicing:

	list = [1,2,3,4,5]

	x = list[:]

this way, if we modify the element values of x, we will not modify the values of list.


--

FUNCTIONS

a function is a piece of reusable code, and it solves a particular task. we call functions instead of writing the code ourselves because it saves time :D

Here are a couple of python functions:

	type()

	max()

	round()

	help()

	print()

	str()

	int()

	bool()

	float()

	len()

For example:

	list = [1, 2, 3, 4, 5]

	max(list)

	> 5

When calling functions, some of the parameters are required, some are not.

--

Methods

Methods are functions that belong to objects.

For example, we have:

 - str:

	capitalize()

	replace()

 - float:

	bit_length()

	conjugate()

 - list:

	index()

	count()

We can do:

	list = ["green", "blue", "purple", "black"]

	list.index("blue")

	> 1

We can do:

	sister = 'jessica'

	sister.capitalize()

	> 'Jessica'

We can do:

	sister = 'jessica'

	sister.replace('ica', 'y')

	> 'jessy'

Methods will behave differently depending on the object type.

We can update our data structures on the fly.

We can do:

	colors = ["blue", "green", "purple"]

	colors.append("black")

	> ["blue", "green", "purple", "black"]


In this section we saw:

 - Functions

 - Methods: call functions on objects

  - We can call these using the dot notation:

  	object.method()

--

String Methods:

	upper()

We can do:

	color = 'green'

	color_up = color.upper()

	print(color_up)

	> GREEN

--

List Methods:

	append() -- adds element to list

	remove() -- removes the first element of a list that matches the input

	reverse() -- reverses the order of the different elements in the list it is called on

For example:
	
	numbers = [1, 2, 3, 4, 5]

	numbers.reverse()

	print(numbers)

	> [5, 4, 3, 2, 1]
	
--

PACKAGES

Functions and methods are powerful. Packages are directories of Python scripts, where each script is a module, and where modules specify functions, methods, and types.

There are thousands of packages, among which we find:

 - Numpy: to efficiently work with arrays

 - Matplotlib: for data visualization

 - Scikit-learn: for machine learning

Packages must first be installed globally, and then imported into scripts. We use pip as a package manager for Python.

	pip --stuff (google this stuff, come on)

	pip3 install numpy

Then we import installed packages using the import function. We can use an alias to call our installed package when we call its methods:

	import numpy

	numpy.array([1, 2, 3])

	> array([1, 2, 3])

Similarly (this time we use the alias thing):

	import numpy as np

	np.array([1, 2, 3])

	> array([1, 2, 3])

We can also import only certain functions from a package. For example:

	from math import pi

--

With stand-alone Python, it is difficult to manipulate lists at scale. For this, we use the numpy package, which stands for numerical python.

Numpy:

 - Numeric Python

 - Alternative to Python list: Numpy Array

 - Calculations over entire arrays

 - Easy and fast

 - Installation

  - In the terminal: pip3 install numpy

Example:
	
	import numpy as np

	list = [1,2,3,4,5]

	list_array = np.array(list)

	list_array ** 2

	> array([1, 4, 9, 16, 25])

Numpy array assumes that one one data type is being used. If this is not true, then numpy array will turn all elements into one data type -- this is known as type coercion.

Numpy array indexing works just as python lists.

--

