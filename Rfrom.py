from tkinter import *
from tkinter import  messagebox
screen=Tk()
screen.title("Registration from")
screen.geometry('400x400')
screen.resizable(False,False)
def register():
    name=name_info.get()
    age=age_info.get()
    phone=phone_info.get()
    email=email_info.get()
    if name=="":
        messagebox.showerror("Errer","plese enter your name")
    elif age=="":
        messagebox.showerror("Eeere","plese enter your age")
    elif phone=="":
        messagebox.showerror("Errer","plese enter your phone no")
    elif email=="":
        messagebox.showerror("enter","plese enter your email")
    else:
        Label(screen,text='registration sussesfull',font='25',fg="green").place(x=135,y=285)
    with open(name+".txt","w")as f:
        f.write(name+"\n")
        f.write(age+"\n")
        f.write(phone+"\n")
        f.write(email+"\n")

def clear():
    name_entry.delete(0,END)
    age_entry.delete(0, END)
    phone_entry.delete(0,END)
    email_entry.delete(0, END)
#label
Label(screen,text="Registration from",font='arial 20 bold',bg='red',fg='white').pack(fill='both')

Label(screen,text="name",font="20").place(x=40,y=75)
Label(screen,text="age",font="20").place(x=40,y=115)
Label(screen,text="phone no",font="20").place(x=40,y=155)
Label(screen,text="email id",font="20").place(x=40,y=195)

#Entry boxg
name_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()


name_entry=Entry(screen,font='10',bd=4,textvariable=name_info)
name_entry.place(x=140,y=75)
age_entry=Entry(screen,font='10',bd=4,textvariable=age_info)
age_entry.place(x=140,y=115)
phone_entry=Entry(screen,font='10',bd=4,textvariable=phone_info)
phone_entry.place(x=140,y=155)
email_entry=Entry(screen,font='10',bd=4,textvariable=email_info)
email_entry.place(x=140,y=195)
#button
Button(screen,text="Register",font="20",command=register).place(x=185,y=255)
Button(screen,text="clear",font="20",command=clear).place(x=350,y=365)


mainloop()