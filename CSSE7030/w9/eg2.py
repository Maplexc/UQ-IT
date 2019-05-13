# Using a canvas and events

import tkinter as tk 
import random

class App(object):
    
    def __init__(self, master):   
        master.title("Example 11")
        master.geometry("300x200")
        # added
        tk.Button(master, text="Delete", command=self.delete).pack() # create a button and pack it (default packing is on the top)
        self._canvas = tk.Canvas(master, bg='white')
        self._canvas.pack(expand=1,fill=tk.BOTH)
        self._canvas.bind("<Button-1>", self.press1)
        self._canvas.bind("<Motion>", self.motion1)
        self._canvas.bind("<ButtonRelease-1>", self.release1)
        self._canvas.bind_all("<Key>", self.key_press)

    # added
    def delete(self):
        self._canvas.delete(tk.ALL)

    def press1(self, e):
        print("press", e.x, e.y)
        d = 5+20*random.random() # create a random red circle, changing the number can get bigger or small circle
        self._canvas.create_oval([(e.x, e.y), (e.x+d, e.y+d)], fill="red")
        # or self._canvas.create_oval([e.x, e.y, e.x+d, e.y+d], fill="red")
        #self._canvas.create_line([(e.x, e.y), (e.x, e.y+d),
                                  #(e.x+d, e.y+d), (e.x+d, e.y),
                                  #(e.x, e.y)]) # draw a square
        self._canvas.create_polygon([(e.x, e.y), (e.x, e.y+d),
                                  (e.x+d, e.y)], fill="green")
       
    def motion1(self, e):
        print("motion", e.x, e.y)

    def release1(self, e):
        print("release", e.x, e.y)

    def key_press(self, e):
        print(e.char, e.keysym, e.keycode)


root = tk.Tk()
app = App(root)
root.mainloop()

# reminder
# move(ID, dx, dy)
# find_closest(x,y)
# id.coords
