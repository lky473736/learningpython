import turtle
t = turtle.Turtle()

def lenbreadsquare() :
    length = int(turtle.textinput ("", "가로"))
    breadth = int(turtle.textinput ("", "세로"))
    for i in range (2) :
        t.fd(length)
        t.lt(90)
        t.fd(breadth)
        t.lt(90)
    
def distotriangle() :
    dis = int(turtle.textinput ("", "길이"))
    t.triangle (dis)
    
def radtocircle() :
    rad = int(turtle.textinput ("", "반지름"))
    rad = int(rad)
    t.circle (rad)

shape = turtle.textinput ("", "도형을 입력하세요.")

if shape == "사각형" :
    lenbreadsquare()

elif shape == "삼각형 " :
    distotriangle()

elif shape == "원" :
    radtocircle()

turtle.mainloop()