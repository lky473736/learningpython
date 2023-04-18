import turtle
t = turtle.Turtle()
s = turtle.Screen()

def draw(x, y) :
    t.goto (x, y)

t.pensize(5)
s.onscreenclick (draw)
    
turtle.mainloop()