# ON TERMINAL:
#
#	python2
#
#	import turtleDraw as td
#
#	td.square()
#	td.triangle()
#	td.circle()
#	td.spiral()
#	td.squareSpiral()

import turtle as tl
import time as tm

def square():
	for x in range(0,3):
		tl.forward(100)
		tm.sleep(.5)
		tl.left(90)
		tm.sleep(.5)
	tl.forward(100)

def triangle():
	for x in range(0,2):
		tl.forward(100)
		tm.sleep(.5)
		tl.left(120)
		tm.sleep(.5)
	tl.forward(100)
	tl.exitonclick()

def circle():
	for x in range(0,360):
		tl.forward(2)
		tm.sleep(.0001)
		tl.left(1)
		tm.sleep(.0001)
	tl.forward(2)
	tl.exitonclick()

def spiral():
	degInc = 1
	for x in range(0,4000):
		tl.forward(2)
		tl.left(degInc)
		degInc = degInc + .001
	tl.forward(2)
	tl.exitonclick()

def squareSpiral():
	tl.left(30)
	for z in range(0,12):
		tl.forward(10)
		square()
		tl.left(120)

print "\n\n RUN THIS PROGRAM:"
print "\n\tturtleDraw.square()"
print "\n\tturtleDraw.triangle()"
print "\n\tturtleDraw.circle()"
print "\n\tturtleDraw.spiral()"
print "\n\tturtleDraw.squareSpiral()"

