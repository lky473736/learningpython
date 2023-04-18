import turtle
import random

colorlist = ["red", "blue", "yellow", "green", "black"]

def touch_act(x, y) :
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    square()

def square() :
    for i in range (4) :
        turtle.begin_fill()
        turtle.color (colorlist[i])
        turtle.fd (100)
        turtle.right (90)
        turtle.end_fill()
    
turtle.onscreenclick(touch_act)

turtle.mainloop()