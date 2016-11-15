
# Source:
# https://www.youtube.com/watch?v=xtXexPSfcZg

# declaring a list
someList = [1,3,454,6,56]

# a loop iterating through our list :)
print 'We are running a for loop on a list'
for eachNumber in someList:
	print(eachNumber)

# another kind of loop
print 'We are running a while loop on a range'
for x in range(1,11):
	print x

# another loop
for aNumber in range (0, 20):
	print aNumber # this includes `0` but not `20`

# declaring variables, conditionals, loops, data conversion,
# concatenation
anotherList = [1,2,3,4,5]
someBool = True
if someBool:
	for thing in anotherList:
		print 'here is a thing:' + str(thing)

# checking for membership

grocery_bag = ['artichoke', 'carrot','celery','pizza', 'tomato']
davids_food = 'tomato'

# we check membership with `if`, `in`

if davids_food in grocery_bag:
	print (davids_food + ' is in the grocery bag')

