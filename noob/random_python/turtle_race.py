#---------------------------------------------------
# Program:      TURTLE RACE
# Author:       VINCE LA
# Some annotations:  David Campos
#---------------------------------------------------

# In this script two turtles race each other.
# The caveat is, there is a turtle-police involved, 
# which has a 2/3 chance of chasing after one of the 
# two racing turtles.

# importing modules
import math, random, turtle

#Our turtles
Amy = turtle.Turtle('turtle')
Robert = turtle.Turtle('turtle')
cop = turtle.Turtle('turtle')

def setup(turtle1, turtle2, s, police):
    s=turtle.Screen()
    s.setworldcoordinates(0,0,50,50)
    turtle1.up()
    turtle2.up()
    turtle1.color('red') # color(pen, fill)
    turtle2.color('red')
    turtle1.setposition(1,25)
    turtle2.setposition(1,25)
    turtle1.down()
    turtle2.down()

    if (police == 'chase'): # Sets up cop turtle, if they are in "chase" mode
        cop.setposition(0,0)
        cop.up()
        
def newHeading(turtle, angleOfTipsiness):
    angle = yourVariableNamesAreTooLong = random.randint(-angleOfTipsiness, angleOfTipsiness)
    turtle.seth(angle)

def newColors(turtle1, turtle2, nSteps, timeStep):
    if (turtle1.xcor() > turtle2.xcor()):
        turtle1.color('green') #Winner
        turtle2.color('red') #You suck

    else:
        turtle1.color('red') #Loser
        turtle2.color('green') #Winner

    #Make the turtles "bleed ink" (pen width gets thinner) over time
    if (nSteps - 5 > timeStep):
        turtle1.width(nSteps/timeStep)
        turtle2.width(nSteps/timeStep)

    else: #Makes turtles "run out of ink"
        turtle1.up()
        turtle2.up()

def tipsyTurtleRace(turtle1,turtle2,angleOfTipsiness,nSteps,police):
    suspectStatus = 'on the loose'
    sirenIndex = 0 #Cycles through siren colors

    whoToChase = random.randint(1,2) #Randomly selects drunk turtle to be chased
    if (whoToChase == 1): suspect = turtle1
    else: suspect = turtle2
    
    for timeStep in range(1,nSteps+1):
        newHeading(turtle1,angleOfTipsiness) #Makes turtles move in random directions
        newHeading(turtle2,angleOfTipsiness)
        if (suspectStatus != 'arrested'): #If no turtle has been arrested, they can move freely
            turtle1.forward(turtleSpeed)
            turtle2.forward(turtleSpeed)
        else: #Makes the arrested turtle stop moving
            if (suspect != turtle1): turtle1.forward(1)
            if (suspect != turtle2): turtle2.forward(1)
            
        newColors(turtle1, turtle2, nSteps, timeStep) #Changes colors of turtles depending on which one is ahead, and also makes them lose ink
        
        if (police == 'chase'): #Police chase animation
            #Measure distance between suspect and cop
            xDistance = suspect.xcor() - cop.xcor()
            yDistance = suspect.ycor() - cop.ycor()
            xyDistance = math.sqrt((suspect.xcor() - cop.xcor())**2 + (suspect.ycor() - cop.ycor())**2) #Straight-line distance

            #Police siren: Wee woo wee woo wee woo
            sirenIndex += 1
            siren = ['yellow', 'red']
            cop.color('blue', siren[sirenIndex%2])

            if (xyDistance < 2 and suspectStatus != 'arrested'): #If suspect is close, arrest them
                print('"I have the suspect in custody"')
                suspectStatus = 'arrested'
                cop.setposition(suspect.xcor(),suspect.ycor()) #Moves the cop on top of the suspect
                
            else: #Determines cop's heading
                if (abs(yDistance > 5)): copHeading = 68 #Cop is far away from suspect verticially
                else:
                    if (xDistance < 0): copHeading = 180 #Cop is in front of suspect
                    else: copHeading = suspect.heading() #Cop is close behind suspect
                
            if (suspectStatus != 'arrested'): #Move the police car
                print('Suspect is',xyDistance*5//1,'feet away')
                cop.forward(3)
                cop.seth(copHeading)
                
##Random chance of police chase
if (random.randint(1,3) < 3):
    police = 'chase'
    turtleSpeed = 2 #Makes the turtles even more irresponsible
    print('Police are on alert for drunk drivers')
    print('"Im in pursuit"')
else:
    police = 'donuts'
    turtleSpeed = 1
    print('The police are taking a donut break')

#Run the race
setup(Amy,Robert,'s',police)
nSteps = 50
tipsyTurtleRace(Amy,Robert,70,nSteps,police)