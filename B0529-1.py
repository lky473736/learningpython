# 그림판 만들기

from tkinter import *
window = Tk()

color = "blue"

def cred() :
    global color # 지역변수로 만들어서 빨간색으로 만들거임
    color = "red"
    
def cgreen() :
    global color 
    color = "green"
    
def cblue() :
    global color
    color = "blue"
    
def end() :
    exit()
    # == window.destroy()
    
def paint(event) : 
    x1, y1 = (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    canvas.create_oval (x1, y1, x2, y2, fill = color)

canvas = Canvas(window, height = 500, width = 500)
canvas.pack()

b1 = Button(window, text = "빨강색", command = cred)
b1.pack()

b2 = Button(window, text = "초록색", command = cgreen)
b2.pack()

b3 = Button(window, text = "파란색", command = cblue)
b3.pack()

b4 = Button(window, text = "종료", command = end)
b4.pack()

canvas.bind("<B1-Motion>", paint)
window.mainloop()