import tkinter as tk
from tkinter import messagebox
from tkinter import *


def main():
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Chem IA")
    window.configure(bg="grey")


    def start():
        window.destroy()
        import setting
        setting()


    def options():
        window.destroy()
        op = tk.Tk()
        op.geometry("200x200")
        op.title("Help")
        op.configure(bg="grey")
        op.mainloop()
        if op.destroy:
            return main()
    
    def exit():
        window.destroy()

    button = tk.Button(window, text="Help", width= 20, height= 1, command=options).place(x=180, y=250)
    button = tk.Button(window, text="Start", width= 20, height= 1, command=start).place(x=180, y=200)
    button = tk.Button(window, text="Exit", width= 20, height= 1, command=exit).place(x=180, y=300)



    window.mainloop()

main()