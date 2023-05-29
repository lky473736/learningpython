# 메모장 만들기

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

window = Tk()
text = Text(window, height = 30, width = 80)
text.pack()

def open() : # 파일 열기
    file = filedialog.askopenfile(parent = window, mode = 'r') # 파일 탐색 후 열기기능
    if file != None : # 파일이 비어있지 않다면 (용량이 있다면)
        lines = file.read() # 파일 읽기
        text.insert('1.0', lines) # 1.0 : 줄간격, window에 텍스트 넣기
        file.close()
    
def save() :
    file = filedialog.asksavefile(parent = window, mode = 'w') # 파일 탐색 후 저장기능
    if file != None : # 파일이 비어있지 않다면 (용량이 있다면)
        lines = text.get('1.0', END+'-1c') # 파일 쓰기
        file.write(lines)
        file.close()
    
def exit() :
    if messagebox.askokcancel("Quit", "종료하시겠습니까?") : # 종료할지 묻는 박스
        window.destroy()

def about() :
    label = messagebox.showinfo ("About", "메모장 프로그램") # 메세지 박스가 뜸 (About : 창 이름)

menu = Menu (window) # 상단 표시줄 만들기
window.config(menu = menu)

filemenu = Menu (menu)
menu.add_cascade(label = "파일", menu = filemenu) # 메뉴의 이름 짓기
filemenu.add_command(label = "열기", command = open)
filemenu.add_command(label = "저장하기", command = save)

helpmenu = Menu (menu)
menu.add_cascade(label = "도움말", menu = helpmenu)
helpmenu.add_command(label = "프로그램 정보", command = about) # 메뉴 안 커맨드 만들기

exitmenu = Menu (menu)
menu.add_cascade(label = "시스템", menu = exitmenu) # 종료
exitmenu.add_command(label = "종료", command = exit)

window.mainloop()