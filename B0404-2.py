# 임규연 (lky473736)

# 논리 연산자 : and, or, not

# 거북이 제어하는 프로그램

import turtle
t = turtle.Turtle()
t.shapesize(3, 3) # shapesize : comma를 기준으로 가로, 세로 순으로 n배 커짐

orderlist = ["l", "r", "s", "c", "q"] 
# l : 왼쪽, r : 오른쪽, s : 직선, c : 초기화, q : 종료

while True : 
    in0 = turtle.textinput ("", "명령을 입력 : ") # turtle 창에 입력
    if in0 == orderlist[0] :
        t.lt(90)
        t.fd(100)
    elif in0 == orderlist[1] :
        t.rt(90)
        t.fd(100)
    elif in0 == orderlist[2] :
        t.fd(100)
    elif in0 == orderlist[3] :
        t.clear()
    elif in0 == orderlist[4] : 
        exit() # exit : 파이선 콘솔에서 나가짐 (종료)
        
turtle.mainloop()
