# class for brush settings, including the size (of the paintbrush and eraser) and colour of the paintbrush
class BrushSettings:
    """
    This class manages brush settings for the Tkinter painting application.
    Allows changing brush size, eraser size, and brush color.
    """
    def __init__(self):
        """
        Initialize brush settings with default values.
        """
        self.brush_size = 3
        self.erase_size = 3
        self.paint_colour = "black"
    
    def change_brush_size(self, size):
        """
        Changes the size of the brush.
        args:
            size (int): new brush size
        """
        self.brush_size = size

    def change_erase_size(self, size):
        """
        Changes the size of the eraser.
        args:
            size (int): new eraser size
        """
        self.erase_size = size
    
    def change_brush_colour(self, colour):
        """
        Changes the colour of the brush.
        args:
            colour (str): new brush color
        """
        self.paint_colour = colour
