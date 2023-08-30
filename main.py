import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.title("Paint App")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

def paint(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", width=2)

canvas.bind("<B1-Motion>", paint)

def choose_color():
    color = askcolor(color="black")[1]
    canvas["bg"] = color

color_button = ttk.Button(root, text="Choose Color", command=choose_color)
color_button.pack()

def clear_canvas():
    canvas.delete("all")

clear_button = ttk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

root.mainloop()
