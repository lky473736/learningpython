# n각형 함수

import turtle
turtle.speed (0)

def regularshape(time) : 
    for i in range (time) :
        for i in range (n) :
            turtle.fd (len)
            turtle.rt (360 / n)
        turtle.rt (20)
        
n = int(turtle.textinput ("", "n?"))
len = int(turtle.textinput ("", "len?"))
time = int(turtle.textinput ("", "time?"))
regularshape(time)
turtle.mainloop()