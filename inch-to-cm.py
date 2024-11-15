import tkinter as tk
from tkinter import font
import os.path

me = os.path.abspath(__file__)
mydir = os.path.dirname(me)

def win():
    def convert():
        number = int(entry.get())
        if number:
            inch = number * 2.54
            label4.config(text=str(inch)+"cm")
    r = tk.Tk()
    bold = font.Font(family="Helvetica", weight="bold")
    r.title("Inch-To-CM")
    r.geometry("540x260")
    r.config(bg="gray")
    photo = os.path.join(mydir, "baner.png")
    if os.path.exists(photo):
        photoi = tk.PhotoImage(file=photo)
        label = tk.Label(r, image=photoi)
        label.pack()
    else:
        pass

    frame = tk.Frame()
    frame.config(bg="gray")

    label2 = tk.Label(frame, text="Inches:", bg="gray", fg="white", font=bold)
    label3 = tk.Label(frame, text=" → ", bg="gray")
    label2.grid(column=0, row=0)
    label3.grid(column=2, row=0)
    label4 = tk.Label(frame, text="output", fg="yellow", bg="gray", font=bold)
    label4.grid(column=3, row=0)

    entry = tk.Entry(frame)
    entry.grid(column=1, row=0)

    frame.pack(pady=20)

    button = tk.Button(r, text="convert", command=convert)
    button.pack()

    r.resizable(False, False)
    r.mainloop()

win()
