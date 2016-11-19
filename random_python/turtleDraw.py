###########################################
#
#	Drawing with Turtle
#	Author: David Campos
#
###########################################
#
#	Execute on terminal:
#
#		python2
#
#		import turtleDraw as td
#
#		td.square()
#		td.triangle()
#		td.circle()
#		td.spiral()
#		td.squareSpiral()
#		td.circleSpiral()

import turtle as tl
import time as tm

def square():
	for x in range(0,3):
		tl.forward(100)
		tm.sleep(.1)
		tl.left(90)
		tm.sleep(.1)
	tl.forward(100)

def triangle():
	for x in range(0,2):
		tl.forward(100)
		tm.sleep(.5)
		tl.left(120)
		tm.sleep(.5)
	tl.forward(100)

def circle():
	for x in range(0,360):
		tl.forward(2)
		tl.left(1)
	tl.forward(2)

def spiral():
	degInc = 1
	for x in range(0,4000):
		tl.forward(2)
		tl.left(degInc)
		degInc = degInc + .001
	tl.forward(2)

def squareSpiral():
	tl.left(30)
	for z in range(0,12):
		tl.forward(10)
		square()
		tl.left(120)

def circleSpiral():
	for c in range(0,12):
		circle()
		tl.left(30)

print "\n\n RUN THIS PROGRAM:"
print "\n\tturtleDraw.square()"
print "\n\tturtleDraw.triangle()"
print "\n\tturtleDraw.circle()"
print "\n\tturtleDraw.spiral()"
print "\n\tturtleDraw.squareSpiral()"
print "\n\tturtleDraw.circleSpiral()"

