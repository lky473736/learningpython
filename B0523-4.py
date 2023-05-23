from tkinter import *
window = Tk()

def changeimg () :
    k = entry.get()
    img = PhotoImage (file = k)
    imagelabel.configure (image = img)
    imagelabel.image = img
    
rabbit = PhotoImage (file = "/Users/alphastation/Desktop/컴퓨터공학전공/repository/learningpython/img/rabbit.GIF")
imagelabel = Label (window, image = rabbit)
imagelabel.pack()

text = Label (window, text = "아래에 경로 입력")
text.pack()

entry = Entry (window, bg = "lightgray", fg = "white")
entry.pack()

button = Button (window, text = "submit", command = changeimg)
button.pack()

window.mainloop()