# 임규연 (lky473736)

import turtle

t = turtle.Turtle()


# 거북이가 글을 쓰는 코드
t.penup()
t.fd(-300)

t.goto(100, 100) # goto : 이동할 수 있는 함수 (괄호 안에는 이차원 좌표를 넣는다)
t.write("거북이가 여기로 오면 양수입니다.")
    
t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")
    
t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다.")
t.goto(-300, 0) # 원상복귀
t.pendown()


# 양수, 0, 음수에 따라 거북이가 이동됨
sel = int(input("입력 : "))

if sel > 0 : 
    t.goto(100, 100) # goto : 이동할 수 있는 함수 (괄호 안에는 이차원 좌표를 넣는다)
    t.write("거북이가 여기로 오면 양수입니다.")

elif sel == 0 : 
    t.goto(100, 0)
    t.write("거북이가 여기로 오면 0입니다.")

else : 
    t.goto(100, -100)
    t.write("거북이가 여기로 오면 음수입니다.")

turtle.mainloop()