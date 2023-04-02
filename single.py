import os
import re
import smtplib
import tkinter as tk
import email 
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class Singl:
    def __init__(self,s):
        self.s=s
        self.s.title("Welcome")
        self.s.geometry("800x500+300+100")

        self.a=tk.Label(self.s,text="Enter the details to send the mail")
        self.a.place(x=300,y=30)

        self.emaill=tk.Label(self.s,text="Enter the receiver's email ID:")
        self.emaill.place(x=10,y=80)
        self.email2=tk.Label(self.s,text="(if you want to send to multiple")
        self.email2.place(x=10,y=100)
        self.email3=tk.Label(self.s,text="email id's press enter in same Textbox)")
        self.email3.place(x=10,y=120)

        self.email=tk.Text(self.s,height=5,width=30)
        self.email.place(x=230,y=80)

        self.sub=tk.Label(self.s,text="Subject:")
        self.sub.place(x=10,y=180)
        self.subt=tk.Text(self.s,height=5,width=30)
        self.subt.place(x=230,y=180)
              

        self.body=tk.Label(self.s,text="Body:")
        self.body.place(x=10,y=280)
        self.bodyt=tk.Text(self.s,height=5,width=30)
        self.bodyt.place(x=230,y=280)

        self.attach=tk.Button(self.s,text="Attach a File/Image",command=self.link)
        self.attach.place(x=650,y=300)

        self.send=tk.Button(self.s,text="Send",command=self.sending)
        self.send.place(x=680,y=330)
        
        self.reset=tk.Button(self.s,text="Reset",command=self.reset1)
        self.reset.place(x=680,y=360)

        self.exit=tk.Button(self.s,text="Exit",command=self.exit)
        self.exit.place(x=680,y=390)

    def reset1(self):
        self.email.delete('1.0', END)
        self.subt.delete('1.0', END)
        self.bodyt.delete('1.0', END)
        self.names=[""]
        if self.display.winfo_exists()==True:
            self.display.destroy()    

    def exit(self):
        self.s.destroy()

    def link(self):
        self.names=list(filedialog.askopenfilenames())      
               
    def sending(self):
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.text=self.email.get("1.0",END)
        self.list=self.text.splitlines()
        c=0
        for i in self.list:
            if (re.fullmatch(self.regex,i)):
                c=c+1
        if c==len(self.list):
            self.msg=MIMEMultipart()
            self.msg['Subject']=self.subt.get("1.0",END)
            self.msg['From']=os.environ.get('USER')
            self.msg.attach(MIMEText(self.bodyt.get("1.0",END),'plain'))
            self.text=self.email.get("1.0",END)
            self.to=self.text.splitlines()
            
            if self.names is not None:
                for name in self.names:
                    try:
                        self.path=name
                        self.part = MIMEBase('application', "octet-stream")
                        self.part.set_payload( open(self.path,"rb").read() )
                        encoders.encode_base64(self.part)
                        self.part.add_header('Content-Disposition', "attachment; filename=%s" % os.path.basename(self.path))
                        self.msg.attach(self.part)
                    except:
                        messagebox.showerror("Error","Unable to attach file")
            else: 
                

                if self.subt.get("1.0",END)=="" and self.bodyt.get("1.0",END)=="" and self.filename.get("1.0",END)=="":
                        messagebox.showerror("Content not avaible","Fill the at least one field from Subject/Body/attach the file or image to send the email!")
                else:
                    try:
                        for i in self.to:
                            self.server=smtplib.SMTP('smtp.gmail.com',587)
                            self.server.starttls()
                            self.server.login(os.environ.get('USER'),os.environ.get('P'))
                            self.text=self.msg.as_string()
                            self.server.sendmail(os.environ.get('USER'), i, self.msg.as_string())
                            self.display = tk.Label(self.s,fg='green',text="Email Has Been Send Succesfully")
                            self.display.place(x=230,y=450)
                    except Exception as e:
                        messagebox.showerror(e)
        else:
            messagebox.showerror("Invalid Email ID","Please,Enter the correct format of email")
