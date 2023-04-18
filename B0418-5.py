import turtle

t = turtle.Turtle()

slist = []

def in_vals() :
    global counts
    counts = int(turtle.textinput("", "counts?"))
    for i in range (counts) :
        val_s = float(turtle.textinput("", "data?"))
        slist.append(val_s)
    
def drawgraph() :
    for i in range (counts) :
        t.left(90)
        t.fd(slist[i])
        t.write(slist[i])
        t.rt(90)
        t.fd(30)
        t.rt(90)
        t.fd(slist[i])
        t.left(90)
                
in_vals()
drawgraph()

turtle.mainloop()