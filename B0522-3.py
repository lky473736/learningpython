from tkinter import *

def mode1() :
    k = e1.get() 
    k = float(k)   
    print (k * (1.8) + 32)

def mode2() :
    j = e2.get() 
    j = float(j) 
    print ((j - 32) * 0.5)
    
def exit():
    window.destroy()
    
window = Tk()

l1 = Label(window, text="섭씨")
l2 = Label(window, text="화씨")
l1.pack() # pack : Tk에 해당되는 기능 집어넣기
l2.pack()

e1 = Entry(window) # Entry : 입력창
e2 = Entry(window)
e1.pack()
e2.pack()

btn1 = Button(window, text="섭씨 -> 화씨", command = mode1)
btn2 = Button(window, text="화씨 -> 섭씨", command = mode2)
btn3 = Button(window, text="프로그램종료", command=exit)
btn1.pack()
btn2.pack()
btn3.pack()

window.mainloop()