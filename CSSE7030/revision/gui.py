import tkinter as tk

class ButtonsFrame(tk.Frame):

    def __init__(self, parent): # master is the tk root object
        tk.Frame.__init__(self,parent.root)
        b1 = tk.Button(self, text = 'A')
        b2 = tk.Button(self, text = 'B')
        b1.pack(expand = 1)
        b2.pack(expand = 1)

class MainWindow(object):
    def __init__(self,root):
        self._root = root
        label = tk.Label(root, text = 'Buttons')
        label.pack(side = tk.LEFT)
        bf = ButtonsFrame(self)


        
