import tkinter as tk

class App(object):

    def __init__(self, master):
        self._master = master
        self._master.title('Example 7')
        self._master.geometry('600x400')
        # create a label object - first argument is always the 'tk parent'
        self._label = tk.Label(self._master, text = 'A label', bg = 'green')
        # pack it - without this it won't appear in the window
        self._label.pack()
        self._frame = tk.Frame(self._master, bg = 'yellow')
        self._frame.pack() # 2 button cover all the frame, so we cannot see the yellow background
        self._button1 = tk.Button(self._frame, text = 'Press me', fg='green',
                                  command=self.press1)
        self._button1.pack(side=tk.LEFT, expand=1)
        self._button2 = tk.Button(self._frame, text='No - Press me', fg='green',
                                  command = self.press2)
        self._button2.pack(side=tk.LEFT, expand=1)
        
        self._state = False

    def redraw(self):
        self._state = not self._state
        if self._state:
            self._label.config(bg='red')
        else:
            self._label.config(bg='green')
        self._master.after(1000, self.redraw) #1000msec
        
    def press1(self):
        self._state = True
        self.redraw()

    def press2(self):
        self._state = False
        self.redraw()


        
root = tk.Tk()
app = App(root)
root.mainloop()



        
                         #side=tk.LEFT, anchor=tk.NW) # anchor in the north-west
                         #expand=1, fill=tk.Y, pady =50, ipadx=50)
            # default side is at the top
            # fill - fill the rest of the area (fill=tk.BOTH), BOTH, X, Y
            # pady - fill the area not going to the end (outside the label)
            # ipadx - control the weidth of the label (within the label)
                        
        # create a button
#        self._button = tk.Button(self._master, text = 'Press me', bg = 'green',
#                                 command = self.press_me)
                                # don't enter the () in command, as command is execute the method
                                # with (), the method will return a value
        # pack it
#        self._button.pack(side=tk.LEFT, expand = 1, anchor=tk.E)
        # to determine what is to be 'displayed'

        

##    def redraw(self):
##        if self._state:
##            self._button.config(text='Press me again', bg='red') # config - can change the characteristics of button
##            self._label.config(bg = 'red')
##        else:
##            self._button.config(text='Press me', bg='green')
##            self._label.config(bg = 'green')
##
##    def press_me(self):
##        self._state = not self._state
##        self.redraw()
