# PYTHON FOR DATA SCIENCE
### Notes from DataCamp

This README contains reference notes from DataCamp's courses on Python for Data Science, Intro as well as Intermediate.

# INTRODUCTION

## Some basics:

	print()		# for printing
	type()		# for variable type
	**		# for exponents
	+ 		# for sum & concatenation
	str()
	float()
	int()

## Lists

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

this is called **indexing**.

we can also do **slicing**.

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

## Maniputaling Lists

We can **update** list elements. for example, if we have:

	list = [1, 2, 3, 4, 5]

	list[0]

	> 1

say we want to **modify element** at position 0, then we do:

	list[0] = "waa"

	list

	> ["waa", 2, 3, 4, 5]

Say we want to **add elements** to a list, we do:

	list = [1, 2, 3, 4, 5]

	list + [6, 7, 8, 9, 10]

	> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Of course, we can declare new variables and assign these values.

Additionally, we can **delete** items from the list. for this, we do:

	list = [1, 2, 3, 4, 5]

	del(list[0])

	list

	> [2, 3, 4, 5]

#### *Behind the Scenes*

When we declare a list variable and assign values to it, we are not actually 'storing values' to our list variable. instead, our list variable points to the values we assign to it.

Let's see an example to sense how this works:

	list = [1, 2, 3, 4, 5]

	x = list

	x[0] = "blah"

	list

	> ["blah", 2, 3, 4, 5]

It is interesting that when we change the value of element with index 0 for list variable x, index 0 for list variable list also changes.

If we want to copy a list whose values are independent from the first list, we can do the following:

	list = [1,2,3,4,5]

	x = list(list)

As notable, we used the `list()` function. we can also use slicing:

	list = [1,2,3,4,5]

	x = list[:]

This way, if we modify the element values of x, we will not modify the values of list.

## Functions

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


## Methods

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

### String Methods:

	upper()

We can do:

	color = 'green'

	color_up = color.upper()

	print(color_up)

	> GREEN

### List Methods:

	append() -- adds element to list

	remove() -- removes the first element of a list that matches the input

	reverse() -- reverses the order of the different elements in the list it is called on

For example:
	
	numbers = [1, 2, 3, 4, 5]

	numbers.reverse()

	print(numbers)

	> [5, 4, 3, 2, 1]

## Packages

Functions and methods are powerful. Packages are directories of Python scripts, where each script is a module, and where modules specify functions, methods, and types.

There are thousands of packages, among which we find:

 - **Numpy**: to efficiently work with arrays

 - **Matplotlib**: for data visualization

 - **Scikit-learn**: for machine learning

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

**we are missing some notes here from the beginner python course.**

--

# INTERMEDIATE

We start with data visualizations with matplotlib.

Here we plot two vectors, year and pop.

	import matplotlib.pyplot as plt

	year = [1950, 1970, 1990, 2010]
	pop = [2.519, 3.692, 5.263, 6.972]

	plt.plot(year, pop)
	plt.show()

	plt.scatter(year, pop)
	plt.show()

It's worth noting the order of parameters for plt.plot() and plt.scatter(). The first parameter is the X-AXIS and the second parameter is the Y-AXIS.

We can do logarithmic transformations to our plots. For example:

	import matplotlib.pyplot as plt

	year = [1950, 1970, 1990, 2010]
	pop = [2.519, 3.692, 5.263, 6.972]

	plt.scatter(year, pop)

	plt.xscale('log')

	plt.show()

## Histograms

Type of visualization helpful to explore data and distributions. Python gives us histogram super-powers:

	import matplotlib.pyplot as plt

	help(plt.hist)

Let's do an example:

	# Build histogram with 5 bins
	plt.hist(life_exp, bins = 5)

	# Show and clean up plot
	plt.show()
	plt.clf()

	# Build histogram with 20 bins
	plt.hist(life_exp, bins = 20)

	# Show and clean up again
	plt.show()
	plt.clf()

## Customizations

 - Data visualization

  - Different plot types

  - Many customizations

  - Choise depends on data and story you want to tell

Example:

	import matplotlib.pyplot as plt

	year = [1950, 1951, 1952, ..., 2100]
	
	pop = [2.538, 2.57, 2.62, ..., 10.85]

	plt.plot(year, pop)

	plt.xlabel('Year')
	plt.ylabel('Population')
	plt.title('World Population Projections')
	plt.yticks([0,2,4,6,8,10],
			   ['0B','2B','4B','6B','8B','10B'])

	plt.show()

--

Here we start seeing bubbles:

	# Import numpy as np
	import numpy as np

	# Store pop as a numpy array: np_pop
	np_pop = np.array(pop)

	# Double np_pop
	np_pop = np_pop * 2

	# Update: set s argument to np_pop
	plt.scatter(gdp_cap, life_exp, s = np_pop)

	# Previous customizations
	plt.xscale('log') 
	plt.xlabel('GDP per Capita [in USD]')
	plt.ylabel('Life Expectancy [in years]')
	plt.title('World Development in 2007')
	plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

	# Display the plot
	plt.show()

--

Here we see colorful bubbles -- all we are doing is further customizing the plt.scatter() method.

	# Specify c and alpha inside plt.scatter()
	plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

	# Previous customizations
	plt.xscale('log') 
	plt.xlabel('GDP per Capita [in USD]')
	plt.ylabel('Life Expectancy [in years]')
	plt.title('World Development in 2007')
	plt.xticks([1000,10000,100000], ['1k','10k','100k'])

	# Show the plot
	plt.show()

--

There are other customizations we can make to our bubble plots. For example:

	plt.text(1550, 71, 'India')

	plt.grid(True)


--

## DICTIONARIES

Declare a dictionary:

	dictionary = {
		"key_1":"value_1"
		"key_2":"value_2"
		
		...

		"key_n":"value_n"
	}

Check the value of a key within a dictionary:

	dictionary["key"]

	> value

Add a key-value pair to an existing dictionary:

	dictionary["key"] = value

Check whether a key is part of a dictionary:

	"key" in dictionary

	> True

Delete a key-value pair from a dictionary:

	del(dictionary["key"])

Dictionaries can contain other dictionaries:

	dictionary_0 = {
		"key_0" = {
			"key_1" = "value_1",
			"key_2" = "value_2"
		}
	}

For the above dictionary, we can access `value_1` by typing:

	dictionary_0["key_0"]["key_1"]

If we wanted to print such value, all we would do is to wrap it in the `print()` function:

	print(dictionary_0["key_0"]["key_1"])


## PANDAS

**Pandas** is an open source library written in Python. Pandas is interesting because it provides high-performance and easy-to-use data structures and data analysis tools.

The `DataFrame` is one of the most important data structures in Pandas. It is a way to store tabular data -- basically rows and columns. We can use Python dictionaries to build Pandas DataFrames.

### Importing Pandas

	import pandas as pd

### Creating a DataFrame out of a Dictionary

	california = {
		key_1 : { ... },
		key_2 : { ... },
		key_3 : { ... }
	}
	
	california_DataFrame = pd.DataFrame(california)

Notice that we imported `pandas` as `pd`, and that we are calling `DataFrame` by `pd.DataFrame()`.

At this point we can see our newly formed DataFrame by doing a simple `print()`:

	print(california_DataFrame)

### Indexing a DataFrame

By convention, rows will be indexed, starting from `0`. We can specify a 'custom' index by using an array -- such array must contain the same amount of elements as the DataFrame.

	row_labels = ['row_1','row_2', ..., 'row_n']

	california_DataFrame.index = row_labels

### CSV to DataFrame

We can import data from a CSV file into Python using the `read_csv()` method. Of course we must call this method from the pandas object, which we denoted earlier as `pd`. Notice that we surround `FILE.csv` with quotes.

	DATAFRAME_NAME = pd.read_csv("FILE_NAME.csv")

`read.csv_()` has multiple parameters, amongst which `index_col` is used to specify which column in the CSV file should be used as row label -- we use integers, starting from `0`, to make such specification.

	DATAFRAME_NAME = pd.read_csv("FILE_NAME.csv", index_col = 0)

### Accessing Data with Pandas

#### Columns

With Pandas we have another data type, known as **Pandas Series**. Let's see an example:

	import pandas as pd
	DATAFRAME_NAME = pd.read_csv("FILE_NAME.csv", index_col = 0)

	DATAFRAME_NAME["COLUM_NAME"] 	# returns pandas series object

We could print this object by wrapping it in the `print()` method, for example.

	print(DATAFRAME_NAME["COLUM_NAME"])

We can output the 'good-old' Pandas **DataFrame** with *double-bracket* notation:

	DATAFRAME_NAME[["COLUMN_NAME"]]		# returns pandas DataFrame

Let's print two DataFrame columns to see how it's done:

	print(DATAFRAME_NAME[["COLUMN_NAME_1","COLUMN_NAME_2"]])

#### Rows

We can access rows, also using square brackets. For this we use `DATAFRAME_NAME[i:j]` such that `i` and `j` are the beginning and ending rows for our subset, respectively. Again:

	DATAFRAME_NAME[i:j]

### More Data Selection `loc` and `iloc`

`loc` is labeled based, whereas `iloc` is index based. As we saw before, we can access data in dataframes as either **series** or **dataframes**:

	import pandas as pd
	DATAFRAME_NAME = pd.read_csv('FILE_NAME.csv', index_col = 0)

**As Series**:

	DATAFRAME_NAME.loc["ROW_NAME"]
	DATAFRAME_NAME.iloc[i]

**As DataFrame**:

	DATAFRAME_NAME.loc[["ROW_NAME"]]
	DATAFRAME_NAME.iloc[[i]]

`loc` and `iloc` also let us access both rows and columns from a dataframe, at the same time.

**As Series**:

	DATAFRAME_NAME.loc["ROW_NAME", "COLUMN_NAME"]
	DATAFRAME_NAME.iloc[i,j]

**As DataFrame**:

	DATAFRAME_NAME.loc([['ROW_NAME_1','ROW_NAME_2'],['COLUMN_NAME_1','COLUMN_NAME_2']])

We can also select *only* columns with `loc` and `iloc`:

**As Series**:

	DATAFRAME_NAME.loc[:,'COLUMN_NAME'] # this returns data for all rows spanning COLUMN_NAME, as a pandas series
	DATAFRAME_NAME.iloc[:, i] # this returns data for all rows spanning column *i*, as a pandas series

We can do the same for accessing **dataframes**. All we need to do is add the necessary *double-brackets*.

##








