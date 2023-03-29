import turtle

t = turtle.Turtle()
t.shape("turtle")

rad = int(input("반지름 : "))

s_c = ["blue", "red", "green", "purple"] # 리스트는 여기서 색깔 변수의 모음이다.

t.penup()
t.fd(-250)
t.pendown()

t.fillcolor(s_c[0])
t.begin_fill()
t.circle(rad)
t.end_fill()

t.penup()
t.fd(150)
t.pendown()

t.fillcolor(s_c[1])
t.begin_fill()
t.circle(rad)
t.end_fill()

t.penup()
t.fd(150)
t.pendown()

t.fillcolor(s_c[2])
t.begin_fill()
t.circle(rad)
t.end_fill()

t.penup()
t.fd(150)
t.pendown()

t.fillcolor(s_c[3])
t.begin_fill()
t.circle(rad)
t.end_fill()

turtle.mainloop()
