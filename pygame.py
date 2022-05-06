from ast import Str
from email import message
from signal import raise_signal
import string
from tkinter import *
from tkinter import messagebox
from turtle import left, position, right
import re
from tkinter.messagebox import showinfo

def open_click():
    Doordash    =   open("doordashlog.txt", "r")
    dash=   Doordash.read()
    
    DoorDash_window_Editor.insert(END, dash)
    Doordash.close()

def add_click():

        file = open("doordashlog.txt","w")
    
        print(firstName,lastName,base_pay,bonus_pay,peak_pay)

        
        #if not re.match("^[a-z]*$"):
        #   firstName_text  =   first_name_entry.get()
        #   lastName_text   =    last_name_entry.get()
            #raise TypeError("input needs to be letter")
        #if not re.match("^[0-1000]*$"):    
        #   base_pay_text   =   base_pay_entry.get()
        #   bonus_pay_text  =   bonus_pay_entry.get()
        #   peak_pay_text   =   peak_pay_entry.get()
            #raise TypeError("Input needs to be number")
        try:
                string(first_name_entry.get())
                string(last_name_entry.get())
                int(base_pay_entry.get())
                int(bonus_pay_entry.get())
                int(peak_pay_entry.get())

        except BaseException:
               print("Please enter a correct number or Name")

        file.write( "\n")
        file.write("First Name " +  first_name_entry.get())
        file.write( "\n")
        file.write("Last Name " +  last_name_entry.get())
        file.write( "\n")
        file.write("Base Pay " +  base_pay_entry.get())
        file.write( "\n")
        file.write("Bonus Pay " +  bonus_pay_entry.get())
        file.write( "\n")
        file.write("Peak Hour Pay " +   peak_pay_entry.get())
        file.write( "\n")
        
        
        file.close()  
 
# root window
root = Tk()

root.geometry("500x600")
root.title('DoorDash Revenue')
 
heading = Label(text="Doordash Revenue Calculator",fg="black",bg="dark gray",width="300",height="3",font=('Garamond', 11) )
heading.pack()

firstName   =   StringVar()
lastName    =   StringVar()
base_pay  = IntVar()
bonus_pay   =   IntVar()
peak_pay    =   IntVar()
    
firstname_text = Label(text="FirstName : ")
firstname_text.place(x=15,y=60)
first_name_entry = Entry(textvariable=firstName,width="20")
first_name_entry.place(x=15,y=80)

lastname_text = Label(text="LastName : ")
lastname_text.place(x=15,y=100)
last_name_entry = Entry(textvariable=lastName,width="20")
last_name_entry.place(x=15,y=120)


base_pay_text = Label(text="Base Pay : ")
base_pay_text.place(x=15,y=140)
base_pay_entry = Entry(textvariable=base_pay,width="20")
base_pay_entry.place(x=15,y=160)


bonus_pay_text = Label(text="Bonus and Tip : ")
bonus_pay_text.place(x=15,y=180)
bonus_pay_entry = Entry(textvariable=bonus_pay,width="20")
bonus_pay_entry.place(x=15, y=200)

peak_pay_text = Label(text="Peak hour pay : ")
peak_pay_text.place(x=15,y=220)
peak_pay_entry = Entry(textvariable=peak_pay,width="20")
peak_pay_entry.place(x=15,y=240)

DoorDash_window_Editor = Text(root, width=40, height=50, font=('Garamond', 12))
scroll_y = Scrollbar(DoorDash_window_Editor)
scroll_y.place(x=290,y=250)
DoorDash_window_Editor.place(x=190, y=60)

open_window_button= Button(root,text="Open Door Dash File", command=open_click)
open_window_button.place(x=15,y=350)

Submit_button = Button(root,text="Update File",width="15",height="2",command=add_click)
Submit_button.place(x=15,y=290)


footer = Label(text=" ",fg="black",bg="dark gray",width="200",height="2")
footer.place(x=0, y=570)

mainloop()