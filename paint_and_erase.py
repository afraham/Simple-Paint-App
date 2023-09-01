# class for the logic behind the paintbrush and eraser
class PaintAndErase:
    def __init__(self, canvas, brush_settings):
        self.canvas = canvas
        self.brush_settings = brush_settings

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, 
                                fill=self.brush_settings.paint_colour, 
                                width=self.brush_settings.brush_size)
    
    def erase(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, 
                                fill="white", 
                                outline="white", 
                                width=self.brush_settings.erase_size)
