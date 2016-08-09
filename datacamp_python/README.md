#notes ( datacamp [python] )

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
	
