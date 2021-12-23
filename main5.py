#login page via grid
from tkinter import*
a=Tk()
b=Label(a,text="login page").grid(row=0,column=0)
d=Label(a,text="username").grid(row=4,column=0)
c=Entry(d).grid(row=4,column=1)
e=Label(a,text="password").grid(row=6,column=0)
f=Entry(e).grid(row=6,column=1)
g=Button(a,text="FORGET PASSWORD").grid(row=8,column=1)
a.mainloop()