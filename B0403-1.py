import turtle

t = turtle.Turtle()
t.shape("turtle")

def back():
    t.penup()
    t.fd(-250)
    t.pendown()

def draw():
    t.penup()
    t.fd(150)
    t.pendown()

s_c = ["blue", "red", "green", "purple"]

back()

for i in range(4):
    t.fillcolor(s_c[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    draw()
    
turtle.mainloop()

