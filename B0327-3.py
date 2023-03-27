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

while True : 
    t.shape ("turtle") # turtle, arrow, circle ... 다양한 커서 모양을 가질 수 있다
    leng = int(input("길이 : ")) # 길이를 입력받는다
    print ("1 : 삼각형, 2 : 사각형, 3 : 원")
    choice = int(input("당신의 선택은? : "))
    t.clear() # 꼬부기가 그린거 지운다
    
    if choice == 1:
        triangle()
    
    elif choice == 2:
        square()
        
    elif choice == 3:
        t.circle(leng)
        
    else:
        print("프로그램 종료")
        break # 반복문 종료
    

turtle.mainloop()  