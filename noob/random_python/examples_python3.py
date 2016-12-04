# more loops
import time as t

sleepVar = .05

n = 10
print("Initiating...")
t.sleep(sleepVar)
while n > 0:
	print (n)
	n = n - 1
	t.sleep(.7)
print("BOOM !")
t.sleep(sleepVar)

# for loop, again
friends = ["sarah", "ravi", "shon", "amil"]

for person in friends:
	print(person)
	t.sleep(sleepVar)

# range
for n in range(0,51,5):	# 3rd arg tells the iteration value
	print(n)
	t.sleep(sleepVar)

for n in range(10, 1, -1):
	print(n)
	t.sleep(sleepVar)

print("\nPractice problem: Find Sum of all Integers between 1 and 100")

# find the sum of all the integers between 1 and 100
sumMing = 0
for n in range(1, 101, 1):
	sumMing = sumMing + n
print(sumMing)

# we can also do this the short way:
print(sum(range(0,101)))

# program does not end until certain string is entered
while True:
	phrase = input('Parrot activated.\nEnter "shut up" to quit this program.\n')
	if (phrase == 'shut up'):
		break
	else:
		print(phrase + '\n')

# we learned about `input()` method and `break` keyword

# `input()` asks user for CLI argumnet, this can be stored as a variable
# `break` terminates a loop

