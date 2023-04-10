import turtle

t = turtle.Turtle()
t.shape ("turtle")
t.speed ()

rad = int(turtle.textinput("", "rad"))
number = int(turtle.textinput ("", "What number do you want? : "))

for i in range (number) :
    t.circle(rad)
    t.right(360/number)
    
turtle.mainloop()