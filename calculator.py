from tkinter import *
window=Tk()
window.geometry("400x300")
w=Label(window,text="calculator",fg="green")
w.grid(row=0,column=1)

A=Entry(window).grid(row=3,column=1)

B=Button(window,text="1",fg="brown")
B.grid(row=5,column=0)

C=Button(window,text="2",fg="brown")
C.grid(row=5,column=1)

D=Button(window,text="3",fg="brown")
D.grid(row=5,column=2)

E=Button(window,text="4",fg="brown")
E.grid(row=6,column=0)

f=Button(window,text="5",fg="brown")
f.grid(row=6,column=1)

g=Button(window,text="6",fg="brown")
g.grid(row=6,column=2)

H=Button(window,text="7",fg="brown")
H.grid(row=7,column=0)

i=Button(window,text="8",fg="brown")
i.grid(row=7,column=1)

j=Button(window,text="9",fg="brown")
j.grid(row=7,column=2)

k=Button(window,text="0",fg="brown")
k.grid(row=8,column=1)

l=Button(window,text="X",fg="brown")
l.grid(row=8,column=2)

m=Button(window,text="%",fg="brown")
m.grid(row=8,column=0)

N=Button(window,text="+",fg="brown")
N.grid(row=5,column=3)

o=Button(window,text="-",fg="brown")
o.grid(row=6,column=3)

p=Button(window,text="/",fg="brown")
p.grid(row=7,column=3)

q=Button(window,text="=",fg="brown")
q.grid(row=8,column=3)









window.mainloop()