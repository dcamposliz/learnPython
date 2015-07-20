#assigns integer of 100 to the variable cars
cars = 100

#assigns integer of 4 to the variable space_in_a_car
space_in_a_car = 4.0

#assigns integer of 30 to the variable drivers
drivers = 30

#assigns integer of 90 to the variable passengers
passengers = 90

#assigns value of (cars - drivers) to the variable cars_not_driven
cars_not_driven = cars - drivers

#assigns value of (drivers) to the variable cars_driven
cars_driven = drivers

#assings value of (cars_driven * space_in_a_car) to the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

#assigns value of (passengers / cars_driven) to the variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
