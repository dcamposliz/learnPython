# Python3 Object-Oriented Programming

class Employee:
	pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.firstName = 'David'
emp_1.lastName = 'Campos'
emp_1.email = 'davidcampos@company.com'
emp_1.pay = 1000

emp_2.firstName = 'test'
emp_2.lastName = 'user'
emp_2.email = 'testuser@company.com'
emp_2.pay = 100

print(emp_1)
print(emp_2)

print(emp_1.firstName,' ',emp_1.lastName)

# this way of creating objects sucks, so we do the following:

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	def fullName(self):
		return '{} {}'.format(self.first, self.last)

"""

We can an instance of an employee and its attributes in the usual way:

	emp_1.fullName()

As well as print them, the usual way:

	print(emp_1.fullName())

We can also print them in the non-usual way, by calling the class instead of the instance:

	print(Employee.fullName(emp_1))

"""
