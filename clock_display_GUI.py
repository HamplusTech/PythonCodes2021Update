from tkinter import *
from tkinter.ttk import *

from time import strftime, timezone

root = Tk()
root.title("Hamplus Hub - Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font = ("consolas", 80), background = "black", foreground = "cyan")
label.pack(anchor="center")

time()

mainloop()
