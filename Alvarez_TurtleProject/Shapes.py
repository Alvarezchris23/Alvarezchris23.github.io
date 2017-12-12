#1.1,2,3
def square(s,chris,r,g,b):
    for i in range(4):
        chris.forward(s)
        chris.left(90)
        chris.color(r,g,b)
        r = r - 10
        g = g + 18
        b = b - 17
        
        
def triangle(s):
    for i in range (3):
        turtle.forward(s)
        turtle.left(120)

def pentagon(s):
    for i in range (5):
        turtle.forward(s)
        turtle.left(72)

def hexagon(s):
    for i in range (6):
        turtle.forward(s)
        turtle.left(60)

def nonagon(s):
    for i in range(9):
        turtle.forward(s)
        turtle.left(40)

def decagon(s):
    for i in range(10):
        turtle.forward(s)
        turtle.left(36)

#1.4
#This is also part of Part 2.7 and 8 because it changes colors and stamps.
import turtle 

s = int(input('Hello, how many sides would you like your polygon to have? '))
print ('Ok, I will now make a polygon with ' + str(s) + ' sides.')
l = int(input('Ok, how long do you want each side to be? '))

angle = s - 2
angle1 = angle * 180
trueangle = 180 - (angle1/s)

wn = turtle.Screen()
wn.colormode(255)
trt = turtle.Turtle('turtle')

def AnyRegPoly(s,r,g,b):
    
    for i in range(s):
        trt.forward(l)
        trt.left(trueangle)
        trt.color(r,g,b)
        trt.stamp()
        r = r - 5
        g = g + 20
        b = g - 10

AnyRegPoly(s,255,1,255)

