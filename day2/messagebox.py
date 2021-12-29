from tkinter import *
from tkinter import messagebox

avi=Tk()
avi.geometry("400x400")
user= Label(text="username")
user.place(x=40,y=60)
em=Entry(avi)
em.place(x=180,y=60)

pasd=Label(text="passowrd").place(x=40,y=80)
pas=Entry(avi,show="*").place(x=180,y=80)

def logg():
    un=em.get()
    messagebox.showinfo(title="login",message=un)
log=Button(avi,text="Login",command=logg)
log.place(x=150,y=130)
sig=Button(avi,text="signup").place(x=193,y=130)
fg=Button(avi,text="Forgot your Password?").place(x=125,y=160)
avi.mainloop()