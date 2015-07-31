#	we are defining a function here
#	which takes two parameters of the integer type
#	then we print strings along with the integers we define

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#	we are printing a string
#	followed by executing the cheese_and_crackers function defined above
#		where we pass values for the arguments the function requires 
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#	we can also assign values to new variables
#	and use such variables as arguments for our function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#	then we run the function, using the variables above for our parguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#	we can also do math for the arguments, and run the function
#	given such parameters
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#	we can variables, math, etc, and run the function
#	given such parameters :)
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)