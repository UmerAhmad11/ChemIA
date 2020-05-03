import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pyautogui
import pygame

win = tk.Tk()
win.geometry("400x300")
win.title("Settings of Experiment")
win.configure(bg="grey")

def back():
    win.destroy()
    import menu
    menu()

button = tk.Button(win, text="Return", width= 10, height= 1, command=back).place(x=0, y=0)



#MAIN LABEL

label = tk.Label(win, text="Edit Experiment", bg="grey", font=('Times', 12, 'bold italic')).place(x=100,y=0)


#2nd Variable

def func_orig2(value):
    print(value)
    

var = StringVar(win)
var.set("Matter")

d_1 = OptionMenu(win, var, "Solid", "Liquid", "Gas", command=func_orig2)
d_1.config(width=8)
d_1.place(x=10, y=48)



def func_orig1(value):
    print(value)
    

var = StringVar(win)
var.set("Substance")

c_1 = OptionMenu(win, var, "Zinc", "Copper", command=func_orig1)
c_1.config(width=10)
c_1.place(x=110, y=48)

#1st Amount
def func_orig(value):
    print(value)

var = StringVar(win)
var.set("Amount")

w_1 = OptionMenu(win, var, "1", "2", "3", command=func_orig)
w_1.config(font=('Helvetica', (8)))
w_1.config(width=4)
w_1.place(x=220, y=48)

check_orig = StringVar()
btn = Checkbutton(win, text="Done", variable=check_orig, onvalue=1, offvalue=0).place(x=290, y=48)
my_val = check_orig.get()
check_orig.set(0)

def drop():
    
    global count 
    global i

    def func_3(value):
        print(value)
    

    var = StringVar(win)
    var.set("Matter")

    d = OptionMenu(win, var, "Solid", "Liquid", "Gas", command=func_3)
    d.config(width=8)
    d.place(x=10, y=count)

    def func_2(value):
        print(value)
    

    var = StringVar(win)
    var.set("Substance")

    c = OptionMenu(win, var, "Zinc", "Copper", command=func_2)
    c.config(width=10)
    c.place(x=110, y=count)


    #1st Amount
    def func(value):
        print(value)

    var = StringVar(win)
    var.set("Amount")

    w = OptionMenu(win, var, "1", "2", "3", command=func)
    w.config(font=('Helvetica', (8)))
    w.config(width=4)
    w.place(x=220, y=count)

    check_1 = StringVar()
    btn_1 = Checkbutton(win, text="Done", variable=check_1, onvalue=1, offvalue=0).place(x=290, y=count)
    my_val2 = check_1.get()
    check_1.set(0)
    
    while i >= 5:
        button_1.configure(state=DISABLED)
    i += 1
    count+=38
    return 0

count = 85
i = 1


 



button_1 = tk.Button(win, text="Add", width=5, height=1, command=drop).place(x=125,y=270)

win.mainloop()
'''
if pyautogui.locateCenterOnScreen('Capture.png'):
    print("located")



   new=tk.Tk()
    new.title("Are you sure you want to quit?")
    def close():
        new.destroy()
        win.destroy()
    def close_two():
        new.destroy()
    btn = tk.Button(new, text="Yes", command=close).place(x=20,y=20)
    btn = tk.Button(new, text="No", command=close_two).place(x=20,y=60)
    new.mainloop()
    '''
