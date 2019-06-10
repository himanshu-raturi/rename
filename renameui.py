import tkinter
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog



top = tkinter.Tk()
top.geometry("330x250+250+280")
L0 = Label(top, text="Status:ready")
L1 = Label(top, text="Path")
L3 = Label(top, text="enter the path")
L2 = Label(top, text="New name")
E2 = Entry(top, bd =3)
L4 = Label(top, text="extension")
E3 = Entry(top, bd =3)


def rename_name(name):
    i = 0
    ext = E3.get()
    for filename in os.listdir():

         dst = name+ str(i) + ext
         src = filename


         os.rename(src, dst)
         i += 1


def hellocall(st):
    st1= st
    p = messagebox.askquestion( "hello", "do you want to rename all files in folder")
    if p == 'yes':
        rename_name(st1)
        L0.config(text="Status:complete")
    else:
        top.destroy()




def loadtemplate(self):
        directoryname = filedialog.askdirectory()
        L3.config(text=directoryname)
        os.chdir( directoryname )
        L0.config(text="Status:processing")

B = tkinter.Button(top, text ="rename", width=10, command = lambda: hellocall(E2.get()) )
L0.pack()
L1.pack()
L3.pack()
B2 = tkinter.Button(top, text = "Browse", command = lambda: loadtemplate(L1), width = 10)



B2.pack()
L2.pack()
E2.pack()
L4.pack()
E3.pack()

B.pack()




# Function to rename multiple files


top.mainloop()
