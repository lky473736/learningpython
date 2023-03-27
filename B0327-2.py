import turtle 

def triangle():
    for i in range(3) :
        t.fd (leng)
        t.right(120)

def square():
    for i in range(4) : # 4번 반복한다
        t.fd (leng) # fd : forward (앞으로 간다)
        t.right (90) # 오른쪽으로 90도 꺾는다
    


t = turtle.Turtle()
t.shape ("turtle") # turtle, arrow, circle ... 다양한 커서 모양을 가질 수 있다
leng = int(input("길이 : ")) # 길이를 입력받는다
print ("삼각형 : 1, 사각형 : 2, 원 : 3")
choice = int(input("당신의 선택 : "))

if choice == 1 : # 정삼각형
    triangle()
    
elif choice == 2 : # 정사각형
    square()
    
elif choice == 3 : # 원
    t.circle(leng+30)
    
"""
t.penup() # 펜을 든다. 궤적이 그려지지 않는다
t.fd (leng+50)
t.pendown() # 다시 펜을 내린다. 이때부터는 궤적이 그려진다.
"""

turtle.mainloop()