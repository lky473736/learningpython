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
    a = a + 1

s_c = ["blue", "red", "green", "purple"]

back()

a = 0
for i in range(4):
    t.fillcolor(s_c[a])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    draw()
    
turtle.mainloop()