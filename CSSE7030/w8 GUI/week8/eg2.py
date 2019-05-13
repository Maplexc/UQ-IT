# Same as eg1 but creating an App class and give a window title

# Best to import like this
import tkinter as tk 

class App(object):
    
    def __init__(self, master):   # master is the tk root object
        self._master=master
        self._master.title("Example 2")
        self._master.geometry("600x400")

root=tk.Tk()
app = App(root)
root.mainloop()
