# class for brush settings, including the size (of the paintbrush and eraser) and colour of the paintbrush
class BrushSettings:
    def __init__(self):
        self.brush_size = 3
        self.erase_size = 3
        self.paint_colour = "black"
    
    def change_brush_size(self, size):
        self.brush_size = size

    def change_erase_size(self, size):
        self.erase_size = size
    
    def change_brush_colour(self, colour):
        self.paint_colour = colour

    
