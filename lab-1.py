from tkinter import *

root=Tk()
e1=Entry(root)
e1.pack()

def clickaction():
    textoutput=e1.get()
    t1=Label(root,text=textoutput)
    t1.pack()

b1=Button(root,text="click",command=clickaction)
b1.pack()
root.mainloop()