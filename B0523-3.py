from tkinter import *
window = Tk()

r = Label (window, text="박스 #1", bg = "red", fg = "white")

r.place(x = 0, y = 0) # l.pack()과 다른 점 : 좌표를 지정해줬다 (절대위치배치)

g = Label (window, text="박스 #2", bg = "green", fg = "white")

g.place(x = 20, y = 20) 

b = Label (window, text="박스 #3", bg = "blue", fg = "white")

b.place(x = 40, y = 40)

window.mainloop()