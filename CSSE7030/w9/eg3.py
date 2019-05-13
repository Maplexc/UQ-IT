# Using a canvas and events and making widgets

import tkinter as tk 
import random

class Controls(tk.Frame):   # Controls is a particular subclass of tk.Frame
    def __init__(self, master):
        super().__init__(master) # use super().__init__ to inherite from superclass
        tk.Button(self, text="Add", command=self.add).pack(side=tk.LEFT) # using self, for Controls is a frame
        tk.Button(self, text="Move", command=self.move).pack(side=tk.LEFT)
        tk.Button(self, text="Delete", command=self.delete).pack(side=tk.LEFT)
        self._mode = "add"

    def add(self):
        self._mode = "add"

    def move(self):
        self._mode = "move"

    def delete(self):
        self._mode = "delete"

    def get_mode(self):
        return self._mode
        

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 3")
        self._master.geometry("600x400")
        self._controls = Controls(self._master) # get interaction between 2 classes
        self._controls.pack() # controls is a frame, so need to pack it
        # canvas using to draw
        self._canvas = tk.Canvas(self._master, bg='white')
        self._canvas.pack(fill=tk.BOTH, expand=1)
        self._canvas.bind("<Button-1>", self.press1)
        self._canvas.bind("<B1-Motion>", self.motion1)
        self._canvas.bind("<ButtonRelease-1>", self.release1)
        self.save_x = None
        self.save_y = None
        self.id = None

    def delete(self):
        self._canvas.delete(tk.ALL)

    def press1(self, e):
        mode = self._controls.get_mode() # get the mode (add, move, or delete)
        if mode == "add":
            d = 5+20*random.random()
            self._canvas.create_oval([(e.x, e.y), (e.x+d, e.y+d)], fill="red")
            # or self._canvas.create_oval([e.x, e.y, e.x+d, e.y+d], fill="red")
            self._canvas.create_line([(e.x, e.y), (e.x, e.y+d),
                                      (e.x+d, e.y+d), (e.x+d, e.y),
                                      (e.x, e.y)])
            #self._canvas.create_polygon([(e.x, e.y), (e.x, e.y+d),
            #                          (e.x+d, e.y+d), (e.x+d, e.y)], fill="")
        elif mode == "move":
            self.id = self._canvas.find_closest(e.x,e.y)
            self.save_x = e.x
            self.save_y = e.y
        else:
            self._canvas.delete(self._canvas.find_closest(e.x, e.y))
            # or self._canvas.delete(self.id)
       
    def motion1(self, e):
        mode = self._controls.get_mode()
        if mode == "move":
            dx = e.x - self.save_x # dx, dy is the difference between the the position you click and the item
            dy = e.y - self.save_y
            self.save_x = e.x
            self.save_y = e.y
            self._canvas.move(self.id, dx, dy)

    def release1(self, e):
        # not really needed
        #print("release", e.x, e.y)
        pass

root = tk.Tk()
app = App(root)
root.mainloop()

