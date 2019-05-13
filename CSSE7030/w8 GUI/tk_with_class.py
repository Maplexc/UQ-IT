import tkinter as tk

class App(object):

    def __init__(self, master): # master is the tk root object
        self._master = master
        self._master.title('Example 2')
        self._master.geometry('600x400') #geometry of the window to start with

root = tk.Tk()
app = App(root)
root.mainloop()
        
