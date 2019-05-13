class frame_row(App):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self._row_id = 1

    def get_row_id(self):
        return self._row_id
    
    def add_row(self):
        self._row_id += 1

    def accept_row(self, row_id):
        
        














##    def add_quick_queue(self):
##        queue = self.quick_queue
##        num = 1
##        s = queue[-1]
##        for row in (1,len(queue)+1):
##            row = tk.Frame(self._frame_quick, bg = 'white')
##            row.pack(side = tk.BOTTOM, fill=tk.X,padx = 20)
##            if s.get_num() == 0:   
##                self._num = tk.Label(row, text = num, font=('Helvetica', 10), width = 2, bg = 'white')
##                self._num.pack(side = tk.LEFT, anchor = tk.W)
##                num += 1
##                self._name = tk.Label(row, text = s.get_name(), font=('Helvetica', 10), width = 15, bg = 'white')
##                self._name.pack(side = tk.LEFT, anchor = tk.W)
##                self._questions_asked = tk.Label(row, text = s.get_num(), font=('Helvetica', 10), width = 13, bg = 'white')
##                self._questions_asked.pack(side = tk.LEFT, anchor = tk.W)
##                self._time = tk.Label(row, text = s.display_wait_time(), font=('Helvetica', 10), width = 15, bg = 'white')
##                self._time.pack(side = tk.LEFT, anchor = tk.W)
##            if len(queue) > 1:
##                # config data
##                pass

    def queue_row(self, question_type):
        """
        Parameter:
            student(Student)
            question_type(str): either 'Long' or 'Quick'"""
##  clean the frames
##        self._frame_quick_queue = tk.Frame(self._frame_quick, bg = 'white')
##        self._frame_quick_queue.pack(fill=tk.X,padx = 20)
##        self._frame_long_queue = tk.Frame(self._frame_long, bg = 'white')
##        self._frame_long_queue.pack(fill=tk.X,padx = 20)

        num = 1
        
        if question_type == 'Long':
            self._frame_long_queue.destroy()
            self._frame_long_queue = tk.Frame(self._frame_long, bg = 'white')
            self._frame_long_queue.pack(fill=tk.X,padx = 20)
            frame = self._frame_long_queue
            queue = self.long_queue.get_queue()
            
        else:
            self._frame_quick_queue.destroy()
            self._frame_quick_queue = tk.Frame(self._frame_quick, bg = 'white')
            self._frame_quick_queue.pack(fill=tk.X,padx = 20)
            frame = self._frame_quick_queue
            queue = self.quick_queue.get_queue()
            
        for i in queue:
            self._frame_row = tk.Frame(frame, bg = 'white')
            self._frame_row.pack(fill=tk.X)
            print(queue)
            s = queue[num-1]
            
            self._num = tk.Label(self._frame_row, text=num, font=('Helvetica', 10), width = 2, bg = 'white')
            self._num.pack(side = tk.LEFT, anchor = tk.W)
            
            
            self._name = tk.Label(self._frame_row, text = s.get_name(), font=('Helvetica', 10), width = 15, bg = 'white')
            self._name.pack(side = tk.LEFT, anchor = tk.W)
            self._questions_asked = tk.Label(self._frame_row, text = s.get_num(), font=('Helvetica', 10), width = 13, bg = 'white')
            self._questions_asked.pack(side = tk.LEFT, anchor = tk.W)
            self._time = tk.Label(self._frame_row, text = s.display_wait_time(), font=('Helvetica', 10), width = 15, bg = 'white')
            self._time.pack(side = tk.LEFT, anchor = tk.W)
            
            self._accept_button = tk.Button(self._frame_row, bg = 'PaleGreen3', relief="groove",text='    ', font=('arial', 7))
                                            #command=self.press_accept)
            self._accept_button.pack(side = tk.LEFT, anchor = tk.W, padx = (15,5))
            self._accept_button.bind('<Button-{}>'.format(num*2-1), self.pressaccept)
            
            self._cancel_button = tk.Button(self._frame_row, bg = 'red',relief="groove", text='    ', font=('arial', 7))
                                           #command=self.press_cancel)
            self._cancel_button.pack(side = tk.LEFT, anchor = tk.W, padx = 5)
            self._cancel_button.bind('<Button-{}>'.format(num*2), self.pressaccept)

            num += 1

### updating
##    def update(self):
##        if len(self.long_queue.get_queue()) != 0:
##            self._master.after(100000,self.queue_row('Long'))
##        if len(self.quick_queue.get_queue()) != 0:
##            self._master.after(100000,self.queue_row('Quick'))
##
##    def update_wait(self):
##        self._time.config(text = student.display_wait_time())                                               

