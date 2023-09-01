import tkinter as tk
from tkinter import *

from brush_settings import BrushSettings
from paint_and_erase import PaintAndErase

# primary functionality / class for the paint application
class BasicPaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("(Basic) Paint App")
        self.root.geometry("700x700")
    
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # from the imported classes
        self.brush_settings = BrushSettings()
        self.paint_and_erase = PaintAndErase(self.canvas, self.brush_settings)

        brush_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # paintbrush size label
        brush_size_label = Label(root, text="Brush Size: ")
        brush_size_label.pack()

        clicked_brush = IntVar()
        clicked_brush.set(self.brush_settings.brush_size)

        drop_brush = OptionMenu(self.root, clicked_brush, *brush_sizes, command=self.brush_settings.change_brush_size)
        drop_brush.pack()

        self.canvas.bind("<B1-Motion>", self.paint_and_erase.paint)

        # eraser size label
        eraser_size_label = Label(root, text="Eraser Size: ")
        eraser_size_label.pack()

        clicked_erase = IntVar()
        clicked_erase.set(self.brush_settings.erase_size)

        drop_eraser = OptionMenu(self.root, clicked_erase, *brush_sizes, command=self.brush_settings.change_erase_size)
        drop_eraser.pack()

        self.canvas.bind("<B3-Motion>", self.paint_and_erase.erase)

# main
if __name__ == "__main__":
    root = Tk()
    app = BasicPaintApp(root)
    root.mainloop()
