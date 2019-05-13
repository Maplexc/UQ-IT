# A simple drawing app

import tkinter as tk 
from tkinter import colorchooser
from tkinter import font


NORMAL_COLOUR = 'grey90'
SELECTED_COLOUR = 'grey80'

# You can think of the toolbar (or probably anything that inherits from a Frame) as a widget

class Toolbar(tk.Frame):
    """The toolbar for DrawingApp"""

    def __init__(self, master, parent):
        """Create the toolbar:
        master - the toplevel window
        parent - the app object
        """
        
        super().__init__(master)
        self.parent = parent
        self.rect = tk.Button(self, text="Rectangle", command = self.set_rect,
                              bg = SELECTED_COLOUR)
        self.rect.pack(side=tk.LEFT,padx=2, pady=2)
        self.oval = tk.Button(self, text="Oval", command = self.set_oval,
                              bg = NORMAL_COLOUR)
        self.oval.pack(side=tk.LEFT,padx=2, pady=2)
        self.polygon = tk.Button(self, text="Polygon", command = self.set_poly,
                                 bg = NORMAL_COLOUR)
        self.polygon.pack(side=tk.LEFT,padx=2, pady=2)
        self.line = tk.Button(self, text="Line", command = self.set_line,
                              bg = NORMAL_COLOUR)
        self.line.pack(side=tk.LEFT,padx=2, pady=2)
        self.text = tk.Button(self, text="Text", command = self.set_text,
                              bg = NORMAL_COLOUR)
        self.text.pack(side=tk.LEFT,padx=2, pady=2)
        self.move = tk.Button(self, text="Move", command = self.set_move,
        bg = NORMAL_COLOUR)
        self.move.pack(side=tk.LEFT,padx=2, pady=2)
        self.deletebutton = tk.Button(self, text="Delete",
                                      command = self.set_delete,
                                      bg = NORMAL_COLOUR)
        self.deletebutton.pack(side=tk.LEFT,padx=2, pady=2)
        self.selected = self.rect

    def change_selected(self, button):
        """Change button colours for change of selection."""
        self.selected.config(bg=NORMAL_COLOUR)
        button.config(bg=SELECTED_COLOUR)
        self.selected=button
        
    def set_rect(self):
        """Set the rectangle selection."""
        self.change_selected(self.rect)
        self.parent.set_rect()
                             
    def set_oval(self):
        """Set the oval selection."""
        self.change_selected(self.oval)
        self.parent.set_oval()
                             
    def set_poly(self):
        """Set the polygon selection."""
        self.change_selected(self.polygon)
        self.parent.set_poly()
        
    def set_line(self):
        """Set the polyline selection."""
        self.change_selected(self.line)
        self.parent.set_line()

    def set_text(self):
        """Set the text selection."""
        self.change_selected(self.text)
        self.parent.set_text()

    def set_move(self):
        """Set the move selection."""
        self.change_selected(self.move)
        self.parent.set_move()

    def set_delete(self):
        """Set the delete selection."""
        self.change_selected(self.deletebutton)
        self.parent.set_delete()
                             

                             
# Another widget

class Configuration(tk.Frame):
    """The configurations bar for DrawingApp"""
    
    def __init__(self, master):
        """Create the configuration bar:
        master - the toplevel window
        """
        
        super().__init__(master)
        self.fillc = tk.Button(self, text="Pick Fill Colour",
                               command = self.sef_fill_colour, bg="white")
        self.fillc.pack(side=tk.LEFT,padx=2, pady=2)
        self.outc = tk.Button(self, text="Pick Outline Colour",
                              command = self.set_outline_colour, bg = "white")
        self.outc.pack(side=tk.LEFT,padx=2, pady=2)
        self.linec = tk.Button(self, text="Pick Line Colour",
                               command = self.set_line_colour, bg = "white")
        self.textc = tk.Button(self, text="Pick Text Colour",
                               command = self.set_text_colour, bg = "white")
        self.line_width_label = tk.Label(self,text="Line width: ")
        self.line_width_scale = \
                                tk.Spinbox(self, from_=1,to=50,width = 5,
                                           command = self.set_line_width, 
                                           state=tk.DISABLED)
        self.line_width_scale.bind("<Return>", self.set_line_width_return)
        self.current_configs = [self.fillc, self.outc]
        self.line_colour = 'white'
        self.fill_colour = 'white'
        self.text_colour = 'white'
        self.line_width = 1
        
    def set_configs(self, items):
        """Disable widgets for previous config and enable widgets for new
        config items is the list of new widgets."""

        if self.line_width_scale in self.current_configs:
            self.line_width_scale.configure(state=tk.DISABLED)
        for b in self.current_configs: b.pack_forget()
        for i in items:
            i.pack(side=tk.LEFT,padx=2, pady=2)
        self.current_configs = items

    def set_fill_configs(self):
        """Set the config widgets for rectangles, ovals and polygons."""
        self.set_configs([self.fillc, self.outc])

    def set_text_configs(self):
        """Set the text config widgets"""
        self.set_configs([self.textc])

    def set_line_configs(self):
        """Set the line config widgets"""
        self.set_configs([self.linec,self.line_width_label,
                         self.line_width_scale])
        self.line_width_scale.configure(state=tk.NORMAL)

    def hide_configs(self):
        """Hide all config widgets."""
        self.set_configs([])

    def sef_fill_colour(self):
        """Choose fill colour."""
        _, colour = colorchooser.askcolor(self.fill_colour, 
                                          title="Choose Fill Colour")
        if colour:
            self.fill_colour = colour
            self.fillc.configure(bg= colour)
            
    def set_outline_colour(self):
        """Choose outline colour."""
        _, colour = colorchooser.askcolor(self.line_colour, 
                                          title="Choose Outline Colour")
        if colour:
            self.line_colour = colour
            self.outc.configure(bg= colour)
            self.linec.configure(bg= colour)
            
    def set_line_colour(self):
        """Choose line colour"""
        _, colour = colorchooser. askcolor(self.line_colour, 
                                           title="Choose Line Colour")
        if colour:
            self.line_colour = colour
            self.outc.configure(bg= colour)
            self.linec.configure(bg= colour)

    def set_text_colour(self):
        """Choose text colour."""
        _, colour = colorchooser.askcolor(self.text_colour, 
                                          title="Choose Text Colour")
        if colour:
            self.text_colour = colour
            self.textc.configure(bg= colour)

    def set_line_width(self):
        self.line_width = self.line_width_scale.get()

    def set_line_width_return(self,e):
        self.line_width = self.line_width_scale.get()

    def get_fill_colour(self):
        return self.fill_colour

    def get_line_colour(self):
        return self.line_colour

    def get_text_colour(self):
        return self.text_colour

    def get_line_width(self):
        return self.line_width


# For drawing rectangles and ellipses - left click, drag, release
# For drawing polygons and (poly)lines left click and release to set a point
#    - each subsequent left click/release draws a line from previous point
#    - middle click to end drawing
# For move left click, drag, release
# For delete left click/release
            
class DrawingApp(object):
    """Drawing demo."""

    def __init__(self, master=None):
        master.title("Drawing Demo")
        self._master = master
        self.customFont = font.Font(family="Helvetica", size=14)

        # Make a toolbar
        toolbar = Toolbar(master, self)
        toolbar.pack(fill=tk.X)
        # Make a canvas and set callbacks
        self.canvas = tk.Canvas(master,width=800, height=600, bg='black')
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.press_button1)
        self.canvas.bind("<Button-2>", self.press_button2)
        self.canvas.bind("<ButtonRelease-1>", self.releaseButton1)
        self.canvas.bind("<B1-Motion>", self.b1Motion)
        self.canvas.bind("<Motion>", self.motion)
        self.canvas.bind_all("<Key>", self.keypress)

        # Make a configuration bar
        self.configFrame = Configuration(master)
        self.configFrame.pack(fill=tk.X)
        self.drawing_fun = self.canvas.create_rectangle
        self.reset()

    def reset(self):
        """Reset values ready for next drawing."""
        self.drawing = None
        self.points = []
        self.string = ''
        

    def set_rect(self):
        """Set up for drawing rectangles"""
        if self.drawing_fun != self.canvas.create_rectangle:
            self.configFrame.set_fill_configs()
            self.drawing_fun = self.canvas.create_rectangle
        self.reset()

    def set_oval(self):
        """Set up for drawing ovals"""
        if self.drawing_fun != self.canvas.create_oval:
            self.configFrame.set_fill_configs()
            self.drawing_fun = self.canvas.create_oval
        self.reset()

    def set_poly(self):
        """Set up for drawing polygons"""
        if self.drawing_fun != self.canvas.create_polygon:
            self.configFrame.set_fill_configs()
            self.drawing_fun = self.canvas.create_polygon
        self.reset()

    def set_line(self):
        """Set up for drawing polylines"""
        if self.drawing_fun != self.canvas.create_line:
            self.configFrame.set_line_configs()
            self.drawing_fun = self.canvas.create_line
        self.reset()

    def set_text(self):
        """Set up for drawing text"""
        if self.drawing_fun != self.canvas.create_text:
            self.configFrame.set_text_configs()
            self.drawing_fun = self.canvas.create_text
        self.reset()

    def set_move(self):
        """Set up for moving"""
        if self.drawing_fun not in [self.canvas.move, self.canvas.delete]:
            self.configFrame.hide_configs()
        self.drawing_fun = self.canvas.move

    def set_delete(self):
        """Set up for deleting"""
        if self.drawing_fun not in [self.canvas.move, self.canvas.delete]:
            self.configFrame.hide_configs()
        self.drawing_fun = self.canvas.delete

    def press_button1(self, e):
        """Left button is pressed"""
        # Drawing rectangles and ovals
        if self.drawing_fun in \
               [self.canvas.create_rectangle,self.canvas.create_oval]: 
            self.startx = e.x
            self.starty = e.y
            self.drawing = \
                self.drawing_fun(e.x, e.y, e.x, e.y,
                                 outline = self.configFrame.get_line_colour(),
                                 fill = self.configFrame.get_fill_colour())
        # Drawing polygons and polylines
        elif self.drawing_fun in \
                [self.canvas.create_polygon, self.canvas.create_line]:
            self.points.extend([e.x,e.y])
        # Drawing text
        elif self.drawing_fun == self.canvas.create_text:
            self.string = ''
            self.drawing = self.drawing_fun(e.x, e.y ,text=self.string,
                                            font = self.customFont,
                                            fill=self.configFrame.get_text_colour())
        # Moving object
        elif self.drawing_fun == self.canvas.move:
            self.startx = e.x
            self.starty = e.y
            self.moveID = self.canvas.find_closest(e.x, e.y)
        # Deleting object
        elif self.drawing_fun == self.canvas.delete:
            ID = self.canvas.find_closest(e.x, e.y)
            self.canvas.delete(ID)

    def releaseButton1(self, e):
        """Left button is released"""
        if self.drawing_fun in \
               [self.canvas.create_rectangle,
                self.canvas.create_oval,
                self.canvas.move]: 
            self.drawing = None



    def keypress(self, e):
        "Keyboard key is pressed"""
        if self.drawing_fun == self.canvas.create_text:
            if e.keysym == 'BackSpace':
                #if backspace is pressed remove last character typed
                self.string = self.string[:-1]
            else:
                self.string += e.char
            self.canvas.itemconfigure(self.drawing, text = self.string)
            
    def motion(self, e):
        """Mouse motion without key press"""
        if self.drawing_fun in \
               [self.canvas.create_polygon, self.canvas.create_line]:
            if len(self.points) == 2 and not self.drawing:
                 self.drawing = \
                    self.canvas.create_line(self.points+[e.x,e.y],
                                            fill = 'white')
            elif self.drawing:
                self.canvas.coords(*([self.drawing]+self.points+[e.x,e.y]))

    def b1Motion(self,e):
        """Motion with left mouse pressed"""
        if self.drawing_fun in \
               [self.canvas.create_rectangle,self.canvas.create_oval]: 
            self.canvas.coords(self.drawing, self.startx, self.starty,
                               e.x, e.y)
        elif self.drawing_fun == self.canvas.move:
            dx = e.x - self.startx
            dy = e.y - self.starty
            self.startx = e.x
            self.starty = e.y
            self.canvas.move(self.moveID, dx, dy)
    
    def press_button2(self, e):
        """Middle mouse button pressed."""
        if self.drawing_fun == self.canvas.create_polygon:
            self.canvas.delete(self.drawing)
            self.points.extend([e.x,e.y])
            self.drawing_fun(self.points,
                             outline = self.configFrame.get_line_colour(),
                             fill = self.configFrame.get_fill_colour())
            self.points = []
            self.drawing = None
        elif self.drawing_fun == self.canvas.create_line:
            self.canvas.delete(self.drawing)
            self.points.extend([e.x,e.y])
            self.drawing_fun(self.points,
                             fill = self.configFrame.get_line_colour(),
                             width=self.configFrame.get_line_width())
            self.points = []
            self.drawing = None

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
