from tkinter import*

area=Tk()
area.geometry("450x450")
area.title("Area Of Triangle")

rad=Label(area,text="Base of a triangle (incm):",fg="red")
rad.place(x=10,y=20)
box1=Entry(area,fg="red")
box1.place(x=165,y=20)

rad=Label(area,text="Height of a triangle (incm):",fg="red")
rad.place(x=10,y=40)
box2=Entry(area,fg="red")
box2.place(x=165,y=40)

def areaOfTriangle():
    b=int(box1.get())
    h=int(box2.get())
    ar=(1/2)*b*h,"cm\u00b2"

    are = Label(area, text="The area of a triangle is: ",font=("Arial",10,"bold"),fg="red")
    are.place(x=10, y=130)
    a=Label(area,text=ar,font=("Arial",10,"bold"),fg="red")
    a.place(x=170,y=130)



b1 = Button(area,text="Calculate The Area",fg="red",command=areaOfTriangle)
b1.place(x=150,y=80)


area.mainloop()