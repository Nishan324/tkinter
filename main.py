from tkinter import *
import tkinter

window=Tk()
t=Label(window,text="username")
t.place(x=30,y=50)
e1=Entry(window).place(x=100,y=50)
p=Label(window,text="password")
p.place(x=30,y=90)
e2=Entry(window).place(x=100,y=90)
q=Button(window,text="login")
q.place(x=150, y=120)
a=Button(window,text="cancel")
a.place(x=190, y=120)

window.mainloop()