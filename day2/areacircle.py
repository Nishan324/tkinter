from tkinter import*

area=Tk()
area.geometry("450x450")
box=Entry(area,fg="Dark blue")
box.place(x=165,y=20)
rad=Label(area,text="Radius Of A Circle (incm):",fg="Dark blue")
rad.place(x=10,y=20)

def areaOfCircle():
    r=int(box.get())
    ar=(22/7)*(r**2),"cm\u00b2"

    are = Label(area, text="The area of a circle is: ",font=("Arial",10,"bold"),fg="Dark blue")
    are.place(x=10, y=80)
    a=Label(area,text=ar,font=("Arial",10,"bold"),fg="Dark blue")
    a.place(x=170,y=80)



b1 = Button(area,text="Calculate The Area",fg="Dark blue",command=areaOfCircle)
b1.place(x=295,y=14)

area.mainloop()