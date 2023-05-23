from tkinter import *
window = Tk()

colorlist = ["black, red, green, blue"]

def colorchange(event) :
    x1, y1 = (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    
    if
    canvas.crate_oval (x1, y1, x2, y2, fill = colorlist[i + 1])

def paint(event, color = colorlist[0]) : 
    x1, y1 = (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    canvas.crate_oval (x1, y1, x2, y2, fill = color)

canvas = Canvas(window, height = 500, width = 500)
canvas.pack()

b1 = Button(window, text = "색상 변경 (검, 빨, 초, 파)", command = colorchange)

canvas.bind("<B1-Motion>", command = paint)
window.mainloop()