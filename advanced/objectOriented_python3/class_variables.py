

class Employee:

	num_of_employees = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		
		Employee.num_of_employees += 1 # this increases value for class variable

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		#SAME AS: self.pay = int(self.pay * Employee.raise_amount)
"""

Notable in this script is the raise amount class variable raise_amount.

To access it for any given instance, we would enter to the terminal:

	INSTANCE.apply_raise()

We can also enter:

	print(Employee.__dict__)

"""

	
