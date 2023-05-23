from tkinter import *
window = Tk()

# 입력창.insert (0, ~~~) : 입력창을 활성시키면 입력창에 ~~~가 나옴

def mode1() :
    k = e1.get() # e1에 Entry한 값을 k에 저장
    k = float(k) # data comport (형변환)해줘야 함. 왜냐하면 Entry에서 얻은 값은 항상 String이기 때문
    e2.insert(0, k * (1.8) + 32)

def mode2() :
    j = e2.get() # e2에 Entry한 값을 j에 저장
    j = float(j) 
    e1.insert(0, j - 32 * 0.5)

def erase() :
    e1.delete(0, END) # tkinter에서 무언가를 지울 때 사용하는 함수
    e2.delete(0, END)
 
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

btn1 = Button(window, text="화씨 -> 섭씨", command=mode1)
btn2 = Button(window, text="섭씨 -> 화씨", command=mode2)
btn3 = Button(window, text="지우기", command=erase)
btn4 = Button(window, text="프로그램종료", command=exit)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btn4.grid(row=2, column=3)

window.mainloop()