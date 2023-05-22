from tkinter import *
window = Tk()

def ftoc():
    pass

def ctof():
    pass
 
def exit():
    window.destroy()
    
l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0) # grid : 표 만들기
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

btn1 = Button(window, text="화씨 -> 섭씨", command=ftoc)
btn2 = Button(window, text="섭씨 -> 화씨", command=ctof)
btn3 = Button(window, text="프로그램종료", command=exit)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)

window.mainloop()

# grid 배치는 아래와 같음
# 0 : "화씨" / 1 : 입력창 / 2 : "화씨 -> 섭씨"
# 0 : "섭씨" / 1 : 입력창 / 2 : "섭씨 -> 화씨"