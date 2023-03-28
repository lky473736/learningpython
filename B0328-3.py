import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "당신의 이름 : ") # 터틀 창 안에서 input (가상 창을 띄워서) 

for i in range(4) :
    t.fd(200)
    t.left(90)

t.write(s + " 씨 안녕하세요. 반가워요!") # 터틀 창 안에서 output (터틀 옆에 화면에 띄워짐)
print(s + " 씨 안녕하세요. 반가워요!") # 인터프리터 창 안에서 output 
turtle.mainloop()
