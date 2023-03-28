import turtle

t = turtle.Turtle()
t.shape("turtle")

n = int(input("각도 입력 : "))
l = int(input("길이 입력 : "))


# n각형 만들기
for i in range(n):
        t.fd(l)
        t.left(360/n)

t.penup
t.fd(l+100)
t.pendown()

for i in range(n+1):
        t.fd(l)
        t.left(360/(n+1))

t.penup
t.fd(l+100)
t.pendown()

for i in range(n+2):
        t.fd(l)
        t.left(360/(n+2))

t.penup
t.fd(l+100)
t.pendown()
        
turtle.mainloop()
