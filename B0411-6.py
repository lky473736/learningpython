# 별 그리기

import turtle

ang = 144
dis = int(turtle.textinput ("", "dis?"))

for i in range (5) :
    turtle.fd (dis)
    turtle.rt (ang)

turtle.mainloop()

'''
while문으로 작성하기

ang = 144
dis = int(turtle.textinput ("", "dis?"))
i = 0

while i < 5:
    turtle.fd (dis)
    turtle.rt (ang)
    i = i + 1

turtle.mainloop()
'''