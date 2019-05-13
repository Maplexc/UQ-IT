import tkinter as tk

class Grid(tk.Frame):
    """A tkinter grid"""
    def __init__(self, master, columns, *args, **kwargs):
        """ construct a new grid
        Parameters:
            master(tk.Tk|tk.Frame): Frame containing this widget
            columns(int): amount of columns in the grid
        """
        super().__init__(master, *args,**kwargs)
        self._row = 0

        # configure the grid to fill the space
        for column in range(columns):
            tk.Grid.columnconfigure(self, column, weight = 1)

    def add_row(self, values):
        """
        Append a new row of values to the grid

        Parameters:
            values(tuple<*>): values stored in this row
        """
        for column, value in enumerate(value):
            label = tk.Label(self, text = value)
            label.grid(row = self._row, column = column, sticky = tk.W)
        self._row += 1

def test(a,b):
    if a == 1:
        print(a)
        return
    else:
        print(b)
    print('b2')
