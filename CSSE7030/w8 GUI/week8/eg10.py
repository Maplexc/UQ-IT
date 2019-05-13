# Using a text widget

import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 10")
        self._master.geometry("600x400")
        self._frame = tk.Frame()
        self._frame.pack()
        self._button1 = tk.Button(self._frame, text="Dump Text",
                                  command=self.dump)
        self._button1.pack(side=tk.LEFT)
        self._button2 = tk.Button(self._frame, text="Clear",
                                  command=self.clear)
        self._button2.pack(side=tk.LEFT)

        self._text = tk.Text(self._master)
        self._text.pack()
        self._text.insert(tk.INSERT, "Some default text")
        self._text.insert("2.4", "More text") # 2.4 is the position of the text, first figure means line, second mean position
    def dump(self):
        print(self._text.get("1.0", tk.END))

    def clear(self):
        self._text.delete("1.0", tk.END)

root = tk.Tk()
app = App(root)
root.mainloop()
