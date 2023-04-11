# 임규연 (lky473736)

import turtle
import random

dis = random.randint (10, 100) # 거리
ang = random.randint (0, 180) # 각도
dir = random.randint (0, 2) # 방향

for i in range (50) :
    turtle.fd (int(dis))
    
    if dir == 0 :
        turtle.lt(dir)
    elif dir == 1 :
        turtle.rt(dir)