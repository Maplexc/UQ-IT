# Using a text widget - with a file menu and filedialog

## menu bar - 'file edit format run options window help'



import tkinter as tk 
from tkinter import filedialog

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("Example 10")
        self._text = tk.Text(self._master)
        self._text.pack(expand=1, fill=tk.BOTH)
        

        # File menu
        menubar = tk.Menu(self._master)
        # tell master what it's menu is
        self._master.config(menu=menubar) # have python recognize the menu
        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        # 3 command will define later

        helpmenu = tk.Menu(menubar)
        menubar.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='From Web',command=self.web_help)
        helpmenu.add_command(label='From friends',command=self.friends_help)
                             
        self._filename = None

    def new_file(self):
        self._text.delete("1.0", tk.END) # "1.0" - 1: first line, 0: first character (delete from the begining to end)
        self._filename = None
        self._master.title("New File")

    def save_file(self):
        if self._filename is None:
            filename = filedialog.asksaveasfilename()
            if filename: # filename cannot be None
                self._filename = filename
        if self._filename:
            self._master.title(self._filename)
            fd = open(self._filename, 'w')
            fd.write(self._text.get("1.0", tk.END))
            fd.close()
            # OR can use - with open(self._filename, 'w') as fd:
            

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self._filename = filename
            self._master.title(self._filename)
            fd = open(filename, 'r')
            self._text.insert(tk.INSERT, fd.read())
            fd.close()

    def web_help(self):
        pass

    def friends_help(self):
        pass
root = tk.Tk()
app = App(root)
root.mainloop()
