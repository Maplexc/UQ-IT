# Adding a button and a label

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 3")
        self._master.geometry("600x400")
        # create a label object - first argument is always the
        # "tk parent"
        self._label = tk.Label(self._master, text="A label", bg="green")
        # pack it - without this it won't appear in the window
        self._label.pack() # default - same as pack(side=tk.TOP)
        # create a button
        self._button = tk.Button(self._master, text="Press Me",bg="green",
                                 command=self.press_me)
        # pack it
        self._button.pack()
        # to determine what is to be "displayed"
        self._state = False

    def redraw(self):
        if self._state:
            self._button.config(text="Press Me Again", bg="red")
            self._label.config(bg="red")
        else:
            self._button.config(text="Press Me", bg="green")
            self._label.config(bg="green")
            
        
    def press_me(self):
        self._state = not self._state
        self.redraw()


root = tk.Tk()
app = App(root)
root.mainloop()
