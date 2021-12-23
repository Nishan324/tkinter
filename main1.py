#1. Registration Page using  grid method.




from tkinter import *
a=Tk()
r=Label(a,text="REGISTRATION").grid(row=0,column=10)
f=Label(a,text="firstname",).grid(row=2,column=10)
b=Entry(f).grid(row=2,column=11)
l=Label(a,text="Lastname").grid(row=3,column=10)
c=Entry(l).grid(row=3,column=11)
e=Label(a,text="EMAIL").grid(row=4,column=10)
d=Entry(e).grid(row=4,column=11)
p=Label(a,text="Password").grid(row=5,column=10)
x=Entry(p).grid(row=5,column=11)
cp=Label(a,text="Cofirm password").grid(row=6,column=10)
y=Entry(cp).grid(row=6,column=11)
z=Button(a,text="login").grid(row=7,column=10)
m=Button(a,text="cancel").grid(row=7,column=11)
a.mainloop()