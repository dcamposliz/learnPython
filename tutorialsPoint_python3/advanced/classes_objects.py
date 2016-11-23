class Employee:
	'Common base class for all employees'
	empCount = 0

	def __init__(self, name, salary):
		self.name = name # Employee has a name
		self.salary = salary # Employee has a salary
		Employee.empCount += 1 # Employee count increases by one everytime the Employee count is instantiated

	def displayCount(self):
		print ("Total Employee count is %d" % Employee.empCount) # this is an interesting way of printing an integer within 

	def displayEmployee(self):
		print ("Name : ", self.name, ", Salary: ", self.salary)


# We can instanciate the methond `Employee` like this:
emp1 = Employee("Simon", 2000)
emp2 = Employee("Manni", 5000)


# Here we execute Employee method `displayEmployee`, and stuff
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

# Say Manny, aka `emp2` gets a name change
emp2.name = "Marco"
print("\nEmployee 2, namely `emp2`, got a new name:")
emp2.displayEmployee()

"""
# Here are some useful functions for working with objects:

	getattr(obj, name[, default])

		# to access the attribute of object.

	hasattr(obj, name)

		# to check if an attribute exists or not.
	
	setattr(obj,name,value)

		# to set an attribute. Is attribute does not exist, then it gets created.
"""

hasattr(emp1, 'salary')
getattr(emp1, 'salary')
setattr(emp1, 'salary', 7000)
emp1.displayEmployee()

# delattr(emp1, 'salary')



"""
Built-In Class Attributes

	__dict__:

		# Dictionary containing the class's namespace.

	__doc__:

		# Class documentation string or none, if undefined.

	__name__:

		# Class name.

	__module__:

		# Module name in which the class is defined. This attribute is "__main__" in interactive mode.

	__bases__:

		# A possibly empty tuple containing the base classes, in order of their occurrence in the base class list.
"""

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)



"""

We can also destroy objects (Garbage Collection)

Python automatically destroys objects when their reference count reaches a threshold.

"""

# here we see an increase in reference count for 40
a = 40
b = a
c = [b]

# and here we see a decrease
del a
b = 100
c[0] = -1



