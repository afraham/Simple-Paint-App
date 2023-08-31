import tkinter as tk
from tkinter import *

from brush_settings import BrushSettings
from paint_and_erase import PaintAndErase

# primary functionality / class for the paint application
class BasicPaintApp:
    def __init__(self, root):
        self.root()
        self.root.title("(Basic) Paint App")
        self.root.geometry("700x700")
    
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # from the imported classes
        self.brush_settings = BrushSettings()
        self.paint_and_erase = PaintAndErase(self.canvas, self.brush_settings)

        brush_size_label = Label(root, text="Brush Size: ")
        brush_size_label.pack()

# main
if __name__ == "__main__":
    root = Tk()
    app = BasicPaintApp(root)
    root.mainloop()



""" root = Tk()
root.title("(Basic) Paint App")
root.geometry("700x700")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

brush_size_label = Label(root, text="Brush Size: ")
brush_size_label.pack()

# Dropdown menu options
brush_width = 3
def brush_selection(selection):
        global brush_width
        brush_width = selection

brush_sizes = [
    1,
    2,
    3,
    4,
    5, 
    6,
    7,
    8,
    9,
    10
]
  
# datatype of menu text
clicked = IntVar()
clicked.set(brush_width)

# Create Dropdown menu
drop = OptionMenu(root, clicked, *brush_sizes, command=brush_selection)
drop.pack()

def paint(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", width=brush_width)

canvas.bind("<B1-Motion>", paint)

def erase(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="white", outline="white", width=brush_width)

canvas.bind("<B3-Motion>", erase)
 """
root.mainloop()
