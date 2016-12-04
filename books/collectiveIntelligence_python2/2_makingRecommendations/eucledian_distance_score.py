# importing data
import recommendations as recDT

# printing out data
print(recDT.critics)

# EUCLEDIAN DISTANCE SCORE
# ~~~~~~~~~~~~~~~~~~~~~~~~
"""
	The Eucledian Distance Score is a simple way of calculating a similarity score.

	In this example, it takes the items that people have ranked in common and uses them for axes.
"""

# In the following code we calculate the Eucledian distance between critics `Toby` and `LaSalle` 

from math import sqrt
stuff = sqrt(pow(5 - 4, 2) + pow(4 - 1, 2))
print(stuff)

print(1 / ( 1 + stuff))

	# I dont understand this example because I dont know where the 5,4,4,1 come from. It is my impression that the 5 should be a 4.5 and so forth.

