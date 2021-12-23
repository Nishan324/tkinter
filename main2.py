#1. Registration Page using  place

from tkinter import *
a=Tk()
a.geometry('200x200')
r=Label(a,text="REGISTRATION").place(x=0,y=0)
f=Label(a,text="firstname",).place(x=0,y=20)
b=Entry(f).place(x=70,y=20)
l=Label(a,text="Lastname").place(x=0,y=40)
c=Entry(l).place(x=70,y=40)
e=Label(a,text="EMAIL").place(x=0,y=60)
d=Entry(e).place(x=70,y=60)
p=Label(a,text="Password").place(x=0,y=80)
x=Entry(p).place(x=70,y=80)
cp=Label(a,text="Cofirm password").place(x=0,y=100)
y=Entry(cp).place(x=100,y=100)
z=Button(a,text="login").place(x=50,y=120)
m=Button(a,text="cancel").place(x=100,y=120)
a.mainloop()