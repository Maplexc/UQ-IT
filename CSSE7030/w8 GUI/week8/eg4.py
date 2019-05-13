# Adding a button and a label but with different layout
# change to using forground colour

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 4")
        self._master.geometry("600x400")
        self._label = tk.Label(self._master, text="A label", bg="green")
        # pack it
        self._label.pack(side=tk.LEFT, expand=1, fill=tk.Y, pady=100, ipadx=30)
        # create a button
        self._button = tk.Button(self._master, text="Press Me",fg="green",
                                 command=self.press_me)
        # pack it
        self._button.pack(side=tk.LEFT)
        self._state = False

    def redraw(self):
        if self._state:
            self._button.config(text="Press Me Again", fg="red")
            self._label.config(bg="red")
        else:
            self._button.config(text="Press Me", fg="green")
            self._label.config(bg="green")
            
        
    def press_me(self):
        self._state = not self._state
        self.redraw()


root = tk.Tk()
app = App(root)
root.mainloop()