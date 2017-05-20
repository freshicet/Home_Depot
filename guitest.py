#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *


def show_entry_fields():
    # 
    First_Name = e1.get()
    Last_Name = e2.get()
    email = e3.get()
    zip_Code = e4.get()
    file = open('File_INFO.txt', 'w')
    file.write(First_Name+'\n')
    file.write(Last_Name+'\n')
    file.write(email+'\n')
    file.write(zip_Code)
    file.close()
    master.destroy()


master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="E-mail").grid(row=2)
Label(master, text="Zip Code").grid(row=3)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


Button(master, text='Quit', command=master.quit).grid(
    row=7, column=0, sticky=W, pady=4)
Button(master, text='Enter', command=show_entry_fields).grid(
    row=8, column=1, sticky=W, pady=4)

name = e1.get()
mainloop()
