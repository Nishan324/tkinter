from tkinter import *
bmi=Tk()
bmi.geometry("400x400")
bmi.title("Calculate the BMI")
bmi.config(background="sky blue")

l1=Label(bmi,text="Mass: ",font=('bold'),bg ="skyblue")
l1.place(x=50,y=50)
e1=Entry(bmi)
e1.place(x=120,y=55)

l2=Label(bmi,text="Height: ",font=("bold"),bg="skyblue")
l2.place(x=48,y=100)
e2=Entry(bmi)
e2.place(x=120,y=105)

def bmic():
    m=int(e1.get())
    h=int(e2.get())
    BMI=m/(h*h),"kg/cm\u00b2"

    l3=Label(bmi,text="The BMI is: ",bg="skyblue")
    l3.place(x=48,y=180)
    l4=Label(bmi,text=BMI,bg="skyblue")
    l4.place(x=130,y=180)


t1=Button(bmi,text="Calculate BMI",bg="skyblue",command=bmic)
t1.place(x=130,y=150)

bmi.mainloop()