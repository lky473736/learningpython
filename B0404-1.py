# 임규연 (lky473736)

import turtle

t = turtle.Turtle()

# def 안에 def를 할 수 있다. -> 함수의 유기적인 결합 
# method -> function (동일치 사용)

def moves() :
    t.goto(100, 100) # goto : 이동할 수 있는 함수 (괄호 안에는 이차원 좌표를 넣는다)
    t.write("거북이가 여기로 오면 양수입니다.")
    
    t.goto(100, 0)
    t.write("거북이가 여기로 오면 0입니다.")
    
    t.goto(100, -100)
    t.write("거북이가 여기로 오면 음수입니다.")

def draw() :
    if sel > 0 : 
       t.goto(100, 100) # goto : 이동할 수 있는 함수 (괄호 안에는 이차원 좌표를 넣는다)
       t.write("거북이가 여기로 오면 양수입니다.")

    elif sel == 0 : 
       t.goto(100, 0)
       t.write("거북이가 여기로 오면 0입니다.")

    else : 
       t.goto(100, -100)
       t.write("거북이가 여기로 오면 음수입니다.")
    


# 거북이가 글을 쓰는 코드
t.penup()
t.fd(-300)

moves()

t.goto(-300, 0) # 원상복귀
t.pendown()


# 양수, 0, 음수에 따라 거북이가 이동됨
sel = turtle.textinput("", "수 입력 : ")

sel = int(sel)

draw()

turtle.mainloop()
