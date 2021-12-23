from tkinter import *
import tkinter

window=Tk()
t=Label(window,text="firstname")
t.place(x=30,y=50)
e1=Entry(window).place(x=100,y=50)
p=Label(window,text="lastname")
p.place(x=30,y=80)
e2=Entry(window).place(x=100,y=80)
b=Label(window,text="email")
b.place(x=30,y=110)
e3=Entry(window).place(x=100,y=110)
b=Label(window,text="password")
b.place(x=30,y=140)
e3=Entry(window).place(x=100,y=140)
q=Button(window,text="login")
q.place(x=70, y=190)
a=Button(window,text="cancel")
a.place(x=140, y=190)

window.mainloop()