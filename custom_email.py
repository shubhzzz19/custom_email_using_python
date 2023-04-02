from single import *
from test import *
import os
from tkinter import *
import tkinter as tk
#from PIL import Image,ImageTk
from tkinter import messagebox
u="s"
p="s"
class Login_in:
    def __init__(self,win):
        self.win=win
        self.win.title("Custom Email Using Python")
        self.win.geometry("400x400+500+100")
        self.l=tk.Label(self.win,text="Login Page")
        self.l.place(x=150,y=10)

        self.l1=tk.Label(self.win,text="Enter Username:")
        self.l1.place(x=10,y=80)
        self.user=tk.Entry(self.win,width=30)
        self.user.place(x=150,y=80)

        self.l2=tk.Label(self.win,text="Enter Password:")
        self.l2.place(x=10,y=110)
        self.pass1=tk.Entry(self.win,width=30,show="*")
        self.pass1.place(x=150,y=110)

        self.login_button=tk.Button(self.win,text="Log-in",command=self.login)
        self.login_button.place(x=30,y=140)
        self.login_exit=tk.Button(self.win,text="Exit",command=self.exit)
        self.login_exit.place(x=150,y=140)
        

    def login(self): 
        if u==u and p==p:
            win.destroy()
            s=Tk()
            app=Singl(s)
            s.mainloop()
        else:
            messagebox.showerror("Invalid","Please enter valid Username or Password!")

    def exit(self):
        win.destroy()


win=Tk()
app=Login_in(win)
win.mainloop()


