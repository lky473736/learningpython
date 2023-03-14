# 임규연 (lky473736) 
# AlphaMech_ 

import turtle
t = turtle.Turtle()
t.shape ("turtle")

#rad = int (input ("입력 : "))
#저 위엔 '일반입력문구'임. 인터프리터에서 입력 받음

rad = turtle.textinput ("", "입력 : ")
#turtle 창에서 입력을 받게끔 하는 코드임
# = 그래픽 입력
len = turtle.textinput ("", "입력 : ")

rad = int(rad)
#rad를 정수형으로 바꾼다 (입력은 문자형이니깐)
len = int(len)

for i in range(3) :
    t.circle(rad) # 반지름이 100인 원 그림
    t.fd (len) # 100 나아감 

# for i in range (n)
# : 들여쓰기 한 부분이 n번 반복된다.


turtle.mainloop()
turtle.bye()
turtle.exitonclick() 

# exitonclick : 누를 때 나가짐 
 
