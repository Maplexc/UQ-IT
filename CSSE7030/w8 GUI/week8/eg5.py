# Change layout

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 5")
        self._master.geometry("600x400")
        self._label = tk.Label(self._master, text="A label", bg="green")
        # pack it
        self._label.pack(side=tk.LEFT, expand=1, fill=tk.Y)#anchor=tk.SW)#, fill=tk.Y, pady=100, ipadx=100) 
        # create a button
        self._button = tk.Button(self._master, text="Press Me",fg="green",
                                 command=self.press_me)
        # pack it - the button (suroundings) consume all available space
        self._button.pack(side=tk.LEFT, expand=1)
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
