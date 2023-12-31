import tkinter as tk
from tkinter.colorchooser import askcolor
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

        # Add a button to switch between paintbrush and eraser
        self.mode_button = Button(root, text="Switch to Eraser", command=self.toggle_mode)
        self.mode_button.pack()
        self.current_mode = 0
        # functionality for paintbrush
        self.canvas.bind("<B1-Motion>", self.paint_and_erase.paint)

        # settings to change brush size
        brush_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        brush_size_label = Label(root, text="Brush Size: ")
        brush_size_label.pack()

        clicked_brush = IntVar()
        clicked_brush.set(self.brush_settings.brush_size)

        drop_brush = OptionMenu(self.root, clicked_brush, *brush_sizes, command=self.brush_settings.change_brush_size)
        drop_brush.pack()

        # clear canvas button
        self.clear_button = Button(root, text="Clear Canvas", command=lambda: self.canvas.delete("all"))
        self.clear_button.pack()



    def toggle_mode(self):
        """
        Toggle between the paintbrush and eraser modes.
        """
        if self.current_mode == 0:
            self.mode_button.config(text="Paintbrush")
            self.current_mode = 1
            self.brush_settings.change_brush_colour("white")
        else:
            self.mode_button.config(text="Eraser")
            self.brush_settings.change_brush_colour("black")
            self.current_mode = 0

# main
if __name__ == "__main__":
    root = Tk()
    app = BasicPaintApp(root)
    root.mainloop()
