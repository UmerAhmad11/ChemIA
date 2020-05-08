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
    

var_orig = StringVar(win)
var_orig.set("Matter")

d_1 = OptionMenu(win, var_orig, "Solid", "Liquid", "Gas", command=func_orig2)
d_1.config(width=8)
d_1.place(x=10, y=48)



def func_orig1(value):
    print(value)
    

var_orig1 = StringVar(win)
var_orig1.set("Substance")

c_1 = OptionMenu(win, var_orig1, "Zinc", "Copper", command=func_orig1)
c_1.config(width=10)
c_1.place(x=110, y=48)

#1st Amount
def func_orig(value):
    print(value)

var_orig2 = StringVar(win)
var_orig2.set("Amount")

w_1 = OptionMenu(win, var_orig2, "1", "2", "3", command=func_orig)
w_1.config(font=('Helvetica', (8)))
w_1.config(width=4)
w_1.place(x=220, y=48)

def done_orig():
    global result_1
    if var_orig.get() == "Solid" and var_orig1.get() == "Zinc" and var_orig2.get() == "1":
        result_1 = True
    else:
        result_1 = False
    global result_2
    if var_orig.get() == "Solid" and var_orig1.get() == "Zinc" and var_orig2.get() == "2":
        result_2 = True
    else:
        result_2 = False
    global result_3
    if var_orig.get() == "Solid" and var_orig1.get() == "Zinc" and var_orig2.get() == "3":
        result_3 = True
    else:
        result_3 = False
    if var_orig.get() == "Solid" and var_orig1.get() == "Copper" and var_orig2.get() == "1":
        print("Hi1")
    if var_orig.get() == "Solid" and var_orig1.get() == "Copper" and var_orig2.get() == "2":
        print("Hi2")
    if var_orig.get() == "Solid" and var_orig1.get() == "Copper" and var_orig2.get() == "3":
        print("Hi3")
    if var_orig.get() == "Liquid" and var_orig1.get() == "Zinc" and var_orig2.get() == "1":
        print("Goodbye1")
    if var_orig.get() == "Liquid" and var_orig1.get() == "Zinc" and var_orig2.get() == "2":
        print("Goodbye2")
    if var_orig.get() == "Liquid" and var_orig1.get() == "Zinc" and var_orig2.get() == "3":
        print("Goodbye3")
    if var_orig.get() == "Liquid" and var_orig1.get() == "Copper" and var_orig2.get() == "1":
        print("bye1")
    if var_orig.get() == "Liquid" and var_orig1.get() == "Copper" and var_orig2.get() == "2":
            print("bye2")
    if var_orig.get() == "Liquid" and var_orig1.get() == "Copper" and var_orig2.get() == "3":
        print("bye3")
    if var_orig.get() == "Gas" and var_orig1.get() == "Zinc" and var_orig2.get() == "1":
        print("Goodnight1")
    if var_orig.get() == "Gas" and var_orig1.get() == "Zinc" and var_orig2.get() == "2":
        print("Goodnight2")
    if var_orig.get() == "Gas" and var_orig1.get() == "Zinc" and var_orig2.get() == "3":
        print("Goodnight3")
    if var_orig.get() == "Gas" and var_orig1.get() == "Copper" and var_orig2.get() == "1":
        print("Goodmorning1")
    if var_orig.get() == "Gas" and var_orig1.get() == "Copper" and var_orig2.get() == "2":
        print("Goodmorning2")
    if var_orig.get() == "Gas" and var_orig1.get() == "Copper" and var_orig2.get() == "3":
        print("Goodmorning3")

check_orig = StringVar()
btn = Checkbutton(win, text="Done", variable=check_orig, onvalue=1, offvalue=0, command=done_orig).place(x=290, y=48)
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
    

    var_1 = StringVar(win)
    var_1.set("Substance")

    c = OptionMenu(win, var_1, "Zinc", "Copper", command=func_2)
    c.config(width=10)
    c.place(x=110, y=count)


    #1st Amount
    def func(value):
        print(value)

    var_2 = StringVar(win)
    var_2.set("Amount")

    w = OptionMenu(win, var_2, "1", "2", "3", command=func)
    w.config(font=('Helvetica', (8)))
    w.config(width=4)
    w.place(x=220, y=count)

    def done():
        global result_1
        if var.get() == "Solid" and var_1.get() == "Zinc" and var_2.get() == "1":
            result_1 = True
        else:
            result_1 = False
        global result_2
        if var.get() == "Solid" and var_1.get() == "Zinc" and var_2.get() == "2":
            result_2 = True
        else:
            result_2 = False
        global result_3
        if var.get() == "Solid" and var_1.get() == "Zinc" and var_2.get() == "3":
            result_3 = True
        else: 
            result_3 = False
        if var.get() == "Solid" and var_1.get() == "Copper" and var_2.get() == "1":
            print("Hi1")
        if var.get() == "Solid" and var_1.get() == "Copper" and var_2.get() == "2":
            print("Hi2")
        if var.get() == "Solid" and var_1.get() == "Copper" and var_2.get() == "3":
            print("Hi3")
        if var.get() == "Liquid" and var_1.get() == "Zinc" and var_2.get() == "1":
            print("Goodbye1")
        if var.get() == "Liquid" and var_1.get() == "Zinc" and var_2.get() == "2":
            print("Goodbye2")
        if var.get() == "Liquid" and var_1.get() == "Zinc" and var_2.get() == "3":
            print("Goodbye3")
        if var.get() == "Liquid" and var_1.get() == "Copper" and var_2.get() == "1":
            print("bye1")
        if var.get() == "Liquid" and var_1.get() == "Copper" and var_2.get() == "2":
            print("bye2")
        if var.get() == "Liquid" and var_1.get() == "Copper" and var_2.get() == "3":
            print("bye3")
        if var.get() == "Gas" and var_1.get() == "Zinc" and var_2.get() == "1":
            print("Goodnight1")
        if var.get() == "Gas" and var_1.get() == "Zinc" and var_2.get() == "2":
            print("Goodnight2")
        if var.get() == "Gas" and var_1.get() == "Zinc" and var_2.get() == "3":
            print("Goodnight3")
        if var.get() == "Gas" and var_1.get() == "Copper" and var_2.get() == "1":
            print("Goodmorning1")
        if var.get() == "Gas" and var_1.get() == "Copper" and var_2.get() == "2":
            print("Goodmorning2")
        if var.get() == "Gas" and var_1.get() == "Copper" and var_2.get() == "3":
            print("Goodmorning3")



    check_1 = StringVar()
    btn_1 = Checkbutton(win, text="Done", variable=check_1, onvalue=1, offvalue=0, command=done).place(x=290, y=count)
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

def tick():
    check_2.set(1)

check_2 = StringVar()
btn_2 = Checkbutton(win, text="Done", variable=check_2, onvalue=1, offvalue=0, command=tick).place(x=340, y=240)
my_val3 = check_2.get()
check_2.set(0)


def go():
    pygame.init()
    screen = pygame.display.set_mode((430,410))
    white = [255, 255, 255]
    red = [255, 0, 0]
    screen.fill(white)
    FPS = 30
    pygame.display.update()

    if check_2.get() == "1":    
        
        if result_1 == True:
            head = pygame.Rect(20, 20, 60, 60)
            pygame.draw.rect(screen, (255, 50, 50), head)

        elif result_1 == False:
            pass

        if result_2 == True:
            head = pygame.Rect(80, 80, 60, 60)
            pygame.draw.rect(screen, (255, 50, 50), head)
            head = pygame.Rect(180, 80, 60, 60)
            pygame.draw.rect(screen, (255, 50, 50), head) 

        elif result_2 == False:
            pass

        if result_3 == True:
            head = pygame.Rect(80, 180, 60, 60)
            pygame.draw.rect(screen, (255, 50, 50), head)
            head = pygame.Rect(180, 280, 60, 60)
            pygame.draw.rect(screen, (255, 50, 50), head)
            head = pygame.Rect(130, 280, 60, 60)
            pygame.draw.rect(screen, (255, 50, 50), head)

        elif result_3 == False:
            pass
              
    else:
        print("Sorry")

    head_dragging = False

    pygame.display.update() 

    clock = pygame.time.Clock()   

    run = True
    while run:  
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    if head.collidepoint(event.pos):
                        head_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = head.x - mouse_x
                        offset_y = head.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    head_dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if head_dragging:
                    mouse_x, mouse_y = event.pos
                    head.x = mouse_x + offset_x
                    head.y = mouse_y + offset_y
            
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (255, 0, 0), head)
        pygame.display.flip()

            
    pygame.display.update()

    pygame.quit()


button_2 = tk.Button(win, text="Create", width=5, height=1, command=go).place(x=350,y=150)


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
