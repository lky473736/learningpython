import random
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

frontimg = "/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/img/coin-front.jpg"
screen.addshape(frontimg)

backimg = "/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/img/coin-back.jpg"
screen.addshape(backimg)

com = random.randrange(2) # randrange : 0 ~ n-1까지 컴퓨터가 랜덤으로 수를 지정함
# 위와 같은 뜻 : com = random.randint(0, 1)

if com == 1 :
    com = "앞면입니다" # 다시 com 변수에 문자열을 지정해준다
    print ("동전을 던집니다.")
    print (com)
    t.register_shape("frontimg", shape=None) # why is non-doing about shape?
    t.shape("frontimg")
    t.stamp()
    
else : 
    com = "뒷면입니다"
    print ("동전을 던집니다.")
    print (com)
    t.register_shape("backimg", shape=None)
    t.shape("backimg")
    t.stamp()

# turtle.TurtleGraphicsError: Bad arguments for register_shape.
