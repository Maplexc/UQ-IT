"""
Simple GUI programming exercise to demonstrate component layout
and event handling.
"""

__copyright__ = "Copyright 2018, University of Queensland"


import tkinter as tk
from tkinter import messagebox 

class SampleApp(object) :
    def __init__(self, master) :
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)

        self._lbl = tk.Label(master, text="Choose a button") # bg=...
        self._lbl.pack(side=tk.TOP, fill = tk.BOTH, expand = 1)
            # expand 1/True, 0/False
            # fill tk.X, Y, BOTH
                  
        bottom_frame1 = tk.Frame(master) # tk.Frame()
        bottom_frame1.pack(side=tk.TOP) # expand or fill the frame if you want to pack on the side
        btn1 = tk.Button(bottom_frame1, text="Change to Blue", command=self.change_blue)
        btn1.pack(side=tk.LEFT, pady = 10)
        btn2 = tk.Button(bottom_frame1, text="Change to Green", command=self.change_green)
        btn2.pack(side=tk.LEFT, pady = 10)

        bottom_frame2 = tk.Frame(master)
        bottom_frame2.pack(side=tk.TOP)
        bottom_lbl = tk.Label(bottom_frame2, text='Change the colour to:')
        bottom_lbl.pack(side=tk.LEFT, expand=1)
        self.entry = tk.Entry(bottom_frame2)
        self.entry.pack(side=tk.LEFT,pady=10)
        btn3 = tk.Button(bottom_frame2, text='Change it!', command=self.change_it)
        btn3.pack(side=tk.LEFT)

        ## side, anchor, expand, fill
            # side - widgets on the top, bottom, left, right side of the windows
            # anchor - e.g. the text in label on w, n, s, e, wn, ws, ... within the frame
        ## padx/pady/ipadx/ipady
        ## .config - change any attribute of widgets (e.g.to modify the text and colour)    

    def change_blue(self) :
        self._lbl.config(bg='blue')

    def change_green(self):
        self._lbl.config(bg='green')

    def change_it(self):
        colour = self.entry.get()
        try:
            self._lbl.config(bg=colour)
        except tk.TclError:    # to specify the error, cuz if only use except, it will include all the error
            messagebox.showerror('Invalid colour', '{} is not a colour!'.format(self.entry.get()))
            # need to import messagebox

        


if __name__ == "__main__" :
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()
