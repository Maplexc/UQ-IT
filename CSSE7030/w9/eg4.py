# Model View Controller pattern (MVC) example
# model - object
# view - gui
# controller - button

import tkinter as tk 
import random
from tkinter import filedialog

class Circle(object):
    def __init__(self, x, y, r, c):
        self._x = int(x)
        self._y = int(y)
        self._r = int(r)
        self._c = c

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def get_bounds(self):
        return [(self._x - self._r, self._y - self._r), 
                (self._x + self._r, self._y + self._r)] # extremity

    def get_colour(self):
        return self._c

    def __repr__(self):
        return "Circle({0}, {1}, {2}, {3})".format(self._x, self._y, 
                                                   self._r, self._c)

class Model(object):
    def __init__(self):
        self._circles = []

    def load_circles(self, filename):
        fd = open(filename, "r")
        self._circles = []
        for line in fd:
            line = line.strip()
            if line:
                self._circles.append(Circle(*line.split())) # Circle(*line.split()) = put each statement into Circle argument
                print(self._circles)
    
    def get_circles(self):
        return self._circles

    def move(self, c, dx, dy):
        # c is a Circle(x,y,r,c)
        c.move(dx, dy)

class Controls(tk.Frame): # control class is a frame class from tkinter
    def __init__(self, master, parent):
        super().__init__(master) # inheriate from tkinter
        tk.Button(self, text="Open", command=parent.open).pack(side=tk.LEFT) # parent class, which is App class, open method
        tk.Button(self, text="Move", command=self.move).pack(side=tk.LEFT)
        tk.Button(self, text="Delete", command=self.delete).pack(side=tk.LEFT)
        self._mode = "move"

    def move(self):
        self._mode = "move"

    def delete(self):
        self._mode = "delete"

    def get_mode(self):
        return self._mode
        
class View(tk.Canvas):
    def __init__(self, master, model, controls):
        super().__init__(master, bg='white')
        self.bind("<Button-1>", self.press1)
        self.bind("<B1-Motion>", self.motion1)
        self.save_x = None
        self.save_y = None
        self.id = None
        self._model = model
        self._controls = controls
        self.redraw()
        self.ids = []

    def redraw(self):
        self.ids = []
        self.delete(tk.ALL)
        for c in self._model.get_circles():
            self.ids.append(self.create_oval(c.get_bounds(), 
                                             fill=c.get_colour()))
            
        
    def press1(self, e):
        mode = self._controls.get_mode()
        if mode == "move":
            self.index = self.ids.index(self.find_closest(e.x,e.y)[0])
            self.save_x = e.x
            self.save_y = e.y
        else:
            cid = self.find_closest(e.x, e.y)[0]
            index = self.ids.index(cid)
            self._model.get_circles().pop(index)
            self.redraw()
       
    def motion1(self, e):
        mode = self._controls.get_mode()
        if mode == "move":
            dx = e.x - self.save_x
            dy = e.y - self.save_y
            self.save_x = e.x
            self.save_y = e.y
            self._model.move(self._model.get_circles()[self.index], dx, dy)
            self.redraw()

class App(object):
    
    def __init__(self, master):
        master.title("Example 3")
        master.geometry("600x400")
        self._model = Model()
        self._controls = Controls(master, self)
        self._controls.pack()
        self._view = View(master, self._model, self._controls)
        self._view.pack(expand=1, fill=tk.BOTH)

    def open(self):
        filename = filedialog.askopenfilename()
        if filename:
            self._model.load_circles(filename)
            self._view.redraw()

root = tk.Tk()
app = App(root)
root.mainloop()

