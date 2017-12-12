#3.3 and 4,5,6

import turtle as trt

def polygon(s,f,trt):
    trt.pu()
    trt.goto(-s/2,s/2)
    trt.pd()
    for i in range(f):
        trt.forward(s)
        trt.right(360/f)
        trt.speed(0)

for i in range (2,100,8):

    polygon(i,4,trt) 

#3.1 and 2
import turtle
import Shapes

messi = turtle.Turtle('turtle')
messi.speed(0)

window = turtle.Screen()
window.colormode (255)
window.bgcolor(0,40,34)

for i in range(10):
    Shapes.square(10 * i, messi, 255,30,255)    

