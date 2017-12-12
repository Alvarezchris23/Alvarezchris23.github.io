import turtle
turtle.delay(0)
turtle.speed(0)


wn=turtle.Screen()
wn.colormode(255)

r=255
g=0
b=255

for i in range (500):
    turtle.color(r,g,b)
    turtle.forward(i)
    turtle.left(91)
    turtle.speed(0)
    r=r-1
    g=g+1
    b=b-1
    if r > 255:
        r = 255
    if g < 0:
        g = 0
    if r > 255:
        r = 255
