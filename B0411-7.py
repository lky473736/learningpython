''' 
함수, 딕셔너리, 리스트 (넘버링)
중간고사 범위 : 함수까지
C언어의 함수 형태 : 4가지 형태
python의 함수 형태 : return값의 지저분한 입출로 인해 형태가 많음

보통의 return : 함수 하나 -> 하나의 return 값 (만일 return 값을 여러 개 반환하고 싶다면 배열을 이용해야 함)
python의 return : 함수 하나 -> 다양한 return 값
'''

import turtle

a = turtle.textinput("", "dis?")
a = int(a)

def square() :
    for i in range(4) :
        turtle.forward(a)
        turtle.right(90)

for i in range (3) : 
    square()
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()