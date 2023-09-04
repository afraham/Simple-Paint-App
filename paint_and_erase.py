# class for the logic behind the paintbrush and eraser
class PaintAndErase:
    """
    This class handles the brush logic for the Tkinter painting application.
    """
    def __init__(self, canvas, brush_settings):
        """
        Initialize the PaintAndErase object.
        args:
            canvas (tkinter.Canvas): the canvas on which to paint and erase
            brush_settings (BrushSettings): the brush settings to use for painting and erasing
        """
        self.canvas = canvas
        self.brush_settings = brush_settings

    def paint(self, event):
        """
        Paint on the canvas using the current brush settings.
        args:
            event: the event containing the mouse position
        """
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, 
                                fill=self.brush_settings.paint_colour, 
                                outline=self.brush_settings.paint_colour, 
                                width=self.brush_settings.brush_size)
