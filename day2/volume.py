from tkinter import *
vol=Tk()
vol.geometry("600x600")
vol. title("Volume_cube_Cuboid")
vol.config(background="skyblue")

l=Label(vol,text="length of a cube(incm):",fg="red")
l.place(x=10,y=20)
e1=Entry(vol,fg="red")
e1.place(x=165,y=20)

l2=Label(vol,text="length of a cuboid(incm):",fg="red")
l2.place(x=10,y=300)
e2=Entry(vol,fg="red")
e2.place(x=165,y=300)

b1=Label(vol,text="breadth of a cuboid(incm):",fg="red")
b1.place(x=10,y=330)
e3=Entry(vol,fg="red")
e3.place(x=165,y=330)

h1=Label(vol,text="height of a cuboid(incm):",fg="red")
h1.place(x=10,y=360)
e4=Entry(vol,fg="red")
e4.place(x=165,y=360)

def volofcube():
    l=int(e1.get())
    v=l**3,"cm\u00b3"

    are = Label(vol, text="The vol of a cube is: ",font=("Arial",10,"bold"),fg="red")
    are.place(x=10, y=130)
    a=Label(vol,text=v,font=("Arial",10,"bold"),fg="red")
    a.place(x=170,y=130)


def volofcuboid():
    l=int(e2.get())
    b=int(e3.get())
    h=int(e4.get())
    v=l*b*h,"cm\u00b3"

    are = Label(vol, text="The vol of a cuboi is: ",font=("Arial",10,"bold"),fg="red")
    are.place(x=10, y=450)
    a=Label(vol,text=v,font=("Arial",10,"bold"),fg="red")
    a.place(x=170,y=450)


b1 = Button(vol,text="Calculate The vol of cube",fg="red",command=volofcube,bg="skyblue")
b1.place(x=150,y=80)

b1 = Button(vol,text="Calculate The vol of cuboid",fg="red",command=volofcuboid,bg="skyblue")
b1.place(x=150,y=400)

vol.mainloop()



vol.mainloop()