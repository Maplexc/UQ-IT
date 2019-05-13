import tkinter as tk 

class App(object):
    
    def __init__(self, master):   
        self._master=master
        self._master.title("CSSE1001/CSSE7030 Queue")
        self._master.geometry("1000x650")


        # important
        self._frame_important = tk.Frame(self._master, bg = 'ivory')
        self._frame_important.pack(side=tk.TOP, fill = tk.X)
        self._label_important_title = tk.Label(self._frame_important, text='Important',
                                               font=('Helvetica', 14, 'bold'), fg = 'goldenrod',
                                               bg = 'ivory')
        self._label_important_title.pack(anchor = tk.NW, padx = 20, pady =(25,0))
        self._message_important = tk.Message(self._frame_important,text = "Individual assessment items must be solely your own work. While students are encouragd to have high-level conversations about the problems they are trying to solve, you must not look at another student's code or copy from it. The university uses sophisticated anti-collusion measures to automatically detect similarity between assignment submissions.", 
                                             font=('Helvetica', 10),
                                             bg = 'ivory', width = 980)
        self._message_important.pack(side = tk.TOP, anchor = tk.W, padx=20, ipady=10)#, fill = tk.X)

        # quick question
        self._frame_quick = tk.Frame(self._master, bg = 'white')
        self._frame_quick.pack(side = tk.LEFT, expand=1, fill=tk.BOTH)
        self._frame_quick_label = tk.Frame(self._frame_quick, bg= 'DarkSeaGreen1',
                                     borderwidth=1, relief="ridge")
        self._frame_quick_label.pack(padx=20, pady=(15,25), fill=tk.X)
        self._label_quick = tk.Label(self._frame_quick_label, text='Quick Questions',
                                     font=('Helvetica', 20, 'bold'), fg = 'ForestGreen',
                                     bg = 'DarkSeaGreen1')
        self._label_quick.pack(pady=15, fill=tk.X)
        self._label_quick_describe = tk.Label(self._frame_quick_label, text = "< 2 mins with a tutor",
                                              font=('Helvetica', 10),
                                              bg = 'DarkSeaGreen1')
        self._label_quick_describe.pack(pady = 10)
        self._message_quick_detail = tk.Message(self._frame_quick,
                                                text = """Some examples of quick questions:
                                                            · Syntax errors 
                                                            · Interpreting error output
                                                            · Assignment/MyPyTutor interpretation
                                                            · MyPyTutor submission issues""",
                                                font=('Helvetica', 10), anchor=tk.W,
                                                width = 240, bg = 'white')
        self._message_quick_detail.pack(side = tk.TOP, padx = 20, fill=tk.X)
        self._quick_button = tk.Button(self._frame_quick, text = 'Request Quick Help',
                                       fg = 'White', bg = 'PaleGreen3',
                                       borderwidth=2, relief="groove",
                                       command=self.pressQuick)
        self._quick_button.pack(ipadx = 5, ipady = 5, pady = 15)
        
        # long question                             
        self._frame_long = tk.Frame(self._master, bg = 'white')
        self._frame_long.pack(side = tk.LEFT, expand=1, fill=tk.BOTH)
        self._frame_long_label = tk.Frame(self._frame_long, bg= 'LightSkyBlue1',
                                          borderwidth=1, relief="ridge")
        self._frame_long_label.pack(padx=20, pady=(15,25), fill=tk.X)
        
        
        self._label_long = tk.Label(self._frame_long_label, text='Long Questions',
                                    font=('Helvetica', 20, 'bold'), fg = 'DodgerBlue3',
                                    bg = 'LightSkyBlue1')
        self._label_long.pack(pady=15, fill=tk.X)
        self._label_long_describe = tk.Label(self._frame_long_label, text="> 2 mins with a tutor",
                                             font=('Helvetica', 10),
                                             bg = 'LightSkyBlue1')
        self._label_long_describe.pack(pady = 10)
        self._message_long_detail = tk.Message(self._frame_long,
                                                text = """Some examples of long questions:
                                                            · Open endeed questions
                                                            · How to start a problem
                                                            · How to improve code
                                                            · Debugging
                                                            · Assignment help""",
                                                font=('Helvetica', 10), anchor=tk.W,
                                                width = 240, bg = 'white')
        self._message_long_detail.pack(side = tk.TOP, padx = 20, fill=tk.X)
        self._long_button = tk.Button(self._frame_long, text = 'Request Long Help',
                                       fg = 'White', bg = 'SkyBlue',
                                       borderwidth=2, relief="groove",
                                       command=self.pressLong)
        self._long_button.pack(ipadx = 5, ipady = 5, pady = 15)

##    def queueview(self):
        # quick
##        line1_quick = tk.Canvas(self._frame_quick, bg = 'white', highlightthickness=0, height = 10)
##        line1_quick.pack(side=tk.TOP, fill=tk.X, padx = 20)
##        line1_quick.create_line(0,0,500,0, fill='grey78')
##        self.label_numofstudent_quickqueue = tk.Label(self._frame_quick,
##                                                      text = '{} students in queue.'.format('No'),
##                                                      bg = 'white')
##                                                      # {} change to variable
##        self.label_numofstudent_quickqueue.pack(anchor = tk.W, padx = 20)
##        canvas_quick = tk.Canvas(self._frame_quick, bg = 'white', highlightthickness=0, height = 40)
##        canvas_quick.pack(side=tk.TOP, fill=tk.X, padx = 20)
##        canvas_quick.create_line(0,5,500,5, fill='grey78')
##        canvas_quick.create_text(115,20, text='#   Name           Questions Asked   Time', font=('Helvetica', 9, 'bold'))
##        canvas_quick.create_line(0,35,500,35, fill='grey78')

        # long
##        line1_long = tk.Canvas(self._frame_long, bg = 'white', highlightthickness=0, height = 10)
##        line1_long.pack(side=tk.TOP, fill=tk.X, padx = 20)
##        line1_long.create_line(0,0,500,0, fill='grey78')
##        self.label_numofstudent_longqueue = tk.Label(self._frame_long,
##                                                     text = '{} students in queue.'.format('No'),
##                                                     bg = 'white')
##                                                     # {} change to variable
##        self.label_numofstudent_longqueue.pack(anchor = tk.W, padx = 20)
##        canvas_long = tk.Canvas(self._frame_long, bg = 'white', highlightthickness=0, height = 40)
##        canvas_long.pack(side=tk.TOP, fill=tk.X, padx = 20)
##        canvas_long.create_line(0,5,500,5, fill='grey78')
##        canvas_long.create_text(115,20, text='#   Name           Questions Asked   Time', font=('Helvetica', 9, 'bold'))
##        canvas_long.create_line(0,35,500,35, fill='grey78')




    def pressQuick(self):
        print('Quick')

    def pressLong(self):
        print('Long')

        
##        self._label = tk.Label(self._frame_important, text="Important")
##        # pack it
##        self._label.pack()
##        # create a frame - a container whose parent is master
##        self._frame = tk.Frame(self._master, bg = 'yellow')
##        # don't forget to pack the frame
##        self._frame.pack()
##        # put two buttons in frame - frame is their parent
##        self._button1 = tk.Button(self._frame, text="Press Me",fg="green",
##                                  command=self.press1)
##        # pack it
##        self._button1.pack(side=tk.LEFT, expand=1)
##        # Another button
##        self._button2 = tk.Button(self._frame, text="No - Press Me",fg="green",
##                                  command=self.press2)
##        # pack it
##        self._button2.pack(side=tk.LEFT, expand=1)
##        
##        self._state = False
##
##    def redraw(self):
##        self._state=not self._state
##        if self._state:
##            self._label.config(bg="red")
##        else:
##            self._label.config(bg="green")
##        self._master.after(1000,self.redraw)
##        
##    def press1(self):
##        self._state = True
##        self.redraw()
##
##    def press2(self):
##        self._state = False
##        self.redraw()


root = tk.Tk()
app = App(root)
root.mainloop()
