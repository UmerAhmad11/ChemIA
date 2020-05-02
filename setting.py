import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pyautogui

win = tk.Tk()
win.geometry("300x300")
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

mb = Menubutton(text="Type of Matter", relief=RAISED)
mb.place(x=10, y= 50)

mb.menu = Menu(mb)
mb["menu"] = mb.menu

Solid = IntVar()
Liquid = IntVar()
Gas = IntVar()

solid = mb.menu.add_checkbutton(label="Solid",variable=Solid)
liquid = mb.menu.add_checkbutton(label="Liquid",variable=Liquid)
gas = mb.menu.add_checkbutton(label="Gas",variable=Gas)


mb = Menubutton(text="Name of Substance", relief=RAISED)
mb.place(x=110, y= 48)

mb.menu = Menu(mb)
mb["menu"] = mb.menu

Zinc_Electrode = IntVar()
Copper_Electrode = IntVar()

zinc_electrode = mb.menu.add_checkbutton(label="Zinc Electrode",variable=Zinc_Electrode)
copp_electrode = mb.menu.add_checkbutton(label="Copper Electrode",variable=Copper_Electrode)

#1st Amount
mb = Menubutton(text="Amount", relief=RAISED)
mb.place(x=230, y= 48)

mb.menu = Menu(mb)
mb["menu"] = mb.menu

one = IntVar()
two = IntVar()
three = IntVar()
four = IntVar()
five = IntVar()

one = mb.menu.add_checkbutton(label="1",variable=one)
two = mb.menu.add_checkbutton(label="2",variable=two)
three = mb.menu.add_checkbutton(label="3",variable=three)
four = mb.menu.add_checkbutton(label="4",variable=four)
five = mb.menu.add_checkbutton(label="5",variable=five)

BUTTON_PRESSED = False


def drop():
    
    global count 
    global i

    mb = Menubutton(text="Type of Matter", relief=RAISED)
    mb.place(x=10, y= count)

    mb.menu = Menu(mb)
    mb["menu"] = mb.menu

    Solid = IntVar()
    Liquid = IntVar()
    Gas = IntVar()

    solid = mb.menu.add_checkbutton(label="Solid",variable=Solid)
    liquid = mb.menu.add_checkbutton(label="Liquid",variable=Liquid)
    gas = mb.menu.add_checkbutton(label="Gas",variable=Gas)

    mb = Menubutton(text="Name of Substance", relief=RAISED)
    mb.place(x=110, y= count)

    mb.menu = Menu(mb)
    mb["menu"] = mb.menu

    Zinc_Electrode = IntVar()
    Copper_Electrode = IntVar()

    zinc_electrode = mb.menu.add_checkbutton(label="Zinc Electrode",variable=Zinc_Electrode)
    copp_electrode = mb.menu.add_checkbutton(label="Copper Electrode",variable=Copper_Electrode)

    #1st Amount
    mb = Menubutton(text="Amount", relief=RAISED)
    mb.place(x=230, y= count)

    mb.menu = Menu(mb)
    mb["menu"] = mb.menu

    one = IntVar()
    two = IntVar()
    three = IntVar()
    four = IntVar()
    five = IntVar()

    one = mb.menu.add_checkbutton(label="1",variable=one)
    two = mb.menu.add_checkbutton(label="2",variable=two)
    three = mb.menu.add_checkbutton(label="3",variable=three)
    four = mb.menu.add_checkbutton(label="4",variable=four)
    five = mb.menu.add_checkbutton(label="5",variable=five)
    
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
