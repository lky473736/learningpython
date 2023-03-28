import turtle
t = turtle.Turtle
t.shape("turtle")

rad = int(input ("반지름값 : "))

s_c = ["blue", "red", "green", "purple"] # 리스트는 변수의 모음이다

t.fillcolor(s_c[0]) # 색깔 채우기 (리스트 중 0번째의 것을 변수로 취급 : blue 색깔)
t.begin_fill()
t.circle(rad)
t.end_fill()

turtle.mainloop()
